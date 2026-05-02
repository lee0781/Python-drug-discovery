import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)

#1. Data:
concentrations  = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
log_conc=np.log10(concentrations)

compounds={'Dox':np.array([98.2, 95.4, 87.3, 71.2, 48.6, 18.3,  4.2]),'TTP488':np.array([99.2, 97.8, 94.1, 83.4, 62.7, 38.2, 15.4]),'Combo':np.array([97.1, 91.3, 78.4, 54.2, 28.7,  9.1,  2.3])}
colors=['steelblue','darkorange','green']

#2. Masking:
print('===Section2: Boolean Masking===')
for name, viability in compounds.items():
    mask=viability<30
    flagged=np.sum(mask)
    print(f"{name}:{flagged} concentrations below 30% viability")

#3. IC50:
print("\n=== Section 3: IC50 Calculation ===")
ic50_results=[] 

for name,viability in compounds.items():
    viab_flip=viability[::-1]
    log_flip=log_conc[::-1]
    log_ic50=np.interp(50,viab_flip,log_flip)
    ic50=10**log_ic50
    ic50_results.append((name,ic50))
    print(f"{name}: IC50 = {ic50:.2f} nM")

#4. Ranking:
print("\n=== Section 4: Ranked by Potency ===")
ic50_results.sort(key=lambda x:x[1])

print(f"{'Rank':<6} {'Compound':<20} {'IC50 (nM)':>10}")
print("-" * 38)
for rank,(name,ic50) in enumerate (ic50_results,start=1):
      print(f"{rank:<6} {name:<20} {ic50:>9.2f}")

#5. Plotting
plt.figure(figsize=(9,6))
for (name,viability),color in zip(compounds.items(),colors):
     viab_flip = viability[::-1]
     log_flip  = log_conc[::-1]
     log_ic50  = np.interp(50, viab_flip, log_flip)
     ic50      = 10 ** log_ic50
     plt.plot(log_conc, viability, 'o-', color=color,
             linewidth=2, markersize=7,
             label=f'{name} (IC50={ic50:.1f} nM)')

plt.axhline(y=50, color='red', linestyle='--', alpha=0.5)
plt.xlabel('Log10 Concentration (nM)', fontsize=12)
plt.ylabel('Cell Viability (%)', fontsize=12)
plt.title('Combination Screen — 4T1 TNBC Cells', fontsize=14)
plt.legend(fontsize=9)
plt.grid(True, alpha=0.3)
plt.ylim(0, 110)
plt.tight_layout()
plt.savefig('week2_project.png', dpi=150)
plt.show()

#6. summary
print("\n=== Section 6: Summary ===")

most_potent_name, most_potent_ic50 = ic50_results[0]
least_potent_name, least_potent_ic50 = ic50_results[-1]
fold = least_potent_ic50 / most_potent_ic50

print(f"Most potent compound: {most_potent_name}")
print(f"IC50: {most_potent_ic50:.2f} nM")
print(f"Fold benefit over {least_potent_name}: {fold:.1f}x")


