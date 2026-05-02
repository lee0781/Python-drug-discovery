import numpy as np
np.set_printoptions(suppress=True)
import matplotlib.pyplot as plt

concentrations=np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
viability=np.array([98.2, 95.4, 87.3, 71.2, 48.6, 18.3, 4.2])
log_conc=np.log10(concentrations)

plt.figure(figsize=(8,5))
plt.plot(log_conc,viability,'o-',color='steelblue',linewidth=2,markersize=8,label='Doxorubicin')
plt.xlabel('Log10 Concentration (nM)',fontsize=12)
plt.ylabel('Cell Viability (%)',fontsize=12)
plt.title('Doxorubicin Dose-Response- TNBC Cells',fontsize=14)
plt.axhline(y=50,color='red',linestyle='--',alpha=0.7,label='IC50 threshold')
#mini challenge-add a second drug to the same plot
viability_drug2=np.array([99.1, 97.2, 91.4, 78.3, 61.2, 34.7, 12.1])
plt.plot(log_conc,viability_drug2,'s--',color='red',linewidth=2,markersize=8,label='Paclitaxel')



plt.legend(fontsize=10)
plt.grid(True,alpha=0.3)
plt.ylim(0,110)
plt.tight_layout()
plt.savefig('dose_response_plot.png',dpi=150)

plt.show()

