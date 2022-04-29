import matplotlib.pyplot as plt
import numpy as np

x = np.linspace( 0, 20, 100 )   # Create a list of evenly-spaced numbers over the range
plt.plot( x, np.sin(x) )        # Plot the sine of each x point
plt.show()                      # Display the plot

y = np.linspace( 0, 15, 70 )   # Create a list of evenly-spaced numbers over the range
plt.plot( y, np.sin(y) )        # Plot the sine of each x point
plt.show()   