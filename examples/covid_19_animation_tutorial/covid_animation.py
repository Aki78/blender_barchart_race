import pandas as pd

df = pd.read_csv('global_covid_data.csv')

print(df.info())

print(df.columns)

df = pd.melt(df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='date', value_name='value')


print(df)


df.to_csv('melted_global_covid_data.csv')