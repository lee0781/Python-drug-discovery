import numpy as np
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)

concentrations = np.array([0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0])
viability      = np.array([98.2, 95.4, 87.3, 71.2, 48.6, 18.3, 4.2])
log_conc=np.log10(concentrations)

def hill_equation(x,top,bottom,log_ic50,n):
    return top+(bottom-top)/(1+10**((log_ic50-x)*n))

params,_=curve_fit(hill_equation,log_conc,viability,p0=[100,0,1,1],maxfev=10000)
top,bottom,log_ic50,n=params

#calculaate R^2
y_predicted=hill_equation(log_conc,top,bottom,log_ic50,n)
residuals=viability-y_predicted

ss_res=np.sum(residuals**2)
ss_tot=np.sum((viability-np.mean(viability))**2)
r_squared=1-(ss_res/ss_tot)

print(f"R^2={r_squared:.3f}")
print(f"IC50={10**log_ic50:2f}nM")
if r_squared >=0.95:
    print("Fit quality:Excellent")
elif r_squared>=0.80:
    print("Fit quality: Acceptable")
else:
    print("Fit quality:Poor-check data")