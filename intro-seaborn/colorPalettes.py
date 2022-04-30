import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



# Set style, enable color code, and create a magenta distplot
sns.set(color_codes=True)
sns.distplot(df['fmr_3'], color='m')

# Show the plot
plt.show()


# Loop to compare multiple palettes for the same plot
# Loop through differences between bright and colorblind palettes
for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.distplot(df['fmr_3'])
    plt.show()
    
    # Clear the plots    
    plt.clf()


# palplot() displays all the colors in a palette
# the snippet below shows the 8 colors of a palette of Purplesk
sns.palplot(sns.color_palette("Purples", 8))
plt.show()
sns.palplot(sns.color_palette("husl", 10))
plt.show()
sns.palplot(sns.color_palette("coolwarm", 8))
plt.show()