import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)

#1. Data
concentrations = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])  # nM
log_conc=np.log10(concentrations)
compounds={'Osimertinib':np.array([98.4, 95.1, 84.2, 62.3, 31.4, 11.2,  3.1]),'Navitoclax':np.array([99.2, 97.3, 93.4, 81.2, 58.7, 32.4, 14.2]),'Combo':np.array([97.8, 91.2, 76.3, 48.4, 19.7,  6.3,  1.8])}
colors=['steelblue', 'darkorange', 'green']

combo_matrix=np.array([[96, 89, 71, 52],[88, 76, 54, 33],[67, 51, 28, 14],[41, 27, 12,  5]],dtype=float)
dox_doses = np.array([0.1, 1.0, 10.0, 100.0])
nav_doses = np.array([0.1, 1.0, 10.0, 100.0])

#2. masking
for name,viability in compounds.items():
    mask=viability<20
    count=np.sum(mask)
    print(f"{name}:{count} wells below 20% viability")

#3. IC50
ic50_results=[]
for name,viability in compounds.items():
    viab_flip=viability[::-1]
    logc_flip=log_conc[::-1]
    log_ic50=np.interp(50,viab_flip,logc_flip)
    ic50=10**log_ic50
    ic50_results.append((name,ic50))
    print(f"{name}: IC50={ic50:.2f}nM")

#4.Ranking
print(f"{'Rank':<6} {'Compound':<20} {'IC50 (nM)':>10}")
print("-" * 40)
ic50_results.sort(key=lambda x: x[1])
for rank, (name,ic50) in enumerate(ic50_results,start=1):
    print(f"{rank:<6} {name:<20} {ic50:>9.2f}")

#5.CI
ic50_osi   = 4.84 
ic50_nav   = 14.38 
ic50_combo = 2.82 
dose_osi_combo=ic50_combo*0.5
dose_nav_combo=ic50_combo*0.5

CI=(dose_osi_combo/ic50_osi)+(dose_nav_combo/ic50_nav)
if CI < 0.3:
    label = "Strong Synergy"
elif CI < 0.7:
    label = "Synergy"
elif CI <= 1.1:
    label = "Additive"
else:
    label = "Antagonism"

print(f"CI={CI:.1f}→ {label}")

#6. plot
plt.figure(figsize=(9, 6))

for (name,viability),color in zip(compounds.items(),colors):
    viab_flip=viability[::-1]
    log_c_flip=log_conc[::-1]
    log_ic50=np.interp(50,viab_flip,logc_flip)
    ic50=10**log_ic50
    plt.plot(log_conc, viability, 'o-', color=color,
             linewidth=2, markersize=7,
             label=f'{name} (IC50={ic50:.1f} nM)')
    
plt.axhline(y=50, color='red', linestyle='--', alpha=0.5)
plt.xlabel('Log10 Concentration (nM)')
plt.ylabel('Cell Viability (%)')
plt.title('Drug screening-Osimertinib,Navitoclax,and Combo')
plt.legend(fontsize=9)
plt.grid(True, alpha=0.3)
plt.ylim(0, 110)
plt.tight_layout()
plt.savefig('combo_screen.png', dpi=150)

#heatmap:
plt.figure(figsize=(6, 5))
img = plt.imshow(combo_matrix, cmap='RdYlGn', 
                 aspect='auto', vmin=0, vmax=100)
plt.colorbar(img, label='Cell Viability (%)')
plt.xticks(range(4), [f'{d}nM' for d in nav_doses])
plt.yticks(range(4), [f'{d}nM' for d in dox_doses])

plt.xlabel('Navitoclax Concentration')
plt.ylabel('Osimertinib Concentration')
plt.title('Combination Viability Matrix')

for i in range(4):
    for j in range(4):
        plt.text(j, i, f'{combo_matrix[i,j]:.0f}%',
                 ha='center', va='center',
                 fontsize=10, fontweight='bold',
                 color='black')
 
plt.tight_layout()
plt.savefig('combo_heatmap.png', dpi=150)

plt.show()

#7.summary
print("\n===== ANALYSIS REPORT =====")
print(f"Osimertinib  IC50: {ic50_osi:.2f} nM")
print(f"Navitoclax   IC50: {ic50_nav:.2f} nM")
print(f"Combo        IC50: {ic50_combo:.2f} nM")
print(f"CI = {CI:.2f} → {label}")
print(f"Conclusion: Combining Osimertinib + Navitoclax shows {label} in A549 cells")
print("===========================")
