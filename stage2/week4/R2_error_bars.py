import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)

concentrations = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
log_conc       = np.log10(concentrations)

rep1 = np.array([98.2, 95.4, 87.3, 71.2, 48.6, 18.3, 4.2])
rep2 = rep1 + np.random.normal(0, 3, size=7)
rep3 = rep1 + np.random.normal(0, 3, size=7)

replicates     = np.vstack([rep1, rep2, rep3])
mean_viability = np.mean(replicates, axis=0)
std_viability  = np.std(replicates, axis=0, ddof=1)
sem_viability  = std_viability / np.sqrt(3)

#1. fit 
def hill_equation(x,top,bottom,log_ic50,n):
    return top + (bottom - top) / (1 + 10**((log_ic50 - x) * n))
params,_=curve_fit(hill_equation,log_conc,mean_viability,p0=[100, 0, 1, 1], maxfev=10000)
top,bottom,log_ic50,n=params
ic50=10**log_ic50

#R²
y_predicted=hill_equation(log_conc,top,bottom,log_ic50,n)
residuals=mean_viability-y_predicted
ss_res=np.sum(residuals**2)
ss_tot=np.sum((mean_viability-np.mean(mean_viability))**2)
r_squared=1-(ss_res/ss_tot)

print(f"IC50:      {ic50:.2f} nM")
print(f"R²:        {r_squared:.3f}")
print(f"Top:       {top:.1f}%")
print(f"Bottom:    {bottom:.1f}%")

#2. plot with error bars
x_smooth = np.linspace(-1, 2, 200)
y_fitted = hill_equation(x_smooth, top, bottom, log_ic50, n)

plt.figure(figsize=(8, 5))
plt.errorbar(log_conc, mean_viability,
             yerr=sem_viability,
             fmt='o', color='steelblue',
             ecolor='steelblue', elinewidth=1.5,
             capsize=4, markersize=7,
             label='Mean ± SEM (N=3)')
plt.plot(x_smooth, y_fitted, color='steelblue', linewidth=2,
         label=f'Fit (IC50={ic50:.2f} nM, R²={r_squared:.3f})')
plt.axhline(y=50, color='red', linestyle='--', alpha=0.7)
plt.xlabel('Log10 Concentration (nM)', fontsize=12)
plt.ylabel('Cell Viability (%)', fontsize=12)
plt.title('Doxorubicin — Fitted Curve with Error Bars', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.ylim(-10, 115)
plt.tight_layout()
plt.savefig('w4tue_errorbars.png', dpi=150)
plt.show()