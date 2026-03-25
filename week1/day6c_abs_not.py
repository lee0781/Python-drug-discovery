import numpy as np
deviations=np.array([-2.8,0.4,1.2,-3.1,0.9,-0.3,2.1,-1.7])
print("Deviations")
print(deviations)
abs_deviations=np.abs(deviations)
print("\nAbsolute deviations:")
print(abs_deviations)

outlier_mask=np.abs(deviations)>2.5
print("\nOutlier mask (|deviation|>2.5):")
print(outlier_mask)

outlier_wells=deviations[outlier_mask]
print("Outliers values:",outlier_wells)

clean_mask=~outlier_mask
print("\nclean mask (~outlier_mask):")
print(clean_mask)

clean_wells=deviations[clean_mask]
print("clean values (outliers removed):",clean_wells)

print(f"\ntotal wells: {deviations.size}")
print(f"outliers: {np.sum(outlier_mask)}")
print(f"clean wells: {np.sum(clean_mask)}")