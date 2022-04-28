import pandas as pd

df = pd.read_csv('test.csv')
mpr = pd.read_csv('dogs.csv')

# select column with bracket notation
age1 = df['age']

# select column with dot notation
age2 = df.age

#print(df.head())
##print(age1)
##print(age2)
#print(df.info())


# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status == 'Still Missing']
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[ mpr['Dog Breed'] != 'Poodle']
print(not_poodle)