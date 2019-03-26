"Interactive Map of Deaths in United States (1999-2016)"
"@Autors: Kristin Aoki and Sina "


#--------------------------------------------------------------------------------------
import csv
import operator
import pandas as pd
import os
import folium
from folium import Choropleth, Map, Marker, LayerControl



state_geo = os.path.join('data', 'us_states.json')
state_deaths = os.path.join('data','death.csv')
state_data = pd.read_csv(state_deaths)
marker_data = os.path.join('data', 'State Long and Lat.csv')
marker_coord = pd.read_csv(marker_data)
#establishes the center of map based on longitude and latitude
m = Map(location=[50.246366, -110], zoom_start=4)

class AverageMap:
#sets the color scheme, data used for legend, and legend labels
    Choropleth(geo_data=state_geo,name='choropleth',data=state_data,
        columns=['State',  'Death Rate'],
        key_on='feature.id',
        fill_color='BuPu',
        fill_opacity=0.7,
        line_opacity=0.5,
        legend_name='Average Death Rate (1999-2016)'
        ).add_to(m)
    for i in range(0,len(marker_coord)):
        Marker([marker_coord.iloc[i]['lon'],marker_coord.iloc[i]['lat']], popup=marker_coord.iloc[i]['state']).add_to(m)
    LayerControl().add_to(m)

class Popup():
    'attributions:states, average number of deaths, location'

# class Popup:
#     with open(filename) as csvf:
#         readCSV = csv.DictReader(csvf) #saving csv data to a dictionary
def sort_state_data(filename):
    with open(filename, 'r')as f:
        csv1 = csv.reader(f, delimiter=',')
        sort = sorted(csv1,key=operator.itemgetter(5))
        #sort = sorted(csv1,key=lambda average: average[5])
        return sort

def popup_content(file1,file2):
    with open(file1,'r') as f1:
        df = pandas.read_csv(f1, index_col = 0)
        df.ix[2:3,]



if __name__ == "__main__":
    m.save('AverageMapmap.html')
    print(sort_state_data('Alabama.csv'))
