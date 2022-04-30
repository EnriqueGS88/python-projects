import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Create a regression plot of premiums vs. insurance_losses
sns.regplot(data=df,
            x="insurance_losses",
            y="premiums")

# Display the plot
plt.show()

