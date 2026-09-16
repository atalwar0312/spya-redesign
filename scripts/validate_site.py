"""Structural validation; does not claim browser or assistive-technology QA."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from collections import Counter
import re
R=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=set();self.links=[];self.h1=0;self.title=0;self.text=[];self.images=[];self.headings=[];self.current=None;self.lang=None;self.viewport=False;self.duplicate_ids=[]
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if a.get('id'):
            if a['id'] in self.ids:self.duplicate_ids.append(a['id'])
            self.ids.add(a['id'])
        if t=='html':self.lang=a.get('lang')
        if t=='meta' and a.get('name')=='viewport':self.viewport=True
        if t=='h1':self.h1+=1
        if t=='title':self.title+=1
        if t in ('h1','h2','h3','summary'):self.current=[]
        if t=='img':self.images.append(a)
        for k in ('href','src'):
            if k in a:self.links.append((t,k,a[k]))
    def handle_endtag(self,t):
        if t in ('h1','h2','h3','summary') and self.current is not None:
            self.headings.append(''.join(self.current));self.current=None
    def handle_data(self,x):
        self.text.append(x)
        if self.current is not None:self.current.append(x)
pages={};errors=[]
for f in R.glob('*.html'):
    p=Page();p.feed(f.read_text());pages[f.name]=p
minor={'a','an','and','as','at','but','by','for','from','in','into','of','on','or','the','to','with'}
for name,p in pages.items():
    if p.h1!=1 or p.title!=1:errors.append(name+': heading/title count')
    if not p.viewport or p.lang!='en':errors.append(name+': language/viewport missing')
    if p.duplicate_ids:errors.append(name+': duplicate IDs')
    anchors=Counter(link for tag,key,link in p.links if tag=='a')
    for url,count in anchors.items():
        if count>1:errors.append(name+': repeated destination '+url)
    for a in p.images:
        if 'alt' not in a:errors.append(name+': image missing alternative text')
    for heading in p.headings:
        for word in heading.split():
            w=word.strip('.,:?!()')
            if w and w[0].islower() and w not in minor:errors.append(name+': capitalization '+heading)
    for tag,key,link in p.links:
        u=urlsplit(link)
        if tag=='a' and u.hostname=='spya.org' and not u.path.endswith('.pdf'):
            errors.append(name+': old website referral '+link)
        if not u.scheme:
            dest=unquote(u.path) or name
            if not (R/dest).is_file():errors.append(name+': missing '+dest)
            if u.fragment and dest in pages and u.fragment not in pages[dest].ids:errors.append(name+': missing anchor '+link)
    text=' '.join(p.text)
    if re.search(r'\$\s*\d|registration (?:is )?open|register now|only \d+ spots',text,re.I):errors.append(name+': unverified availability/price claim')
css=(R/'css/styles.css').read_text()
if re.search(r'text-transform\s*:\s*uppercase',css):errors.append('Forced uppercase remains')
# Every live content page must be reachable from the homepage.
seen=set();todo=['index.html']
while todo:
    name=todo.pop()
    if name in seen:continue
    seen.add(name)
    for tag,key,url in pages[name].links:
        u=urlsplit(url)
        if tag=='a' and not u.scheme and u.path in pages and u.path not in seen:todo.append(u.path)
for name in set(pages)-seen-{'404.html'}:errors.append('Unreachable page '+name)
assert not errors,'\n'.join(errors)
print(f'PASS: {len(pages)} pages; local links/anchors, reachability, unique anchor destinations, heading capitalization, image alt attributes, language, and viewport.')
print('PASS: no old-site HTML referrals or unverified open-registration claims.')
print('Browser appearance, screen-reader usability, external availability, and transaction completion are not certified by these checks.')
