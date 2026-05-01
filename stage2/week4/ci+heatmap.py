import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)
#1.CI calculation

ic50_dox=9.24
ic50_ttp=29.41
ic50_combo=3.12

dose_dox=ic50_combo*0.5
dose_ttp=ic50_combo*0.5

CI=(dose_dox/ic50_dox)+(dose_ttp/ic50_ttp)

print(f"CI= {CI:.3f}")
if CI<0.3:
    print("Classification: STRONG SYNERGY")
elif CI < 0.7:
    print("Classification: SYNERGY")
elif CI <= 1.1:
    print("Classification: ADDITIVE")
else:
    print("Classification: ANTAGONISM")

#2. heatmap
combo_matrix = np.array([
    [95, 88, 62, 41],
    [87, 74, 48, 28],
    [61, 49, 22, 11],
    [38, 24,  8,  3],
], dtype=float)

dox_doses = [0.1, 1.0, 10.0, 100.0]
ttp_doses = [0.1, 1.0, 10.0, 100.0]

plt.figure(figsize=(7, 6))
img = plt.imshow(combo_matrix, cmap='RdYlGn',
                 aspect='auto', vmin=0, vmax=100)
plt.colorbar(img, label='Cell Viability (%)')

for i in range(4):
    for j in range(4):
        plt.text(j, i, f'{combo_matrix[i,j]:.0f}%',
                 ha='center', va='center',
        d         fontsize=10, fontweight='bold')

plt.xticks(range(4), [f'{d} nM' for d in ttp_doses])
plt.yticks(range(4), [f'{d} nM' for d in dox_doses])
plt.xlabel('TTP488 Concentration', fontsize=12)
plt.ylabel('Doxorubicin Concentration', fontsize=12)
plt.title(f'Combo Matrix — CI={CI:.3f} (Strong Synergy)', fontsize=13)
plt.tight_layout()
plt.savefig('w4wed_ci_heatmap.png', dpi=150)
plt.show()