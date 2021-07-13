import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

print(df.info())
print(df.head(20))
print(df.describe())

import plotly.express as px
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-watercolor",
                        color_continuous_scale = [(0, "black"), (0.9, "grey"), (1, "white")],
                        #color_continuous_scale = ["black", "grey", "white"],
                        )
fig.show()
