import pandas as pd

#example_df = bcr.load_dataset('covid19_tutorial')
df = pd.read_csv('../data/melted_global_covid_data.csv')
df = df[['date', 'Country/Region', 'value', 'Province/State']]
df = df.rename(columns={'Country/Region' : 'country', 'value' : 'n_infected', 'Province/State' : 'Province'})
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

#df = df.drop(columns=["Unnamed: 0"])
#print(df.Country.unique())
#print(len(df.Country.unique()))


#df = df[df.Province.isna()]
df = df.groupby(['date', 'country']).sum().reset_index()
#df.index.name = "index"
df = df.set_index("date")

df.to_csv("cleaned_global_covid_data.csv")

print(df)