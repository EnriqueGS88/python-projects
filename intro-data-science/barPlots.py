from matplotlib import pyplot as plt

# Display the DataFrame hours using print
print(hours)

# Create a bar plot from the DataFrame hours
# Add error bars = standard deviation
plt.bar(hours.officer, hours.avg_hours_worked, yerr=hours.std_hours_worked, label="Hours Worked")

# Display the plot
plt.show()