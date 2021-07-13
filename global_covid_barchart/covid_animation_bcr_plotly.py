import bar_chart_race as bcr
import pandas as pd

#example_df = bcr.load_dataset('covid19_tutorial')
df = pd.read_csv('../data/melted_global_covid_data.csv')
df = df[['date', 'Country/Region', 'value', 'Province/State']]
df = df.rename(columns={'Country/Region' : 'Country', 'value' : 'n_infected', 'Province/State' : 'Province'})
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

#print(df.Country.unique())
#print(len(df.Country.unique()))


#df = df[df.Province.isna()]
df = df.groupby(['date', 'Country']).sum().reset_index()

#print(len(df.Country.unique()))
#print(df[df.Country == "China"])


df = df.pivot(index=["date"], columns=["Country"],values="n_infected")


print(df)

fig = bcr.bar_chart_race_plotly(
    df=df,
    #filename='covid19_horiz.mp4',
    orientation='h',
    sort='desc',
    n_bars=8,
    fixed_order=False,
    fixed_max=False,
    steps_per_period=10,
    interpolate_period=False,
    #label_bars=True,
    bar_size=.95,
    #period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    #period_fmt='%B %d, %Y',
    #period_summary_func=lambda v, r: {'x': .99, 'y': .18,
    #                                  's': f'Total infections: {v.nlargest(6).sum():,.0f}',
    #                                  'ha': 'right', 'size': 8, 'family': 'Courier New'},
    perpendicular_bar_func=None,
    period_length=500,
    #figsize=(5, 3),
    #dpi=150,
    #cmap='dark24',
    title='COVID-19 Infections by Country',
    #title_size='',
    #bar_label_size=7,
    #tick_label_size=7,
    #shared_fontdict={'family' : 'Helvetica', 'color' : '.1'},
    scale='linear',
    #writer=None,
    #fig=None,
    #bar_kwargs={'alpha': .7},
    filter_column_colors=True)

print(fig.layout)
print(fig.frames[0])

# sources = [
    # "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Iris_setosa_var._setosa_%282595031014%29.jpg/360px-Iris_setosa_var._setosa_%282595031014%29.jpg",
    # "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Iris_versicolor_quebec_1.jpg/320px-Iris_versicolor_quebec_1.jpg",
    # "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/480px-Iris_virginica_2.jpg",
# ]
# # add images
# for i, src in enumerate(sources):
    # fig.add_layout_image(
        # source=src,
        # xref="x domain",
        # yref="y domain",
        # x=1,
        # y=1 / (i + 1),
        # xanchor="right",
        # yanchor="top",
        # sizex=0.2,
        # sizey=0.2,
    # )

# for i, frame in enumerate(fig.frames):
    # x = frame.data[0]["x"][6]
    # y = frame.data[0]["y"][6]
    # frame.add_layout_image(
        # source=src[0],
        # xref="x domain",
        # yref="y domain",
        # x=x,
        # y=y,
        # xanchor="right",
        # yanchor="top",
        # sizex=0.2,
        # sizey=0.2,
    # )   



from export_frames import export_frames
export_frames(fig,"firstimages", type="png")
#fig.show()
