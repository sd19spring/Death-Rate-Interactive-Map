"Interactive Map of Deaths in United States (1999-2016)"
"@Autors: Kristin Aoki and Sina "

#--------------------------------------------------------------------------------------
import csv
import pandas as pd
import os
import folium

state_geo = os.path.join('data', 'us_states.json')
state_deaths = os.path.join('data','death.csv')
state_data = pd.read_csv(state_deaths)

m = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(geo_data=state_geo,name='choropleth',data=state_data,
    columns=['State',  'Death Rate'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Death Rate (1999-2016)'
).add_to(m)

folium.LayerControl().add_to(m)

m.save('map.html')

# with open(NCHS_-_Leading_Causes_of_Death__United_States(1).csv) as csvf:
#     readCSV = csv.DictReader(csvf) #saving csv data to a dictionary
