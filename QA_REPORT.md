# MILI Explorer 2.1 — Final QA Report

**PASS — ready for GitHub Pages branch deployment.**

## Data validation

- 336,878 unique physical sites
- 16 Montréal-agglomeration municipalities
- 16 data chunks
- 45 dynamic filter definitions
- No duplicate site IDs
- All schema chunk paths present

## Version 2.1 search validation

- Partial address search: PASS
- Full mailing-address normalization: PASS
- Street-type and postal-code tolerance: PASS
- Accent and punctuation tolerance: PASS
- Minor street-name typo correction: PASS
- Ranked relevance: PASS
- Live autocomplete: PASS
- Search updates while typing: PASS

The query `5281 Chambord St. Montreal, QC H2J 3N4` is designed to find the physical assessment site stored as `5279–5281 rue Chambord (MTL)`.

## Functional validation

- JavaScript syntax: PASS
- Dynamic numeric/category/boolean/text filters: PASS
- Municipality filter: PASS
- Sorting: PASS
- Map clustering: PASS
- Property details: PASS
- Saved properties and notes: PASS
- CSV export: PASS

## Regression counts

- All: 336,878
- Residential 1–2: 228,738
- V1 Screen: 2,035
- Premium: 15
