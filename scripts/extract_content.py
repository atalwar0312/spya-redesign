import json
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

BASE = "https://spya.org/"
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "source"
OUTPUT.mkdir(parents=True, exist_ok=True)

AGENT = "SPYAContentReviewBot"
MAX_PAGES = 60
session = requests.Session()
session.headers["User-Agent"] = AGENT
last_request = 0.0
delay = 2.0


def fetch(url):
    global last_request
    time.sleep(max(0, delay - (time.monotonic() - last_request)))
    try:
        return session.get(url, timeout=30, allow_redirects=False)
    finally:
        last_request = time.monotonic()


def clean_url(href, current):
    import re

    href = str(href).strip()
    if not href:
        return None

    # Normalize malformed absolute links before resolving relative links.
    href = re.sub(r"^(https?):/+(?=[^/])", r"\1://", href, flags=re.I)

    # Do not crawl links containing unescaped internal whitespace.
    if any(character.isspace() for character in href):
        return None

    absolute = urljoin(current, href)
    parts = urlsplit(absolute)
    if parts.scheme not in ("http", "https"):
        return None

    return urlunsplit(
        (parts.scheme, parts.netloc.lower(), parts.path or "/", parts.query, "")
    )


def is_page(url):
    parts = urlsplit(url)
    if parts.netloc != "spya.org" or parts.query:
        return False
    path = parts.path.lower()
    if path.startswith(("/wp-", "/feed", "/author/", "/tag/")):
        return False
    suffix = Path(path).suffix
    return not suffix or suffix in (".html", ".htm")


robots_url = urljoin(BASE, "robots.txt")
robots_response = fetch(robots_url)
robots = RobotFileParser()
robots.set_url(robots_url)

if robots_response.status_code == 404:
    robots.parse([])
elif robots_response.status_code == 200:
    if "<html" in robots_response.text[:500].lower():
        raise SystemExit("robots.txt returned HTML. Stop and review before crawling.")
    robots.parse(robots_response.text.splitlines())
else:
    raise SystemExit(
        f"Cannot verify crawling rules: HTTP {robots_response.status_code}. "
        "Share this message before continuing."
    )

crawl_delay = robots.crawl_delay(AGENT)
if crawl_delay:
    delay = max(delay, float(crawl_delay))
rate = robots.request_rate(AGENT)
if rate and rate.requests:
    delay = max(delay, rate.seconds / rate.requests)

seeds = [
    "", "about-us/", "sports/", "registration/", "board/", "calendar/",
    "baseball/", "basketball/", "cheer/", "post-1616/",
    "football/", "lacrosse/", "nfl-flag/", "soccer/", "softball-2/"
]
queue = deque(urljoin(BASE, path) for path in seeds)
seen = set()
pages = []
issues = []


def save_results():
    result = {
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "source": BASE,
        "notice": "Source material only; dates, fees and policies are unverified.",
        "pages": pages,
        "issues": issues,
        "remaining_urls": list(dict.fromkeys(queue)),
    }
    (OUTPUT / "spya_content.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    report = [
        "# SPYA source inventory",
        "",
        "Extracted content is not yet verified for publication.",
        "Image and document URLs are references, not downloaded files.",
        "",
    ]
    for page in pages:
        report.extend([
            f"## {page['title']}",
            f"Source: {page['url']}",
            "",
            page["text"],
            "",
        ])
    report.extend(["## Extraction issues", ""])
    report.extend(f"- {item['url']}: {item['reason']}" for item in issues)
    (OUTPUT / "spya_content.md").write_text(
        "\n".join(report), encoding="utf-8"
    )


try:
    while queue and len(seen) < MAX_PAGES:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)

        if not robots.can_fetch(AGENT, url):
            issues.append({"url": url, "reason": "Disallowed by robots.txt"})
            continue

        print(f"Reading {url}", flush=True)
        try:
            response = fetch(url)
        except requests.RequestException as error:
            issues.append({"url": url, "reason": str(error)})
            continue

        if response.status_code in (401, 403, 429):
            issues.append({
                "url": url,
                "reason": f"HTTP {response.status_code}; crawl stopped"
            })
            break

        if 300 <= response.status_code < 400:
            target = clean_url(response.headers.get("Location", ""), url)
            issues.append({"url": url, "reason": f"Redirect to {target}"})
            if target and is_page(target) and target not in seen:
                queue.append(target)
            continue

        if response.status_code != 200:
            issues.append({"url": url, "reason": f"HTTP {response.status_code}"})
            continue

        if "text/html" not in response.headers.get("Content-Type", "").lower():
            issues.append({"url": url, "reason": "Not an HTML page"})
            continue

        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.get_text(" ", strip=True) if soup.title else url

        all_links = set()
        for anchor in soup.select("a[href]"):
            link = clean_url(anchor["href"], url)
            if link:
                all_links.add(link)
                if is_page(link) and link not in seen:
                    queue.append(link)

        main = soup.find("main") or soup.find("article") or soup.body or soup
        content = BeautifulSoup(str(main), "html.parser")
        for element in content.select(
            "script, style, nav, footer, noscript, "
            "[role='navigation'], [role='contentinfo']"
        ):
            element.decompose()

        images = []
        for img in content.select("img"):
            source = img.get("data-src") or img.get("src")
            image_url = clean_url(source, url) if source else None
            if image_url:
                images.append({
                    "url": image_url,
                    "alt": img.get("alt", ""),
                    "reuse_approval": "Not checked",
                })

        lines = [
            line.strip()
            for line in content.get_text("\n", strip=True).splitlines()
            if line.strip()
        ]
        pages.append({
            "url": url,
            "title": title,
            "text": "\n".join(lines),
            "links": sorted(all_links),
            "images": images,
            "verification_status": "Needs review",
        })
        save_results()
finally:
    save_results()

print(f"\nSaved {len(pages)} pages; {len(issues)} issues recorded.")
print(f"Output folder: {OUTPUT}")
print("Finished. No registration forms were submitted.")
