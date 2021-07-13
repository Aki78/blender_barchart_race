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

df = df.groupby(['date', 'Country']).sum().reset_index()

df_pivot = df.pivot(index=["date"], columns=["Country"],values="n_infected").copy()

print(df_pivot)
print(df)


#fig = make_subplots(rows=2, cols=1, subplot_titles = ('Subplot (1,1)', 'Subplot(1,2)'))


fig = bcr.bar_chart_race_plotly(
    df=df_pivot,
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
    #fig=fig,
    #bar_kwargs={'row': 1, 'col' : 1},
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




#fig.update_layout(height=700, showlegend=False)

#fig.show()

def figures_to_html(figs, filename="dashboard.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")



figures_to_html([fig, fig2])
