# dose_response_screen.py
# Stage 2 Portfolio Project :AstraZeneca EGFR Resistance Team
# Osimertinib + Selumetinib combo screen:EGFR-sensitive cell line (synthetic data)
# Author: Youngwon Lee | April 2026

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)

#1. Data setup
# Synthetic viability data — Osimertinib + Selumetinib EGFR inhibitor combo screen
# Concentration range: 0.001–1000 µM
# Viability curves model an EGFR-sensitive lung cancer cell line

concentrations = np.array([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0])  # µM
log_conc = np.log10(concentrations)
np.random.seed(2024)

compounds = {
    'Osimertinib': np.array([98.4, 95.1, 84.2, 62.3, 31.4, 11.2,  3.1]),
    'Selumetinib': np.array([99.2, 97.8, 93.4, 81.3, 61.2, 38.4, 17.3]),
    'Osi + Selu':  np.array([97.9, 92.4, 78.3, 53.2, 22.8,  7.4,  1.9]),
}
colors = ['steelblue', 'darkorange', 'green']

combo_matrix = np.array([
    [97, 90, 73, 51],
    [88, 77, 57, 34],
    [66, 52, 31, 16],
    [42, 28, 13,  5],
], dtype=float)
osi_doses  = [0.001, 0.01, 0.1, 1.0]
selu_doses = [0.001, 0.01, 0.1, 1.0]

#── 3 REPLICATES PER COMPOUND ─────────────────────────────────────
replicates = {}
for name, viability in compounds.items():
    rep1 = viability
    rep2 = viability + np.random.normal(0, 3, size=7)
    rep3 = viability + np.random.normal(0, 3, size=7)
    replicates[name] = np.vstack([rep1, rep2, rep3])


#2. QC Maksing
print("\n── QC Masking ──")
for name, viability in compounds.items():
    mask=viability<20
    count=np.sum(mask)
    print(f"{name}: {count} wells below 20% viability")
    if count>0:
        print(f"→ flagged at:{concentrations[mask]}uM ")

#3. Quick IC50
print("\n──Quick IC50 (np.interp) ──")
ic50_interp=[]
for name, viability in compounds.items():
    viability_flip=viability[::-1]
    log_conc_flip=log_conc[::-1]
    log_ic50=np.interp(50,viability_flip,log_conc_flip)
    ic50=10**log_ic50
    ic50_interp.append((name,ic50))
    print(f"{name}: IC50={ic50:.2f} µM")

#4. Fitted IC50
print("\n──Fitted IC50 (curve_fit) & R²──")
ic50_fitted=[]
r2_results={}
def hill_equation(x,top,bottom,log_ic50,n):
    return top + (bottom - top) / (1 + 10**((log_ic50 - x) * n))
for name, viability in compounds.items():
    params,_=curve_fit(hill_equation,log_conc,viability,p0=[100,0,1,1],maxfev=10000)
    top,bottom,log_ic50_fit,n=params
    ic50_fit=10**log_ic50_fit
    ic50_fitted.append((name,ic50_fit))
   

    viability_predicted=hill_equation(log_conc,top,bottom,log_ic50_fit,n)
    ss_res=np.sum((viability-viability_predicted)**2)
    ss_tot=np.sum((viability-np.mean(viability))**2)
    r2=1-(ss_res/ss_tot)
    print(f"  {name}: IC50={ic50_fit:.2f} µM | R²={r2:.4f}")
    r2_results[name]=r2

#5. Ranking
print("\n──Ranking──")

ic50_fitted.sort(key=lambda x: x[1])
print(f"{'Rank':<6}{'Compound':<20}{'IC50'}")
print("-"*40)
for rank,(name,ic50_fit) in enumerate(ic50_fitted,start=1):
     print(f"{rank:<6}{name:<20}{ic50_fit:.2f} µM")

#6.CI calculation
print("\n──Combination Index──")

ic50_dict  = dict(ic50_fitted)
ic50_osi   = ic50_dict['Osimertinib']
ic50_selu  = ic50_dict['Selumetinib']
ic50_combo = ic50_dict['Osi + Selu']
doses_osi=ic50_combo*0.5
doses_selu=ic50_combo*0.5

CI=(doses_osi/ic50_osi)+(doses_selu/ic50_selu)

if CI<1:
    flag='Synergy'
elif CI==1:
    flag='Additive'
elif CI>1:
    flag='Antagonism'
print(f"CI={CI:.2f}: {flag}")

#7. Plotting
print("\n──Dose Response Plot──")

x_smooth=np.linspace(-3,3,300)

plt.figure(figsize=(9, 6))

for (name,viability),color in zip(compounds.items(),colors):
    viability=compounds[name]

    params, _ = curve_fit(hill_equation, log_conc, viability,p0=[100, 0, 1, 1], maxfev=10000)
    top, bottom, log_ic50_fit, n = params
    ic50_fit = 10**log_ic50_fit

    y_smooth=hill_equation(x_smooth,top,bottom,log_ic50_fit,n)
    plt.plot(x_smooth,y_smooth, color=color, linewidth=1,label=f'{name} (IC50={ic50_fit:.2f}µM)')

    rep_array = replicates[name]
    means= np.mean(rep_array, axis=0)
    sems= np.std(rep_array, ddof=1, axis=0) / np.sqrt(3)
    plt.errorbar(log_conc, means, yerr=sems, fmt='o',color=color, capsize=4, alpha=0.7)

plt.xlabel("log10 Concentration (µM)", fontsize=12)
plt.ylabel("Cell Viability (%)", fontsize=12)
plt.title("Osimertinib + Selumetinib Dose-Response\nEGFR-sensitive Cell Line", fontsize=13)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("dose_response_combo.png", dpi=150)
plt.show()



#8.Heatmap
print("\n──Heatmap──")

osi_doses  = [0.001, 0.01, 0.1, 1.0]
selu_doses = [0.001, 0.01, 0.1, 1.0]

plt.figure(figsize=(7, 6))
img = plt.imshow(combo_matrix, cmap='RdYlGn',aspect='auto', vmin=0, vmax=100)
plt.colorbar(img, label='Cell Viability (%)')

for i in range(4):
    for j in range(4):
        plt.text(j, i, f'{combo_matrix[i,j]:.0f}%',ha='center', va='center',fontsize=10, fontweight='bold')
plt.xticks(range(4), [f'{d} µM' for d in osi_doses])
plt.yticks(range(4), [f'{d} µM' for d in selu_doses])
plt.xlabel('Osimertinib Concentration', fontsize=12)
plt.ylabel('Selumetinib Concentration', fontsize=12)
plt.title(f'Combo Matrix — CI={CI:.3f} (Synergy)', fontsize=13)
plt.tight_layout()
plt.savefig('project_ci_heatmap.png', dpi=150)
plt.show()
