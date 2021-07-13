import bar_chart_race as bcr
import pandas as pd
import plotly

from plotly.subplots import make_subplots
import plotly.graph_objects as go

import pycountry
import plotly.express as px

# Get the three-letter country codes for each country
def get_country_code(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None


df_raw = pd.read_csv('../data/melted_global_covid_data.csv')
df = df_raw.copy()
df = df[['date', 'Country/Region', 'value', 'Province/State']]
df = df.rename(columns={'Country/Region' : 'Country', 'value' : 'n_infected', 'Province/State' : 'Province'})
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

# filter dates
df = df[(df.date > '2020-05-1') & (df.date < '2020-06-1')]

df = df.groupby(['date', 'Country']).sum().reset_index()

df_pivot = df.pivot(index=["date"], columns=["Country"],values="n_infected").copy()

print(df_pivot)
print(df)


fig = bcr.bar_chart_race_plotly(
    df=df_pivot,
    #filename='covid19_horiz.mp4',
    orientation='h',
    sort='desc',
    n_bars=5,
    fixed_order=False,
    fixed_max=False,
    steps_per_period=3,
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
    #fig=fig,
    bar_kwargs={"xaxis":"x2", "yaxis":"y2"},
    layout_kwargs={'xaxis2': {'anchor': 'y2', 'domain': [0.6, 0.95]}, 
        'yaxis2': {'anchor': 'x2', 'domain': [0.6, 0.95]}},
        #dict(
        #    xaxis2={"domain":[0.8, 1]},
        #    yaxis2={"anchor":"x2"}),
    filter_column_colors=True)





# fig.set_subplots(2, 1, horizontal_spacing=0.1)

# fig.add_trace(go.Bar(y=[2, 3, 1]),
#               row=2, col=1)


df['iso_alpha_3'] = df['Country'].apply(get_country_code)
df['date'] = df['date'].dt.strftime('%Y-%m-%d')


fig2 = px.choropleth(df,                            # Input Dataframe
                     locations="iso_alpha_3",           # identify country code column
                     color="n_infected",                     # identify representing column
                     hover_name="Country",              # identify hover name
                     animation_frame="date",        # identify date column
                     projection="natural earth",        # select projection
                     color_continuous_scale = 'Peach',  # select prefer color scale
                     #range_color=[0,50000],              # select range of dataset
                     )

#fig2.data[0].xaxis = "x1"
#fig2.data[0].yaxis = "x2"


#fig.update_layout(height=700, showlegend=False)

#fig.show()

#print(len(fig.frames))
#print(len(fig2.frames))
#print(fig2.frames)

for f in fig2.frames:
    print(f.name)
for f in fig.frames:
    print(f.name)

#print(fig.frames[0])
#print(fig.data)

#print(fig2.data)
#print(fig2.frames[0])


# create new figure combining both

combined_frames = []

enhanced_frames2 = [] 
for i, frame in enumerate(fig2.frames):
    if i == 0:
        continue
    enhanced_frames2.extend([frame] * 10) # steps per period from bcr

for f1, f2 in zip(enhanced_frames2, fig.frames):
    #print(f1.data)
    #print(f2.data)
    #exit()
    combined_frames.append(
        go.Frame(
            data=[
                f1.data[0],
                f2.data[0]])
        )




combined_fig = go.Figure(
    data=combined_frames[0].data,
    frames=combined_frames,
    layout=fig.layout)

#combined_fig.update_layout(dict(
#    xaxis={"domain":[0, 0.7]}))


#print("layout of combined figures")
#print(combined_fig.layout)
combined_fig.layout.annotations = None
combined_fig.layout.margin = None
combined_fig.layout.title = None

# update layout for other figure (world map)
combined_fig.layout.geo = fig2.layout.geo
combined_fig.layout.geo.domain = {'x': [0.0, 1], 'y': [0.0, .6]}

combined_fig.layout.coloraxis = fig2.layout.coloraxis

combined_fig.layout.sliders = fig2.layout.sliders

combined_fig.show()


#print(fig.data)

#print(fig2.layout)
print("layout of combined figures")

print(combined_fig.layout)




#print(combined_fig.data)