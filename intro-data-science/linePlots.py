import pandas as pd
from matplotlib import pyplot as plt

deshaun = pd.read_csv('worked_hours.csv')
mengfei = pd.read_csv('worked_hours2.csv')

# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)

# Plot another line on the chart
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

# Display Deshaun's plot
plt.show()