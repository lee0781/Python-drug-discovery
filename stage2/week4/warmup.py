import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)

ic50_results = [("Combo", 3.12), ("Dox", 9.24), ("TTP488", 29.41)]

ic50_results.sort(key=lambda x: x[1])
most_potent=ic50_results[0]
least_potent=ic50_results[-1]
fold=least_potent[1]/most_potent[1]

print(f"most potent:{most_potent}")
print(f"least potent:{least_potent}")
print(f"Fold:{fold}")

