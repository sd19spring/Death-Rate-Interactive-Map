import csv
import sys
import pandas as pd
import os
import folium
import shutil

def yearly_map(year):
    state_geo = os.path.join('data', 'us_states.json')
    state_deaths = os.path.join('data','death.csv')
    year_file = str(year)+'.csv'


    row_list = []
    f = open(state_deaths)
    csv_f = csv.reader(f)
    for row in csv_f:
        if row[0] == str(year):
            row_list.append(row)
            with open(year_file, 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerow(["Year","113 Cause Name","Cause Name","State","Deaths","Population","Death Rate","Age-adjusted Death Rate"])
                for row in row_list:
                    writer.writerow(row)
                writeFile.close()

def produce_map(year):
    yearly_map(year)
    year_file = str(year)+'.csv'
    state_geo = os.path.join('data', 'us_states.json')
    #state_deaths = os.path.join('data',year_file)
    state_data = pd.read_csv(year_file)
    marker_year = 'StateLonandLat'+str(year)+'.csv'
    marker_data = os.path.join('data',marker_year)
    marker_coord = pd.read_csv(marker_data)

    #establishes the center of map based on longitude and latitude
    m = folium.Map(location=[50.246366, -110], zoom_start=4)

    #sets the color scheme, data used for legend, and legend labels
    folium.Choropleth(geo_data=state_geo,name='choropleth',data=state_data,
        columns=['State',  'Death Rate'],
        key_on='feature.id',
        fill_color='BuPu',
        fill_opacity=0.7,
        line_opacity=0.5,
        legend_name='Average Death Rate in '+str(year)
    ).add_to(m)
    for i in range(0,len(marker_coord)):
        popup = folium.Popup(marker_coord.iloc[i]['state'],max_width=350)
        folium.Marker([marker_coord.iloc[i]['lon'],marker_coord.iloc[i]['lat']], popup=popup).add_to(m)
# <<<<<<< HEAD
    folium.LayerControl().add_to(m)
    m.save(str(year)+'.html')

# produce_map(2011)
# =======
# #establishes the center of map based on longitude and latitude
# m = folium.Map(location=[50.246366, -110], zoom_start=4)
#
# #sets the color scheme, data used for legend, and legend labels
# folium.Choropleth(geo_data=state_geo,name='choropleth',data='2014.csv',
#     columns=['State',  'Death Rate'],
#     key_on='feature.id',
#     fill_color='BuPu',
#     fill_opacity=0.7,
#     line_opacity=0.5,
#     legend_name='Average Death Rate (2014)'
# ).add_to(m)
# for i in range(0,len(marker_coord)):
#     popup = folium.Popup(marker_coord.iloc[i]['state'],max_width=350)
#     folum.Marker([marker_coord.iloc[i]['lon'],marker_coord.iloc[i]['lat']], popup=popup).add_to(m)
# folium.LayerControl().add_to(m)

if __name__ == "__main__":
    yearly_map(2014)
    produce_map(2014)
    yearly_map(2016)
    produce_map(2016)
# >>>>>>> 8b342e1c40ce9d9a5b85cefea766dc210226058c
