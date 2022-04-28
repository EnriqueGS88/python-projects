import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv')
r = pd.read_csv('test.csv')

plt.plot(df.age, df.location)

# print(r)
plt.show()