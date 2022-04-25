import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(6,6))

ax = fig.add_subplot(111, projection='3d')

# Plot the point (2,3,4) on the 3d space
ax.scatter(2,3,4)

plt.show()
