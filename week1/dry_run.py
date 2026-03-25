import numpy as np
np.set_printoptions(suppress=True)
np.random.seed(2024)

#section1:build plate
DMSO_rows=np.random.uniform(92,100,size=(2,12))
treated_rows=np.random.uniform(10,75,size=(4,12))
Staur_rows=np.random.uniform(1,8,size=(2,12))

plate=np.vstack([DMSO_rows,treated_rows,Staur_rows])
plate=np.clip(plate,1,105)
print("\n---8*12 Plate---")
print(np.round(plate,1))

#section2:plate summary
print("total wells:",plate.size)
print(f"plate mean:{np.mean(plate):.1f}")
print(f"plate SD:{np.std(plate,ddof=1):.1f}")
print(f"plate dimensions:{plate.shape[0]}rows*{plate.shape[1]}columns")

#section3:control QC
DMSO_wells=plate[0:2,:]
dmso_mean=np.mean(DMSO_wells)
dmso_sd=np.std(DMSO_wells,ddof=1)
dmso_cv=(dmso_sd/dmso_mean)*100
print(f"DMSO mean:{dmso_mean:.1f}")
print(f"DMSO STD:{dmso_sd:.1f}")
print(f"DMSO CV%:{dmso_cv:.1f}%")
if dmso_cv<10:
    print("pass")
else:
    print("fail")
#section 4:row by row loop
print("\n---Section4---")
row_mean=np.mean(plate,axis=1)
for i in range(8):
    mean_val=row_mean[i]
    if mean_val>85:
        print("Pass")
    elif mean_val<30:
        print("Hit")
    else:
        print("---")

#section5:hit identification
print("\n---section 5---")
hit_mask=plate<30
hit_wells=plate[hit_mask]
hit_count=np.sum(hit_mask)
print(f"Total hit wells: {hit_count}")

#section6:Final summary
print("\n-------QC Summary---")
print(f"Control QC:{'Pass' if dmso_cv<10 else 'Fail'}")
print(f"Hits indentified:{hit_count}")
print(f"Total wells:{plate.size}")
print(f"Plate mean:{np.mean(plate):.1f}")

