import pandas as pd
import numpy as np

quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.graph_objects as go

print(quakes.describe())

frames = []
RANGE = 25
START = np.ones(10) * 5
y = START.copy()
for i in range(RANGE):
	dmb = go.Densitymapbox(lat=quakes.Latitude + i * 5, lon=quakes.Longitude + i * 5, z=quakes.Magnitude + i,
                                 radius=10)
	data = [dmb]
	frames.append(go.Frame(data = data))


fig = go.Figure(
	data = frames[0].data,
	frames = frames,
    layout=go.Layout(
    transition = {'duration': 5000},
    updatemenus=[dict(
	type="buttons",
	buttons=[dict(label="Play",
      	method="animate",
      	args=[None, {"frame": {"duration": 600, 
                "redraw": True},
      		"fromcurrent": True,
      		"easing" : "linear", 
      		"transition": {"duration": 600},
      		"mode" : "immediate"}]
      )])]
        )
	)
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()