# MILI Explorer – Montréal Agglomeration Edition

A fully static, free, GitHub Pages-ready property intelligence explorer covering the **entire Montréal agglomeration**.

## Coverage

- **336,878 unique physical assessment sites**
- Montréal plus all 15 reconstituted municipalities in the agglomeration
- No property-use prefilter: residential, commercial, industrial, institutional, vacant and other uses are included
- Condominium assessment records sharing one physical geometry are consolidated into one physical site and flagged

## Municipalities

- Baie-D'Urfé
- Beaconsfield
- Côte-Saint-Luc
- Dollard-des-Ormeaux
- Dorval
- Hampstead
- L'Île-Dorval
- Kirkland
- Mont-Royal
- Montréal-Est
- Montréal-Ouest
- Pointe-Claire
- Sainte-Anne-de-Bellevue
- Senneville
- Westmount
- Montréal

## Capabilities

- Search by address, matricule, municipality, use, housing area and street information
- Dynamic filters generated from `data/schema.json`
- Municipality filter with readable names
- Numeric, category, boolean and text filters
- Map clustering and ranked result cards
- Property detail view containing every imported field
- Opportunity, constraint-risk and data-confidence scores
- Saved properties and browser-local notes
- CSV export of every match
- Presets: All, Residential 1–2, V1 Screen and Premium

## Search and display limits

The filter engine evaluates all **336,878 sites**. For browser performance, it displays up to 250 cards and 3,000 map markers. CSV export contains all matching rows.

## Deployment

1. Create a public GitHub repository.
2. Upload all files while preserving their paths.
3. In **Settings → Pages**, choose **Deploy from a branch**, `main`, `/ (root)`.
4. The expected loaded count is **336,878**.

## Important limitations

This is a preliminary screening tool. It does not confirm legal zoning, ownership, title, tax assessment values, legal lot boundaries, FAR, height, setbacks, subdivision rights or permitted unit count.
