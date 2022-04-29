import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed(42)

ages = np.random.randint(low = 8, high = 30, size = 35)
heights = np.random.randint(130, 195, 35)
weights = np.random.randint(30, 160, 35)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Formatting data points
ax.scatter( xs = heights, ys = weights, zs = ages, c="green" )

# Add a title
ax.set_title("Age-wise body weight-height distribution")

# Add axes
ax.set_xlabel("height (cm)")
ax.set_ylabel("weight (kg)")
ax.set_zlabel("age (years)")

# Turn off gridlines
# ax.grid(False)

# Limit the Axes
ax.set_xlim(100, 200)
ax.set_ylim(20, 160)
ax.set_zlim(5, 35)

# Fix specific values for X
ax.set_xticks([100, 125, 150, 175, 200])
ax.set_yticks([20,55,90,125,160])
ax.set_zticks([5,15,25,35])

plt.show()