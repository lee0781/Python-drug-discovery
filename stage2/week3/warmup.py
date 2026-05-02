import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
np.set_printoptions(suppress=True)



plate=np.random.uniform(2,100,size=(3,3))
mean_plate=np.mean(plate,axis=1)
for i,mean in enumerate(mean_plate):
    print(f"Row{i}:{mean}")