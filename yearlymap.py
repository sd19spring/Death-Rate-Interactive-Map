import csv
import sys
import pandas as pd
import os
import folium
from folium import Marker, Map, Choropleth, LayerControl, Popup
import webbrowser

def yearly_map(year):
    """
    This function generates a file for a given year that will be used to generate the map.
    The data is being read from a CSV and written to a new file.
    """
    state_geo = os.path.join('data', 'us_states.json')
    state_deaths = os.path.join('data','death.csv')
    #allows file to be created for multiple years with the same file extension
    year_file = str(year)+'.csv'

    row_list = []
    f = open(state_deaths)
    csv_f = csv.reader(f)
    for row in csv_f:
        #reads csv to find rows for the given year to place in new file
        if row[0] == str(year):
            row_list.append(row)
            with open(year_file, 'w') as writeFile:
                writer = csv.writer(writeFile)
                #add the column titles
                writer.writerow(["Year","113 Cause Name","Cause Name","State","Deaths","Population","Death Rate"])
                for row in row_list:
                    writer.writerow(row)
    return year_file

def produce_map(year):
    """
    This function generates a map of the US and displays all the data for a given year in popups and a color gradient
    """
    year_file = yearly_map(year)
    state_geo = os.path.join('data', 'us_states.json')
    state_data = pd.read_csv(year_file)
    marker_year = 'StateLonandLat'+str(year)+'.csv'
    marker_data = os.path.join('data',marker_year)
    marker_coord = pd.read_csv(marker_data)

    #establishes the center of map based on longitude and latitude
    m = Map(location=[50.246366, -110], zoom_start=4)

    #sets the color scheme, data used for legend, and legend labels
    Choropleth(geo_data=state_geo,name='choropleth',data=state_data,
        columns=['State',  'Death Rate'],
        key_on='feature.id',
        fill_color='BuPu',
        fill_opacity=0.7,
        line_opacity=0.5,
        legend_name='Average Death Rate in '+str(year)
    ).add_to(m)
    #create markers and places them within corresponding state
    for i in range(0,len(marker_coord)):
        #popup contains data about causes fo death
        popup = Popup(marker_coord.iloc[i]['state'],max_width=350)
        Marker([marker_coord.iloc[i]['lon'],marker_coord.iloc[i]['lat']], popup=popup).add_to(m)
    LayerControl().add_to(m)
    map = str(year)+'.html'
    m.save(map)
    webbrowser.open('file://'+os.path.realpath(map))

if __name__ == "__main__":
    produce_map(2011)
    produce_map(2014)
    produce_map(2016)
