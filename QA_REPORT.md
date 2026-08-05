# Independent Final Validation — MILI Explorer Montréal Agglomeration Edition

## Result

**PASS — repository structure, data package and application logic validated for GitHub Pages deployment.**

## Data validation

- Unique physical assessment sites: **336,878**
- Municipalities represented: **16**
- Dynamic filter definitions: **45**
- Data chunks: **16**
- Duplicate site IDs: **0**
- Rows with invalid length: **0**
- Rows with missing/non-numeric coordinates: **0**
- Opportunity, constraint and confidence score ranges: **validated 0–100**

## Exact preset regression counts

- All: **336,878**
- Residential 1–2: **228,738**
- V1 Screen: **2,035**
- Premium: **15**

These are the exact expected counts for deployment testing.

## Functional logic validated

- Schema loading and chunk paths
- Dynamic numeric filters
- Dynamic category filters
- Dynamic boolean filters
- Dynamic text filters
- Municipality filtering
- Global text search fields
- Sorting by opportunity, constraint risk, lot area and Metro distance
- CSV export of every matching row
- Saved-property notes using browser localStorage
- 250-card and 3,000-marker display caps without limiting filtering or CSV export
- JavaScript syntax: **PASS**
- Required GitHub Pages files: **PASS**

## Coverage interpretation

The database includes the full Montréal agglomeration assessment geography represented as **unique physical sites**. Separate condominium assessment records that share the same physical geometry are consolidated into one physical-site record and flagged. Therefore, the application does not place one marker for every individual condominium unit.

## External dependency

The map interface loads Leaflet, MarkerCluster and OpenStreetMap tiles from public internet services. The property data itself is included in the repository.

## What this version can do

- Search the full 336,878-site Montréal agglomeration inventory
- Filter every numeric, category, boolean and text field exposed by the schema
- Search by address, matricule, municipality, use, housing area and street information
- Filter by municipality
- Filter residential, commercial, industrial, institutional, vacant and other uses
- Filter lot/building area, dwellings, year, storeys, coverage and open-site percentage
- Filter PUM planning, intensification and opportunity sectors
- Filter Metro/future-transit proximity
- Filter permits
- Filter heritage and wetland/flood indicators
- Filter corner and double-frontage screening indicators
- Rank, save and export results

## Limitations

It does not confirm legal zoning, ownership, assessment dollar values, taxes, legal cadastre, title, FAR, setbacks, height, subdivision rights or permitted unit yield.
