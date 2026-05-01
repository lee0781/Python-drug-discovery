import numpy as np
np.set_printoptions(suppress=True)

concentrations=np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
viability=np.array([98.2, 95.4, 87.3, 71.2, 48.6, 18.3, 4.2])
log_conc=np.log10(concentrations)

print("Concentrations(nM):",concentrations)
print("Log10 values:",np.round(log_conc,2))

diff_from_50=np.abs(viability-50)

ic50_index=np.argmin(diff_from_50)

print(f"Approx IC50:{concentrations[ic50_index]:.1f}nM")
print(f"Viability at Ic50:{viability[ic50_index]:.1f}%")