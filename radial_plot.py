import numpy as np
from matplotlib import pyplot as plt
import para_oscl as po
from globals import *

dth0 = 0.1*th0

x_arr,t_arr = po.para_oscl(a,b,th0,thdot0,N)
x_arr2,t_arr2 = po.para_oscl(a,b,th0+dth0,thdot0,N)

fig = plt.figure(figsize=(10,10))  # Angular position plot
ax = fig.add_subplot(111, polar=True)
plt.polar(x_arr[:,0],t_arr)
ax.set_theta_zero_location('S')
ax.grid(False)
plt.xlabel('r = t (in s)',fontsize=20)
plt.title(r'$\omega$ = ' + str(wg)+'| Drag Coeff ='+str(np.round(beta,5)),fontsize=25)
# plt.savefig('Ang_posn_'+str(wg)+'_drg_'+str(np.round(beta,5))+'.png')

plt.figure()
plt.plot(t_arr,x_arr2[:,0]-x_arr[:,0])
plt.show()