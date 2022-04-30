import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Plot the pandas histogram
df['fmr_2'].plot.hist()
plt.show()
plt.clf()

# Set the default seaborn style
sns.set()

# Plot the pandas histogram again
df['fmr_2'].plot.hist()
plt.show()
plt.clf()


# Using predetermined styles 

for style in ['white','dark']:sns.set_style(style)

sns.distplot(df['fmr_2'])
plt.show()
plt.clf()