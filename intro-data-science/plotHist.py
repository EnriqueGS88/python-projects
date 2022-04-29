# Change the range to start at 5 and end at 35
plt.hist(puppies.weight, bins=50, range=(5, 35))
plt.hist(puppies.weight, bins=10)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()