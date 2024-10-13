import numpy as np

# cross-sectional area
L = 3.09
Lerr = 0.02
W = 0.92
Werr = 0.02

A = L * W
Aerr = np.sqrt((W * Lerr)**2 + (L * Werr)**2)
print(f"A = {A:.2f} ± {Aerr:.2f}")

# resistivity error, rho = VA/IL
V5err = 1e-6
V7err = 1e-6 
Ierr = 1e-3
