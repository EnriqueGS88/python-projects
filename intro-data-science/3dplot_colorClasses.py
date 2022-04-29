import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed(42)

ages = np.random.randint(low = 8, high = 30, size = 35)
heights = np.random.randint(130, 195, 35)
weights = np.random.randint(30, 160, 35)

 # 0 for male, 1 for female
gender_labels = np.random.choice([0, 1], 35)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Formatting data points
scat_plot = ax.scatter( xs = heights, ys = weights, zs = ages, c=gender_labels )

# Add a title
ax.set_title("Age-wise body weight-height distribution")

# Add axes
ax.set_xlabel("height (cm)")
ax.set_ylabel("weight (kg)")
ax.set_zlabel("age (years)")

# Turn off gridlines
# ax.grid(False)

# Add a color bar for the Labels

cb = plt.colorbar( scat_plot, pad=0.2 )

cb.set_ticks([0,1])

cb.set_ticklabels(["Male", "Female"])

plt.show()