import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)

#1. data 
concentrations = np.array([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0])  # nM
log_conc=np.log10(concentrations)

compounds={'Osimertinib':np.array([98.4, 95.2, 82.3, 54.7, 21.3, 6.2, 1.8]),'Gefitinib':np.array([99.1, 97.4, 91.2, 73.4, 48.2, 22.7, 8.4])}

#2. IC50
ic50_results=[]
for name,viability in compounds.items():
    viab_flip=viability[::-1]
    log_c_flip=log_conc[::-1]
    log_ic50=np.interp(50,viab_flip,log_c_flip)
    ic50=10**log_ic50
    ic50_results.append((name,ic50))
    print(f"{name}: IC50={ic50:.2f}nM")

#3.Ranking
print(f"{'Rank':<6} {'Compound':<20} {'IC50 (nM)':>10}")
print("-" * 40)
ic50_results.sort(key=lambda x: x[1])
for rank, (name,ic50) in enumerate(ic50_results,start=1):
    print(f"{rank:<6} {name:<20} {ic50:>9.2f}")

#4.Plot
colors = ['steelblue', 'darkorange', 'green']
plt.figure(figsize=(9, 6))

for (name,viability),color in zip(compounds.items(),colors):
    viab_flip=viability[::-1]
    log_c_flip=log_conc[::-1]
    log_ic50=np.interp(50,viab_flip,log_c_flip)
    ic50=10**log_ic50
    plt.plot(log_conc, viability, 'o-', color=color,
             linewidth=2, markersize=7,
             label=f'{name} (IC50={ic50:.1f} nM)')
    
plt.axhline(y=50, color='red', linestyle='--', alpha=0.5)
plt.xlabel('Log10 Concentration (nM)')
plt.ylabel('Cell Viability (%)')
plt.title('Drug screening-Osimertinib and Gefitinib')
plt.legend(fontsize=9)
plt.grid(True, alpha=0.3)
plt.ylim(0, 110)
plt.tight_layout()
plt.savefig('compound_screen.png', dpi=150)
plt.show()

#5. CI
ic50_osi=1.38
ic50_gef=8.48

combo_fraction=0.3

dose_osi_combo=ic50_osi*combo_fraction*0.5
dose_gef_combo=ic50_gef*combo_fraction*0.5

CI=(dose_osi_combo/ic50_osi)+(dose_gef_combo/ic50_gef)

if CI < 0.3:
    label = "Strong Synergy"
elif CI < 0.7:
    label = "Synergy"
elif CI <= 1.1:
    label = "Additive"
else:
    label = "Antagonism"

print(f"CI={CI:.1f}→ {label}")