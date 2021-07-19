import csv

fp = "/home/aki/BlenderProjects/animated-plotengine/data/enhanced_global_covid_data.csv"
writer = csv.writer(open("/home/aki/BlenderProjects/animated-plotengine/data/final.csv", 'w'))

my_countries = ['Japan', 'Angola', 'Italy', 'Andorra', 'Spain', 'Australia', 'Sweden', 'Germany', 'Colombia', 'Chile', 'China', 'Taiwan*', 'Singapore', 'Peru', 'Kuwait', 'Norway', 'Albania', 'Russia', 'Korea, South', 'Diamond Princess', 'Vietnam', 'Iran', 'Pakistan', 'South Africa', 'Canada', 'Thailand', 'Malaysia', 'Afghanistan', 'Netherlands', 'Mexico', 'Turkey', 'Algeria', 'Bahrain', 'France', 'United Kingdom', 'Nepal', 'Switzerland', 'Argentina', 'US', 'Brazil', 'Belgium', 'India']

with open( fp ) as csvfile:
    rdr = csv.reader(csvfile)
    for i, row in enumerate(rdr): 
        if i == 0:
            writer.writerow(row)
            continue
        if row[1] in my_countries: 
            writer.writerow(row)
