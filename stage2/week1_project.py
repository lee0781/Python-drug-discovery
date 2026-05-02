import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)

#1. DATA:Define concentrations + viability arrays, log-transform

concentrations=np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
viability=np.array([98.2, 95.4, 87.3, 71.2, 48.6, 18.3, 4.2])

log_conc=np.log10(concentrations)

#2.Approx IC50
diff_from_50=np.abs(viability-50)
IC50_index=np.argmin(diff_from_50)


print(f"Approx IC50:{concentrations[IC50_index]:.1f}nM")
print(f"Viability at IC50:{viability[IC50_index]:.1f}%")

#3. Plot
plt.figure(figsize=(8,5))
plt.plot(log_conc,viability,'o-',color='green',markersize=7,linewidth=2,label='Dox')
plt.axhline(y=50,color='red',linestyle='--',alpha=0.3,label='ic50 threshold')
plt.xlabel('Log Concentration (nM)',fontsize=12)
plt.ylabel('Cell Viability (%)',fontsize=12)
plt.title('Dox treatment on Cell',fontsize=14)
plt.legend(fontsize=9)
plt.ylim(0,110)
plt.tight_layout()
plt.savefig('practice plot.png',dpi=150)
plt.show()

#4.summary
print("="*40)
print("ANalysis Complete")
print("="*40)
IC50=concentrations[IC50_index]
Viability_at_IC50=viability[IC50_index]
Viability_high=np.max(viability)
Viability_low=np.min(viability)

print(f"IC50:{IC50:.1f}nM")
print(f"Viability at ic50:{Viability_at_IC50:.1f}%")
print(f"max viability:{Viability_high:.1f}%")
print(f"min viability:{Viability_low:.1f}%")

