from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re
R=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):super().__init__();self.ids=set();self.links=[];self.h1=0;self.title=0;self.text=[]
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.add(a['id'])
        if t=='h1':self.h1+=1
        if t=='title':self.title+=1
        for k in ('href','src'):
            if k in a:self.links.append((t,k,a[k]))
    def handle_data(self,x):self.text.append(x)
pages={};errors=[]
for f in R.glob('*.html'):
    p=Page();p.feed(f.read_text());pages[f.name]=p
for name,p in pages.items():
    if p.h1!=1 or p.title!=1:errors.append(name+': heading/title count')
    for tag,key,link in p.links:
        u=urlsplit(link)
        if tag=='a' and u.hostname=='spya.org' and not u.path.endswith('.pdf'):
            errors.append(name+': old website referral '+link)
        if not u.scheme:
            dest=unquote(u.path) or name
            if not (R/dest).is_file():errors.append(name+': missing '+dest)
            if u.fragment and dest in pages and u.fragment not in pages[dest].ids:errors.append(name+': missing anchor '+link)
    text=' '.join(p.text)
    if re.search(r'\$\s*\d|registration (?:is )?open|register now|only \d+ spots',text,re.I):errors.append(name+': unverified seasonal claim')
css=(R/'css/styles.css').read_text()
if re.search(r'text-transform\s*:\s*uppercase',css):errors.append('Forced uppercase remains')
assert not errors,'\n'.join(errors)
print(f'{len(pages)} pages checked: local links, fragment targets, primary headings and titles pass.')
print('No general old-site referrals, forced uppercase, prices or open-registration claims found.')
print('Visual, mobile and screen-reader checks require browser review.')
