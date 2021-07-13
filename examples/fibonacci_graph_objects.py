import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly


frames = []


def fibonacci(n, N):
	if n < (N -1):
		return fibonacci(n+1, N) + fibonacci(n+2, N)
	else:
		return 1
	

RANGE = 25
fib_lst = []
for i in range(RANGE):
	fib = fibonacci(0,i)
	fib_lst.append(fib)





	bar = go.Bar(x = list(range(1,i + 1)), y = fib_lst.copy())
	data = [bar]

	frames.append(go.Frame(data = data))




fig = go.Figure(
	data =[go.Bar(x=[0, 1], y=[0, 1])],
	frames = frames,
    layout=go.Layout(
        xaxis=dict(range=[1, RANGE], autorange=False),
        yaxis=dict(range=[1, fibonacci(0, RANGE)], autorange=False),
        updatemenus=[dict(
    	type="buttons",
    	buttons=[dict(label="Play",
          method="animate",
          args=[None])])]
	        )
    )

#fig.write_image("image.png")

from export_frames import export_frames

export_frames(fig, "name")
#fig.show()

print(fig.data)
print(fig.layout)

