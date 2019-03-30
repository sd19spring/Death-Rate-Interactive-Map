#This File Copies info from State Raw Data to StateLonandLat1999

import csv
import os



def copy_state(year):
    """
    This generates the files that will be read by yearlymap.py to place text in popups for markers.
    The function takes in a year and maps all the data of that year from State files to a new file called StateLonandLat.csv 
    """

    state_list = ['state']

    for filename in sorted(os.listdir('States')):
        state_raw = os.path.join('States',filename)
        state_name = filename[:len(filename)-4]
        all_state_info = state_name + '\n'

        f = open(state_raw)
        csv_f = csv.reader(f)
        for row in csv_f:
            if row[0] == str(year):
                state_info = row[2] + ' - ' + row[4] + '\n'
                all_state_info += state_info
        state_list.append(all_state_info)
        f.close()

    item_list1 = []
    item_list2 = []
    total_row = []
    f1 = open('StateLonandLat.csv')
    csv_f1 = csv.reader(f1)

    for row in csv_f1:
        item_list1.append(row[0])
        item_list2.append(row[1])

    for n in range(len(item_list1)):
        item_list3 = []
        item_list3.append(item_list1[n])
        item_list3.append(item_list2[n])
        item_list3.append(state_list[n])
        total_row.append(item_list3)

    f1.close()


    with open('StateLonandLat'+str(year)+'.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        for row in total_row:
            writer.writerow(row)
        writeFile.close()

if __name__ == "__main__":
    copy_state(1999)
    copy_state(2000)
    copy_state(2001)
    copy_state(2002)
    copy_state(2003)
    copy_state(2004)
    copy_state(2005)
    copy_state(2006)
    copy_state(2007)
    copy_state(2008)
    copy_state(2009)
    copy_state(2010)
    copy_state(2011)
    copy_state(2012)
    copy_state(2013)
    copy_state(2014)
    copy_state(2015)
    copy_state(2016)
