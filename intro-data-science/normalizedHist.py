from matplotlib import pyplot as plt
import pandas as pd

gravel = pd.read_csv('radius.csv')

# Create a histogram
# Normalize to 1
plt.hist(gravel.radius,density=True)

print(gravel.head())

# Display histogram
plt.show()