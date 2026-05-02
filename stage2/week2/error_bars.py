import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)
np.random.seed(42)

concentrations = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
log_conc       = np.log10(concentrations)

rep1=np.array([98.2, 95.4, 87.3, 71.2, 48.6, 18.3, 4.2])
rep2=rep1+np.random.normal(0,3,size=7)
rep3=rep1+np.random.normal(0,3,size=7) #0=mean 3=SD

replicates=np.vstack([rep1,rep2,rep3])
mean_variability=np.mean(replicates,axis=0)

std_variability=np.std(replicates,axis=0,ddof=1)
sem_variability=std_variability/np.sqrt(3)

#fit the curve
def hill_equation(x,top,bottom,log_ic50,n):
    return top + (bottom - top) / (1 + 10**((log_ic50 - x) * n))
params,_=curve_fit(hill_equation,log_conc,mean_variability,p0=[100,0,1,1],maxfev=10000)

top,bottom,log_ic50,n=params
ic50=10**log_ic50

#plot with error bars
x_smooth=np.linspace(-1,2,200)
y_fitted=hill_equation(x_smooth,top,bottom,log_ic50,n)

plt.figure(figsize=(8,5))
plt.errorbar(log_conc,mean_variability,yerr=sem_variability,fmt='o',color='steelblue',ecolor='steelblue',elinewidth=1.5,capsize=4,markersize=7,label='Mean ± SEM (N=3)')
plt.plot(x_smooth, y_fitted, color='steelblue',
         linewidth=2, label=f'Fit (IC50={ic50:.1f} nM)')

plt.axhline(y=50, color='red', linestyle='--', alpha=0.7)
plt.xlabel('Log10 Concentration (nM)', fontsize=12)
plt.ylabel('Cell Viability (%)', fontsize=12)
plt.title('Doxorubicin — Dose-Response with Error Bars', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.ylim(-10, 115)
plt.tight_layout()
plt.savefig('error_bars_plot.png', dpi=150)
plt.show()

print(f"IC50={ic50:.2f}nM (N=3, ± SEM)")