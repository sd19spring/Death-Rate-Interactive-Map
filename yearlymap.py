"Interactive Map of Deaths in United States (1999-2016)"
"@Autors: Kristin Aoki and Sina "

#--------------------------------------------------------------------------------------
import csv
import sys
import pandas as pd
import os
import folium

state_geo = os.path.join('data', 'us_states.json')
state_deaths = os.path.join('data','death.csv')
csv_file = pd.read_csv(state_deaths)


def yearly_map(year):
    """Takes year as an integer argument
    Makes a new csv file only containing the values for tha that year."""

    row_list = []
    f = open(state_deaths)
    csv_f = csv.reader(f)
    for row in csv_f:
        if row[0] == str(year):
            row_list.append(row)
            with open(str(year)+'.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                for row in row_list:
                    writer.writerow(row)

#establishes the center of map based on longitude and latitude
m = folium.Map(location=[50.246366, -110], zoom_start=4)

#sets the color scheme, data used for legend, and legend labels
folium.Choropleth(geo_data=state_geo,name='choropleth',data='2014.csv',
    columns=['State',  'Death Rate'],
    key_on='feature.id',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Average Death Rate (2014)'
).add_to(m)

folium.LayerControl().add_to(m)

if __name__ == "__main__":
    yearly_map(2014)
    m.save('map2014.html')
