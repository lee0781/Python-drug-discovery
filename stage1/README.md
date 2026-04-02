# Stage 1 — NumPy Fundamentals: TNBC Combination Drug Screen

Simulates a cell viability assay plate for triple-negative breast cancer (TNBC) cells treated with a chemotherapy + RAGE inhibitor combination. Models a realistic 4x6 plate reader output and performs standard HTS analysis using NumPy.

## What it does

1. **Plate simulation** — generates a 4x6 well plate with biologically realistic viability distributions per treatment group
2. **Plate QC** — calculates DMSO control CV% and flags pass/fail
3. **Per-treatment analysis** — computes row means and classifies each condition (NEG CTRL / MOD HIT / HIT)
4. **Hit identification** — applies Boolean masking to flag wells below 50% viability

## Treatments modeled

| Row | Treatment | Expected Viability |
|-----|-----------|-------------------|
| A | DMSO control | ~97.5% |
| B | Chemo alone | ~68% |
| C | Chemo + RAGE Inhibitor (low) | ~44% |
| D | Chemo + RAGE Inhibitor (high) | ~22% |

## Output

```
[[100.   98.6  97.2  97.3  98.9  99.2]
 [ 54.4  61.1  70.4  68.5  73.5  76.4]
 [ 33.9  42.1  52.   49.8  41.2  42.3]
 [ 25.9  18.9  22.9  27.8  15.9  15.9]]
Plate mean viability:57.7%
Plate standard deviation:29.8%
Plate shape: (4, 6)
Total wells:24

----QC Control----
DMSO mean:98.5
DMSO std:1.1
DMSO CV%:1.1%
Status:Pass (CV%=1.13%)
A   DMSO ctrl                   98.5%            NEG CTRL
B   Chemo alone                 67.4%                 ---
C   Chemo + RAGE Inhib low      43.6%             MOD HIT
D   Chemo + RAGE Inhib high     21.2%                 HIT

---HIT IDENTIFICATION---
Total hit wells:11
Hit rate:45.8%

Hits per treatment row
A — DMSO ctrl: 0/6 wells
B — Chemo alone: 0/6 wells
C — Chemo + RAGE Inhib low: 5/6 wells
D — Chemo + RAGE Inhib high: 6/6 wells

-------QC Summary---
Control QC:Pass
Hits identified:11
Total wells:24
Plate mean:57.7
```

