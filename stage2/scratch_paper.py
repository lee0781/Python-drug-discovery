import numpy as np
np.random.seed(42)

viability = np.array([98.2, 95.4, 87.3, 71.2, 48.6, 18.3, 4.2])

diff_from_50=np.abs(viability-50)
approx_IC50=np.argmin(diff_from_50)
IC50_index=viability[approx_IC50]
print(IC50_index)

