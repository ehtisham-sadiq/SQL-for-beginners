import pandas as pd
df = pd.read_csv('/home/dell/Data/Introduction to data analyst and data science for begineers/SQL-for-beginners/world-university-rankings-202223/2023_QS_World_University_Rankings.csv')
# print(df.head())
denmark = df[df.location == 'Denmark']
print(denmark)