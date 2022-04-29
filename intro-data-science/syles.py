from matplotlib import pyplot as plt
import pandas as pd

deshaun = pd.read_csv('worked_hours.csv')
aditya = pd.read_csv('worked_hours2.csv')

# Change the color of Phoenix to `"DarkCyan"`
plt.plot(deshaun["day_of_week"], deshaun["hours_worked"], label="Phoenix", color="DarkCyan")

# Make the Los Angeles line dotted
plt.plot(aditya["day_of_week"], aditya["hours_worked"], label="Los Angeles", linestyle='--', marker='s')

plt.legend()
plt.show()