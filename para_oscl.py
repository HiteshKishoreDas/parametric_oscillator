#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:53:16 2020

@author: hitesh
"""
import numpy as np
from matplotlib import pyplot as plt

# Parameters
g0 = 9.8            # Background value of g
d_pivot = 0.1       # Amplitude of displacement of pivot
wg = 6.0           # Angular frequency of g
phi_g = 0.          # Initial phase of oscln in g 

l = 1.              # Length
r = 0.05            # Radius of bob
eta = 1.85e-5       # Viscosity of air
beta = 1000.*6*np.pi*eta*r          # Coefficient for drag

print(np.sqrt(g0/l),wg)

def g (t): # Function for variation of g
    return g0 + wg**2*d_pivot*np.cos(wg*t+phi_g)

def f (u,t): # RHS of time-derivative equations
    x = u[0]
    y = u[1]
    f_y = -g(t)*np.sin(x)/l - beta*y
    f_x = y 
    return np.array([f_x,f_y])

def leapfrog (f,a,b,h,x0): # Leapfrog method
    t_arr = np.arange(a,b,h)
    x = np.copy(x0)
    x_arr = np.zeros((np.size(t_arr),np.size(x0)),dtype=float)
    
    x_mid = x + h*f(x,t_arr[0])/2
        
    for i in range(np.size(t_arr)):
        t = t_arr[i]
        x_arr[i,:] = x
        
        k1 = h*f(x_mid, t + 0.5*h)
        x += k1
        k2 = h*f(x, t + h)
        x_mid += k2
        
    return x_arr, t_arr

a = 0.0         # Starting time
b = 50.        # Ending time
N = 100000      # Number of points
h_t = (b-a)/N   # Distance between points

th0 = np.pi/400   # Initial angular position
thdot0 = 0.     # Initial angular velocity

x0 = np.array([th0,thdot0])     # Initial condition

x_arr,t_arr = leapfrog(f,a,b,h_t,x0)
x_arr = np.array(x_arr)

fig = plt.figure(figsize=(10,10))  # Angular position plot
ax = fig.add_subplot(111, polar=True)
plt.polar(x_arr[:,0],t_arr)
ax.set_theta_zero_location('S')
ax.grid(False)
plt.xlabel('r = t (in s)',fontsize=20)
plt.title(r'$\omega$ = ' + str(wg)+'| Drag Coeff ='+str(np.round(beta,5)),fontsize=25)
plt.savefig('Ang_posn_'+str(wg)+'_drg_'+str(np.round(beta,5))+'.png')