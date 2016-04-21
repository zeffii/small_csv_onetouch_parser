import os
import csv
import json
import collections
from collections import defaultdict

"""
"07/04/2016": {
      "sleeptimes": "",
      "comments": "",
      "glucose": [
        {"time": "21:53", "value": 22.92},
        {"time": "17:57", "value": 19.59},
        {"time": "12:12", "value": 19.26},
        {"time": "08:06", "value": 5.72}
    ]
  }
"""


filename = r"C:\Users\zeffi\OneDrive\Documents\Export_4212016.csv"
some_dict = defaultdict(list)

def sanedate(date):
    MM, DD, YYYY = date.split('/')
    return '/'.join([YYYY, MM, DD])

def formatted_time(gtime):
    HH, MM, SS = gtime.split(':')
    return ':'.join([HH, MM])

def open_csv_test(filename):
    #csvfile = open(filename, 'r', encoding='ISO-8859-15', newline='')
    csvfile = open(filename, 'r', newline='')
    ofile = csv.reader(csvfile, delimiter=',')

    # skip the first 7 lines (OneTouch uses an odd csv format)
    for i in range(6):
        next(ofile)

    for row in ofile:
        try:
            print(row)
            date, gtime, gvalue = row[1:4]
            date = sanedate(date)
            gtime = formatted_time(gtime)
            some_dict[date].append({'time': gtime, 'value': float(gvalue)})
        except:
            print("failed at")
            print(row)

    for k, v in some_dict.items():
        v = v.reverse()

    new_some_dict = defaultdict(dict)
    for k, v in some_dict.items():
        new_some_dict[k]['glucose'] = v
        new_some_dict[k].update(dict(times="", comments=""))


    with open('C:/Users/zeffi/Documents/some_constructed.json', 'w') as wfile:
       wfile.write(json.dumps(new_some_dict, sort_keys=True, indent=4))



open_csv_test(filename)
