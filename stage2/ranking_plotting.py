import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

concentrations = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
log_conc       = np.log10(concentrations)

#Day 4A:
compounds = {'Doxorubicin':  np.array([98.2, 95.4, 87.3, 71.2, 48.6, 18.3,  4.2]),'TTP488':       np.array([99.2, 97.8, 94.1, 83.4, 62.7, 38.2, 15.4]),'Dox + TTP488': np.array([97.1, 91.3, 78.4, 54.2, 28.7,  9.1,  2.3]),}
colors=['steelblue','darkorange','green']

ic50_results=[]

for name,viability in compounds.items():
    viab_flip=viability[::-1]
    log_flip=log_conc[::-1]
    log_ic50=np.interp(50,viab_flip,log_flip)
    ic50=10**log_ic50
    ic50_results.append((name,ic50))

#sorting
ic50_results.sort(key=lambda x:x[1])

#ranking
print(f"{'Rank':<6} {'Compound':<20} {'IC50 (nM)':>10}")
print('='*40)
for rank,(name,ic50) in enumerate(ic50_results,start=1):
    print(f"{rank:<6} {name:<20} {ic50:>9.2f}")

#plotting
plt.figure(figsize=(9,6))

for (name,viability),color in zip(compounds.items(),colors):
    viab_flip = viability[::-1]
    log_flip  = log_conc[::-1]
    log_ic50  = np.interp(50, viab_flip, log_flip)
    ic50      = 10 ** log_ic50
    plt.plot(log_conc,viability,'o-',color=color,linewidth=2,markersize=7,label=f"{name}(IC50={ic50:.1f}nM)")

plt.axhline(y=50,color='red',linestyle='--',alpha=0.5)
plt.xlabel('Log10 Concentration (nM)')
plt.ylabel('Viability(%)')
plt.title('Combination Screen — Dox + RAGE Inhibition')
plt.legend(fontsize=9)
plt.grid(True, alpha=0.3)
plt.ylim(0, 110)
plt.tight_layout()
plt.savefig('compound_screen.png', dpi=150)
plt.show()