from matplotlib import pyplot as plt
import pandas as pd

deshaun = pd.read_csv('worked_hours.csv')
aditya = pd.read_csv('worked_hours2.csv')

# Officer Deshaun
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')

# Add a label to Aditya's plot
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')

# Add a command to make the legend display
plt.legend()

# Display plot
plt.show()