#!/usr/bin/env python3
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
s=json.loads((root/'data/schema.json').read_text(encoding='utf-8'))
rows=[]
for c in s['chunks']:
    p=root/c['file']
    assert p.exists(), c['file']
    a=json.loads(p.read_text(encoding='utf-8'))
    assert len(a)==c['rows']
    rows.extend(a)
idx={f:i for i,f in enumerate(s['fields'])}
assert len(rows)==s['total_sites']==336878
assert len({r[idx['site_id']] for r in rows})==len(rows)
for p in ['index.html','assets/app.js','assets/styles.css','README.md','QA_REPORT.md']:
    assert (root/p).exists(), p
print(f"PASS: {len(rows):,} sites across {len(s['chunks'])} chunks")
