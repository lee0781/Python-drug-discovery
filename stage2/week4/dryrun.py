import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)
#1. data 
concentrations = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])  # µM
np.random.seed(2024)

log_conc=np.log10(concentrations)

compounds = {
    'Venetoclax':         np.array([98.7, 96.2, 88.4, 71.3, 44.8, 19.2, 5.7]),
    'Navitoclax':         np.array([99.1, 97.4, 92.3, 79.8, 58.2, 33.7, 14.1]),
    'Ven + Navi':         np.array([97.8, 92.1, 79.4, 57.3, 28.4,  9.8,  2.4]),
}
colors = ['steelblue', 'darkorange', 'green']

combo_matrix = np.array([
    [97, 91, 74, 53],
    [89, 78, 59, 37],
    [68, 54, 33, 17],
    [44, 29, 14,  6],
], dtype=float)

#2. masking
for name, variability in compounds.items():
    mask=variability<25
    count=np.sum(mask)
    print(f"{name}:{count} wells below 25% viability")

#3. IC50 estimate
ic50_results=[]
for name,viability in compounds.items():
    viab_flip=viability[::-1]
    log_flip=log_conc[::-1]
    logic50=np.interp(50,viab_flip,log_flip)
    ic50=10**logic50
    ic50_results.append((name,ic50))
    print(f"{name}: IC50={ic50:.2f}uM")

#4. IC50(fitted)
def hill_equation (x,top,bottom,logic50,n):
    return top + (bottom - top) / (1 + 10**((logic50 - x) * n))
for name, viability in compounds.items():
    params,_=curve_fit(hill_equation,log_conc,viability,p0=[100,0,1,1],maxfev=1000)
    top,bottom,logic50_fit,n=params
    ic50_fitted=10**logic50_fit
    print(f"IC50(fitted){name}:{ic50_fitted:.2f}uM")

    viability_predicted=hill_equation(log_conc,top,bottom,logic50_fit,n)
    ss_res=np.sum((viability-viability_predicted)**2)
    ss_tot=np.sum((viability-np.mean(viability))**2)
    r2=1-(ss_res/ss_tot)
    print(f"R2={r2:.4f}")

#5. error bars

for name,viability in compounds.items():
    rep1=  viability
    rep2=rep1+ np.random.normal(0,3,size=7)
    rep3=rep1+ np.random.normal(0,3,size=7)

    replications=np.vstack([rep1,rep2,rep3])
    mean_viability=np.mean(replications,axis=0)
    std_viability=np.std(replications,ddof=1,axis=0)
    sem_viability=std_viability/np.sqrt(3)
    print(f"{name}: SEM={sem_viability.mean():.2f}")


#6. Ranking
ic50_results.sort(key=lambda x: x[1])

print(f"\n{'Rank':<6}{'Compound':<20}{'IC50 (µM)'}")

for rank,(name,ic50) in enumerate (ic50_results,start=1):
    print(f"{rank:<6}{name:<20}{ic50:.2f}")

#7. CI calculation
ic50_ven=7.9
ic50_nav=14.44
ic50_combo=4.07
dose_ven=ic50_combo*0.5
dose_nav=ic50_combo*0.5   

CI=(dose_ven/ic50_ven)+(dose_nav/ic50_nav)

print(f"CI={CI:.2f}uM")
if CI<1:
    print('Synergy')
elif CI==1:
    print('Additive')
elif CI>1:
    print('antagonism')
else:
    print('--')


#8.Heatmap
ven_doses  = [0.1, 1.0, 10.0, 100.0]  
navi_doses = [0.1, 1.0, 10.0, 100.0]  

plt.figure(figsize=(7, 6))
img = plt.imshow(combo_matrix, cmap='RdYlGn',
                 aspect='auto', vmin=0, vmax=100)
plt.colorbar(img, label='Cell Viability (%)')

for i in range(4):
    for j in range(4):
        plt.text(j, i, f'{combo_matrix[i,j]:.0f}%',
                 ha='center', va='center',
                 fontsize=10, fontweight='bold')

plt.xticks(range(4), [f'{d} nM' for d in ven_doses])
plt.yticks(range(4), [f'{d} nM' for d in navi_doses])
plt.xlabel('Venetoclax Concentration', fontsize=12)
plt.ylabel('Navitoclax Concentration', fontsize=12)
plt.title(f'Combo Matrix — CI={CI:.3f} (Strong Synergy)', fontsize=13)
plt.tight_layout()
plt.savefig('w4wed_ci_heatmap.png', dpi=150)
plt.show()