"""Script to enhance the frame rate of data with a temporal dimension.

Usage:  On the bottom of the script a file can be read.
		It is necessary to specify the unit of time e.g. 'D', 'W', 'M', 'Y'
		The framerate will be per 1 unit of time. 
		Specify the interpolation frame rate to get smoother change in data. If a higher
		frame rate is necessary but no interpolation is required, constant_frame_rate 
		can be used. The total frame rate per unit of time is 
		interpolation_frame_rate * constant_frame_rate. 

		It is also necessary to give the column(s) the data will be grouped by 
		as a list (e.g ["country"]).

		The results can be visualized by uncommenting the plotting section

"""

import pandas as pd 

def enhance_frames(df, interpolation_frame_rate=1, constant_frame_rate=1, groupby=[], unit='D'):
	"""Increases the number of entries in a pandas.DataFrame
	object.

	Args:
		df (pandas.DataFrame): Requires a datetime index.
		interpolation_frame_rate (int): number of frames per unique date. Values in the DataFrame
			get linearly interpolated.
		constant_frame_rate (int): number of frames to be repeated. This will be applied after
			interpolation_frame_rate.
	Returns:
		pandas.DataFrame
	"""

	df["date"] = pd.to_datetime(df["date"])
	df = df.set_index("date").sort_index()

	rule = int(pd.Timedelta(1, unit=unit).total_seconds() / interpolation_frame_rate)
	
	df = df.groupby(groupby).resample(
		str(rule)+"S", closed='right').interpolate(method='linear')
	df = df.drop(columns=groupby)
	df = df.reset_index()

	df = df.set_index("date").sort_index()


	rule = int(pd.Timedelta(1, unit=unit).total_seconds() / constant_frame_rate / interpolation_frame_rate)
	df = df.groupby(groupby).resample(
		str(rule)+"S", closed='right').pad()
	df = df.drop(columns=groupby)
	df = df.reset_index()
	df = df.set_index("date").sort_index()

	df = df.groupby(groupby).apply(lambda x : x.reset_index()).drop(columns=groupby).reset_index()
	df = df.rename(columns={"level_1" : "frame_index"})
	return df

if __name__ == '__main__':
	df = pd.read_csv('../data/cleaned_global_covid_data.csv')

	print(df)
	df = enhance_frames(df, 
		interpolation_frame_rate=1, 
		groupby=["country"], 
		constant_frame_rate=1)

	print(df)

	df.to_csv("../data/enhanced_global_covid_data.csv")
	
	# plotting
	pd.options.plotting.backend = "plotly"
	#fig = df.plot(y=["n_infected"], color="country")
	#fig = df.plot(y=["frame_index"], color="country")

	#fig.write_html("test.html")
