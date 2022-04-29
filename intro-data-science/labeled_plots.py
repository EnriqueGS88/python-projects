from matplotlib import pyplot as plt
import pandas as pd

deshaun = pd.read_csv('worked_hours.csv')
aditya = pd.read_csv('worked_hours2.csv')

# Lines
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')

# Add annotation "Missing June data" at (2.5, 80)
xcord = 2.5
ycord = 80

plt.text(xcord, ycord, "Missing Thu data")

# Add a title
plt.title("Worked hours", fontsize=16)

# Add y-axis label
plt.ylabel("hours")

# Legend
plt.legend()
# Display plot
plt.show()