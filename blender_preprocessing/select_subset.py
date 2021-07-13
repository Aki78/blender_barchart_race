import pandas as pd 


def select_subset(df, column_name, column_values):
	df = df[df["country"].isin(column_values)]
	return df




if __name__ == '__main__':
	df = pd.read_csv('../data/enhanced_global_covid_data.csv')

	print(df)
#	df = select_subset(df, column_name = "country", column_values = ["Germany", "Finland"])
	df = select_subset(df, column_name = "country", column_values = ["Denmark","Finland"])

	print(df)

	df.to_csv("../data/subset_global_covid_data.csv")
	
	# plotting
	pd.options.plotting.backend = "plotly"
	#fig = df.plot(y=["n_infected"], color="country")
	#fig.write_html("test.html")
