import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed(42)

xs = np.random.random(100)*10+20
ys = np.random.random(100)*5+7
zs = np.random.random(100)*15+50

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Formatting data points
ax.scatter( xs, ys, zs, c="green" )

# Add a title
ax.set_title("Atom velocity distribution")

# Add axes
ax.set_xlabel("atomic mass (dalton)")
ax.set_ylabel("atomic radius (pm)")
ax.set_zlabel("atomic velocity (x10^6 m/s)")

# Turn off gridlines
ax.grid(False)


plt.show()