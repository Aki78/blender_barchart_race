import pycountry
import pandas as pd

# Aggregate the dataset
df_confirm = pd.read_csv('global_covid_data.csv')  
df_confirm = df_confirm.drop(columns=['Province/State','Lat', 'Long'])
df_confirm = df_confirm.groupby('Country/Region').agg('sum')
date_list = list(df_confirm.columns)

# Get the three-letter country codes for each country
def get_country_code(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None
df_confirm['country'] = df_confirm.index
df_confirm['iso_alpha_3'] = df_confirm['country'].apply(get_country_code)

# Transform the dataset in a long format
df_long = pd.melt(df_confirm, id_vars=['country','iso_alpha_3'], value_vars=date_list)
print(df_long)
print(df_long.info())

import plotly.express as px

fig = px.choropleth(df_long,                            # Input Dataframe
                     locations="iso_alpha_3",           # identify country code column
                     color="value",                     # identify representing column
                     hover_name="country",              # identify hover name
                     animation_frame="variable",        # identify date column
                     projection="natural earth",        # select projection
                     color_continuous_scale = 'Peach',  # select prefer color scale
                     #range_color=[0,50000]              # select range of dataset
                     )        
#fig.show()          
#fig.write_html("example_map.html")                      # write the result to HTML file

#print(fig.__dict__)

#print(fig.layout)
#print(fig.data)
#print(fig.frames)
