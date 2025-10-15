#!/usr/bin/env python3
"""
Scan generated public/ HTML files and validate <script type="application/ld+json"> blocks are valid JSON.

Usage: python3 scripts/validate_jsonld.py
"""
import json
import re
from pathlib import Path

ROOT = Path('public')
pattern = re.compile(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S | re.I)

errors = []
count = 0

for p in ROOT.rglob('*.html'):
    txt = p.read_text(encoding='utf-8')
    for m in pattern.finditer(txt):
        count += 1
        blob = m.group(1).strip()
        try:
            json.loads(blob)
        except Exception as e:
            errors.append((str(p), str(e), blob[:200].replace('\n',' ')))

print(f'Found {count} JSON-LD blocks in public/')
if errors:
    print('\nErrors:')
    for f, err, snippet in errors:
        print(f'- {f}: {err}\n  snippet: {snippet}\n')
    raise SystemExit(2)
else:
    print('All JSON-LD blocks are valid JSON.')
    raise SystemExit(0)
