# Stage 2 — Dose-Response Curves & Combination Analysis

Full dose-response pipeline analyzing an Osimertinib + Selumetinib
combination screen on an EGFR-sensitive lung cancer cell line.

## What it does
1. **Data setup** — 3 compounds with 3 simulated replicates per condition
2. **QC masking** — flags wells below 20% viability, reports flagged concentrations
3. **Quick IC50** — estimates IC50 for all 3 compounds using np.interp()
4. **Fitted IC50** — fits Hill equation via curve_fit(), calculates R² per compound
5. **Ranking** — sorts compounds by fitted IC50, prints ranked table
6. **Combination Index** — calculates CI, interprets synergy vs antagonism
7. **Dose-response plot** — all 3 fitted curves + error bars on one graph
8. **Heatmap** — combo dose matrix with RdYlGn colormap

## Compounds screened
| Compound | Target | Expected IC50 |
|---|---|---|
| Osimertinib | EGFR inhibitor (3rd gen) | ~2.53 µM |
| Selumetinib | MEK inhibitor | ~34.50 µM |
| Osi + Selu | EGFR + MEK combo | ~1.24 µM |

## Output
Fitted IC50 — Osimertinib: 2.53 µM | Selumetinib: 34.50 µM | Combo: 1.24 µM
CI = 0.26 → Synergy
Plots saved: dose_response_combo.png | project_ci_heatmap.png

## Data
Synthetic viability data — Osimertinib + Selumetinib EGFR inhibitor combo screen
Concentration range: 0.001–1000 µM
