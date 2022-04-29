import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Create a regression plot of premiums vs. insurance_losses
sns.regplot(data=df,
            x="insurance_losses",
            y="premiums")

# Display the plot
plt.show()

# Alternatively you can use LMPLOT

# Create a regression plot of premiums vs. insurance_losses
# HUE = shows multiple regions in 1 single chart
sns.lmplot(data=df,
            x="insurance_losses",
            y="premiums", hue="Region")


# COL = shows 1 Chart on the right for every single 1 Region
sns.lmplot(data=df,
            x="insurance_losses",
            y="premiums", col="Region")

# ROW = shows 1 Chart BELOW for every single 1 Region
sns.lmplot(data=df,
            x="insurance_losses",
            y="premiums", row="Region")

# Display the plot
plt.show()