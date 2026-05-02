import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)

concentrations = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
viability      = np.array([98.4, 95.2, 82.3, 54.7, 21.3, 6.2, 1.8])
log_conc       = np.log10(concentrations)

#1.ic50 estimate
viab_flip=viability[::-1]
logc_flip=log_conc[::-1]
log_ic50_interp=np.interp(50,viab_flip,logc_flip)
ic50_interp=10**log_ic50_interp
print(f"np.interp IC50:{ic50_interp:.2f}nM")

#2.curve fit ic50
def hill_equation(x,top,bottom,log_ic50,n):
    return top + (bottom - top) / (1 + 10**((log_ic50 - x) * n))

params,_=curve_fit(hill_equation,log_conc,viability,p0=[100,0,1,1],maxfev=10000)
top,bottom,log_ic50_fit,n=params
ic50_fit=10**log_ic50_fit

print(f"curve_fit IC50:  {ic50_fit:.2f} nM")
print(f"Difference:      {abs(ic50_interp - ic50_fit):.2f} nM")

#3.plot
x_smooth=np.linspace(-1,2,200)
y_fitted=hill_equation(x_smooth,top,bottom,log_ic50_fit,n)

plt.figure(figsize=(8, 5))
plt.scatter(log_conc, viability, color='steelblue', s=80, zorder=5, label='Data points')
plt.plot(x_smooth, y_fitted, color='steelblue', linewidth=2,
         label=f'Fitted curve (IC50={ic50_fit:.2f} nM)')
plt.axhline(y=50, color='red', linestyle='--', alpha=0.7, label='IC50 threshold')
plt.axvline(x=log_ic50_fit, color='green', linestyle='--', alpha=0.7)
plt.xlabel('Log10 Concentration (nM)', fontsize=12)
plt.ylabel('Cell Viability (%)', fontsize=12)
plt.title('Osimertinib — IC50 Comparison', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.ylim(-10, 115)
plt.tight_layout()
plt.savefig('w4mon_ic50_review.png', dpi=150)

gefitinib = np.array([99.1, 97.4, 91.2, 73.4, 48.2, 22.7, 8.4])

# fit curve_fit for gefitinib
params_gef, _ = curve_fit(hill_equation, log_conc, gefitinib,
                           p0=[100, 0, 1, 1], maxfev=10000)
top_g, bottom_g, log_ic50_gef, n_g = params_gef
ic50_gef = 10 ** log_ic50_gef

# smooth curve for gefitinib
y_fitted_gef = hill_equation(x_smooth, top_g, bottom_g, log_ic50_gef, n_g)

# add to existing plot BEFORE plt.show()
plt.scatter(log_conc, gefitinib, color='darkorange', s=80, zorder=5)
plt.plot(x_smooth, y_fitted_gef, color='darkorange', linewidth=2,
         label=f'Gefitinib (IC50={ic50_gef:.2f} nM)')
plt.show()