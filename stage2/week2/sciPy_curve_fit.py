import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)

#Step1: data
concentrations = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
viability      = np.array([98.2, 95.4, 87.3, 71.2, 48.6, 18.3, 4.2])
log_conc=np.log10(concentrations)

#2:def hill equation
def hill_equation(x,top,bottom,log_ic50,n):
    return top+(bottom-top)/(1+10**((log_ic50-x)*n))

#3:fit the curve
params,_=curve_fit(hill_equation,log_conc,viability,p0=[100,0,1,1],maxfev=10000)
top,bottom,log_ic50,n=params

ic50=10**log_ic50

print(f"IC50:{ic50:.2f}nM")
print(f"Top:{top:.1f}%")
print(f"Bottom:{bottom:.1f}%")
print(f"Slope:{n:.2f}")

#4:plot
x_smooth=np.linspace(-1,2,200) 
y_fitted=hill_equation(x_smooth,top,bottom,log_ic50,n)
plt.figure(figsize=(8,5))
plt.scatter(log_conc,viability,color='steelblue',s=50,zorder=5,label='Data points')

plt.plot(x_smooth,y_fitted,color='steelblue',linewidth=2,label=f"Fitted curve(IC50:{ic50:.1f}nM)")
plt.axhline(y=50,color='red',linestyle='--',alpha=0.7)
plt.axvline(x=log_ic50,color='green',linestyle='--',alpha=0.7,label=f"IC50:{ic50:.1f}nM")
plt.xlabel('Log10 Concentration(nM)',fontsize=12)
plt.ylabel('Cell Viability(%)',fontsize=12)
plt.title('Dox-Fitted Dose-Response Curve',fontsize=14)
plt.legend(fontsize=10)
plt.grid(True,alpha=0.3)
plt.ylim(-10,115)
plt.tight_layout()
plt.savefig('fitted_curve.png',dpi=150)
plt.show()