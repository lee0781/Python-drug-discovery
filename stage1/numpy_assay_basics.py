#Basic NumPy Assay
#TNBC combination drug screen: cell viability analysis
#scenario: TNBC cells treated with chemotherapy + RAGE inhibitor/ cell viability measured

import numpy as np
np.set_printoptions(suppress=True)
np.random.seed(2024)
ROW_LABELS = ['A', 'B', 'C', 'D']
treatments = ['DMSO ctrl',
              'Chemo alone',
              'Chemo + RAGE Inhib low',
              'Chemo + RAGE Inhib high']



#1. Plate Building

DMSO_rows=np.random.normal(97.5,1.5,size=(1,6))
Chemo_rows=np.random.normal(68.0,5.2,size=(1,6))
Combo_rows_low=np.random.normal(44.0,6.7,size=(1,6))
Combo_rows_high=np.random.normal(22.0,4.1,size=(1,6))

plate=np.vstack([DMSO_rows,Chemo_rows,Combo_rows_low,Combo_rows_high])
plate=np.clip(plate,0,105)
print(np.round(plate,1))

#2. Plate Summary
print(f"Plate mean viability:{np.mean(plate):.1f}%")
print(f"Plate standard deviation:{np.std(plate,ddof=1):.1f}%")
print("Plate shape:",plate.shape)
print(f"Total wells:{plate.size}")

#3. Control QC
print("\n----QC Control----")
DMSO_mean=np.mean(plate[0,:])
DMSO_std=np.std(plate[0,:],ddof=1)
DMSO_cv=(DMSO_std/DMSO_mean)*100
print(f"DMSO mean:{DMSO_mean:.1f}")
print(f"DMSO std:{DMSO_std:.1f}")
print(f"DMSO CV%:{DMSO_cv:.1f}%")

if DMSO_cv<10:
    print(f"Status:Pass (CV%={DMSO_cv:.2f}%)")
else:
    print("Fail")

#4. Per-treatment analysis
row_mean=np.mean(plate,axis=1)
for i in range(4):
    mean_val=row_mean[i]
    if mean_val>85:
        flag="NEG CTRL"
    elif mean_val<35:
        flag="HIT"
    elif mean_val<55:
        flag="MOD HIT"
    else:
        flag="---"
    print(f"{ROW_LABELS[i]:<4}{treatments[i]:<22}{mean_val:>10.1f}%{flag:>20}")

#5. Hit ID
print("\n---HIT IDENTIFICATION---")
hit_mask=plate<50
hit_wells=plate[hit_mask]
hit_count=np.sum(hit_mask)
print(f"Total hit wells:{hit_count}")
print(f"Hit rate:{(hit_count/plate.size)*100:.1f}%")
print("\nHits per treatment row")
for i in range(4):
    row_hits=np.sum(plate[i,:]<50)
    print(f"{ROW_LABELS[i]} — {treatments[i]}: {row_hits}/6 wells")

#6. Summary
print("\n-------QC Summary---")
print(f"Control QC:{'Pass' if DMSO_cv<10 else 'Fail'}")
print(f"Hits identified:{hit_count}")
print(f"Total wells:{plate.size}")
print(f"Plate mean:{np.mean(plate):.1f}")
