#!/usr/bin/env python3
from pathlib import Path
import json, hashlib
root=Path(__file__).resolve().parents[1]
required=['index.html','assets/app.js','assets/styles.css','data/schema.json','.github/workflows/deploy.yml']
for f in required:
    if not (root/f).exists(): raise SystemExit('FAIL missing '+f)
s=json.loads((root/'data/schema.json').read_text(encoding='utf-8'))
fields=s['fields']; n=0; ids=set(); municipalities=set()
for c in s['chunks']:
    p=root/c['file']
    if not p.exists(): raise SystemExit('FAIL missing '+c['file'])
    rows=json.loads(p.read_text(encoding='utf-8'))
    if len(rows)!=c['rows']: raise SystemExit('FAIL row count '+c['file'])
    for r in rows:
        if len(r)!=len(fields): raise SystemExit('FAIL row width '+c['file'])
        d=dict(zip(fields,r)); sid=d['site_id']
        if sid in ids: raise SystemExit('FAIL duplicate '+str(sid))
        ids.add(sid); municipalities.add(d['municipality_name'])
        if not (-90<=float(d['latitude'])<=90 and -180<=float(d['longitude'])<=180): raise SystemExit('FAIL coordinates')
        for score in ['opportunity_score','constraint_risk','data_confidence']:
            if not 0<=float(d[score])<=100: raise SystemExit('FAIL score')
        n+=1
if n!=s['total_sites']: raise SystemExit(f'FAIL total {n}')
if len(municipalities)!=16: raise SystemExit(f'FAIL municipalities {len(municipalities)}')
print(f'PASS: {n:,} sites, {len(municipalities)} municipalities, {len(s["field_definitions"])} dynamic filters')
