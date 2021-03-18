import numpy as np

# Parameters
g0 = 9.8            # Background value of g
d_pivot = 0.1       # Amplitude of displacement of pivot
wg = 6.0           # Angular frequency of g
phi_g = 0.          # Initial phase of oscln in g 

l = 1.              # Length
r = 0.05            # Radius of bob
eta = 1.85e-5       # Viscosity of air
beta = 1000.*6*np.pi*eta*r          # Coefficient for drag

a = 0.0         # Starting time
b = 1000.        # Ending time
N = 100000      # Number of points

th0 = np.pi/400   # Initial angular position
thdot0 = 0.     # Initial angular velocity