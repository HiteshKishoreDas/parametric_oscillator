import numpy as np
from matplotlib import pyplot as plt
import para_oscl as po
from globals import *

from matplotlib.animation import FuncAnimation
# plt.style.use('seaborn-pastel')

dth0 = 0.1*th0

x_arr,t_arr = po.para_oscl(a,b,th0,thdot0,N)
x_arr2,t_arr2 = po.para_oscl(a,b,th0+dth0,thdot0,N)

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-2, 2), ylim=(-2, 2))
ax.grid()
line1, = ax.plot([], [],'o-', lw=3)
line2, = ax.plot([], [],'o-', lw=3)

n = 50

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2,
def animate(i):
    x = [ 0, 0+l*np.sin(x_arr[i*n,0]) ]
    y = [ 0, 0-l*np.cos(x_arr[i*n,0]) ]

    x2 = [ 0, 0+l*np.sin(x_arr2[i*n,0]) ]
    y2 = [ 0, 0-l*np.cos(x_arr2[i*n,0]) ]

    print(int(N/n), i)

    line1.set_data(x, y)
    line2.set_data(x2, y2)
    return line1, line2,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=int(N/n), interval=100, blit=True)


anim.save('para_oscl_'+str(wg)+'.mp4', writer='ffmpeg')
print('Done!')