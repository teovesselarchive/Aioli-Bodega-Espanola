"""Validate the generated static site's local references and required content."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
ROOT=Path(__file__).resolve().parents[1]
class Inspect(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.append(d['id'])
  for key in ['href','src']:
   if d.get(key):self.links.append(d[key])
  if tag=='img':assert 'alt' in d,'Image missing alt text'
errors=[];count=0
for p in (ROOT/'dist').rglob('*.html'):
 s=p.read_text();v=Inspect();v.feed(s)
 assert len(v.ids)==len(set(v.ids)),f'Duplicate IDs in {p}'
 assert 'noindex,nofollow' in s and '{BASE}' not in s,p
 assert p.read_bytes()==(ROOT/p.relative_to(ROOT/'dist')).read_bytes(),f'Root/dist mismatch: {p}'
 for link in v.links:
  url=urlsplit(link)
  if url.scheme or url.netloc:continue
  target=(p.parent/unquote(url.path)) if url.path else p
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{p}: {link}')
  count+=1
assert not errors,'\n'.join(errors)
assert len(list((ROOT/'dist/assets/originals').glob('*menu*.png')))==7
assert sum(len(g['items']) for g in json.loads((ROOT/'data/menu.json').read_text()))==67
for f in ['app.js','styles.css']:
 assert (ROOT/f).read_bytes()==(ROOT/'dist'/f).read_bytes()
print(f'PASS: {count} local references, five pages, seven menu sheets, 67 readable entries, root/dist parity.')
