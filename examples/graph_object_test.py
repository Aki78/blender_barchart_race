import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly


frames = []



RANGE = 25
fib_lst = []
START = np.ones(10) * 5
y = START.copy()
for i in range(RANGE):
	y += np.random.rand(10) - 0.5



	bar = go.Bar(x = np.arange(10), y = y)
	data = [bar]

	frames.append(go.Frame(data = data))




fig = go.Figure(
	data =[go.Bar(x= np.arange(10), y=  START )],
	frames = frames,
    layout=go.Layout(
        xaxis=dict(range=[0, 10], autorange=False),
        yaxis=dict(range=[1, 10], autorange=False),
        transition = {'duration': 5000},
        updatemenus=[dict(
    	type="buttons",
    	buttons=[dict(label="Play",
          	method="animate",
          	args=[None, {"frame": {"duration": 600, 
                    "redraw": False},
          		"fromcurrent": True,
          		"easing" : "linear", 
          		"transition": {"duration": 600},
          		"mode" : "immediate"}]
          )])]
	        )
    )

fig.show()

