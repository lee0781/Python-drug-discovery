import numpy as np

wells=np.array([98.2, 12.3, 110.5, 8.4, 45.2, 3.1, 95.7, 22.1, 88.3, 0.2, 67.4, 14.8])
print("All Wells:")
print(wells)

hit_mask=(wells<30)&(wells<105)
hit_wells=wells[hit_mask]
print("\nHits(<30% AND <105%):")
print(hit_wells)

extreme_mask=(wells>100)|(wells<5)
extreme_wells=wells[extreme_mask]
print("\nExtreme wells (>100% OR <5%):")
print(extreme_wells)

#combining three conditions
drug_mask=(wells>=10)&(wells<=80)
drug_wells=wells[drug_mask]
print("\nDrug range(10-80%)")
print(drug_wells)

#count results
print(f"\nTotal wells: {wells.size}")
print(f"Hits: {hit_wells.size}")
print(f"Extreme wells: {extreme_wells.size}")
print(f"Drug range: {drug_wells.size}")