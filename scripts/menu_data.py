"""Validate the complete menu data without overwriting its transcribed content."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
groups=json.loads((ROOT/'data/menu.json').read_text())
assert len(groups)==52
assert sum(len(g['items']) for g in groups)==343
ids=[]
for group in groups:
 assert group['category'] in {'seasonal','lunch','dessert','drinks','wine','spirits'}
 assert (ROOT/'assets/originals'/group['source']).exists()
 for item in group['items']:
  assert item['name'] and item['source']
  ids.append(item['id'])
assert len(ids)==len(set(ids))
print('PASS: 52 groups, 343 source-mapped entries, six sections, unique item IDs.')
