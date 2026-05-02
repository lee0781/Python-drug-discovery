import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

concentrations = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
viability      = np.array([98.2, 95.4, 87.3, 71.2, 48.6, 18.3, 4.2])
log_conc       = np.log10(concentrations)


#np.interp needs increasing y values
viability_flipped=viability[::-1]
log_conc_flipped=log_conc[::-1]

#np.interp
log_ic50=np.interp(50,viability_flipped,log_conc_flipped)

#convert log back to nM
ic50=10**log_ic50

print(f"IC50={ic50:.2f}nM")
print(f"Log IC50={log_ic50:.3f}")

#plot a graph
plt.figure(figsize=(8,5))
plt.plot(log_conc,viability,'o-',color='green',linewidth=2,markersize=8,label='Doxorubicin')
plt.axhline(y=50,color='red',linestyle='--',alpha=0.7,label='50% viability')
plt.axvline(x=log_ic50,color='blue',linestyle='--',alpha=0.7,label=f'IC50={ic50:.1f}nM')

plt.xlabel('Log10 Concentration (nM)')
plt.ylabel('Cell Viability (%)')
plt.title('IC50 Calculation-Doxorubicin/TNBC Cells')
plt.legend()
plt.grid(True,alpha=0.3)
plt.ylim(0,110)
plt.tight_layout()
plt.savefig('ic50_plot.png',dpi=150)
plt.show()
