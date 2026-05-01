import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)

#1. define ic50
ic50_dox   = 9.24    
ic50_ttp   = 29.41   
ic50_combo = 3.12 

print(f"Dox IC50:   {ic50_dox:.2f} nM")
print(f"TTP488 IC50: {ic50_ttp:.2f} nM")
print(f"Combo IC50:  {ic50_combo:.2f} nM")

#2. calculate CI
#assume combo ic50 is 50%dox and 50%ttp
dose_dox = ic50_combo * 0.5   # 1.56 nM of Dox in combo
dose_ttp = ic50_combo * 0.5   # 1.56 nM of TTP488 in combo

CI=(dose_dox/ic50_dox)+(dose_ttp/ic50_ttp)
print(f"CI Calculation:")
print(f"Dox fraction:{dose_dox/ic50_dox:.3f}")
print(f"TTP488 fraction:{dose_ttp/ic50_ttp:.3f}")
print(f"CI:{CI:.3f}")

#3. interpreting CI
print(f"Interpretarion:")
if CI<0.3:
    print(f"CI={CI:.3f}→ strong synergy")
elif CI<0.7:
     print(f"  CI = {CI:.3f} → SYNERGY")
elif CI < 0.9:
    print(f"  CI = {CI:.3f} → SLIGHT SYNERGY")
elif CI<=1.1:
    print(f"  CI = {CI:.3f} → ADDITIVE")
elif CI <= 1.45:
    print(f"  CI = {CI:.3f} → SLIGHT ANTAGONISM")
else:
    print(f"  CI = {CI:.3f} → ANTAGONISM")