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


yearly_map(2014)
