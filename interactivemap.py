"Interactive Map of Deaths in United States (1999-2016)"
"@Autors: Kristin Aoki and Sina "


#--------------------------------------------------------------------------------------
import csv
import operator
import pandas as pd
import os
import folium
from folium import Choropleth, Map, Marker, LayerControl
from folium import IFrame

state_geo = os.path.join('data', 'us_states.json')
state_deaths = os.path.join('data','death.csv')
state_data = pd.read_csv(state_deaths)
marker_data = os.path.join('data', 'StateLonandLat1999-2016.csv')#need to make this a more universal statement because each each has own file
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
        popup = folium.Popup(marker_coord.iloc[i]['state'],max_width=350)
        Marker([marker_coord.iloc[i]['lon'],marker_coord.iloc[i]['lat']], popup=popup).add_to(m)
    LayerControl().add_to(m)

if __name__ == "__main__":
    m.save('AverageMap.html')
