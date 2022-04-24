from mpl_toolkits.mplot3d import Axes3D

# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)
#ax = plt.axes( projection = '3d' )

#ax = plt.axes( projection = '3d' )
#
## Data for a 3d line
#zline = np.linspace( 0, 15, 1000 )
#xline = np.sin( zline )
#yline = np.cos( zline )
#ax.plot3D( xline, yline, zline, 'gray' )
#
## Data for 3d scattered points
#zdata = 15 * np.random.random( 100 )
#xdata = np.sin( zdata ) + 0.1 * np.random.random( 100 )
#ydata = np.cos( zdata ) + 0.1 * np.random.random( 100 )
#ax.scatter3D( xdata, ydata, zdata, c = zdata, cmap = 'Greens')