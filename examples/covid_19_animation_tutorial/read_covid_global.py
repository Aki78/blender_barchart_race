import urllib.request
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
output = './global_covid_data.csv'
urllib.request.urlretrieve(url, output)

