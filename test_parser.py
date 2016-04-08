import os
import csv
import json
import collections
from collections import defaultdict

filename = "C:/Users/zeffi/Documents/Export_482016.csv"
some_dict = defaultdict(list)

def sanedate(date):
    MM, DD, YYYY = date.split('/')
    return '/'.join([DD, MM, YYYY])

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
            date = date + '__' + sanedate(date)
            gtime = formatted_time(gtime)
            some_dict[date].append({'time': gtime, 'value': float(gvalue)})
        except:
            print("failed at")
            print(row)

    with open('C:/Users/zeffi/Documents/some_constructed.json', 'w') as wfile:
       wfile.write(json.dumps(some_dict, sort_keys=True, indent=4))



open_csv_test(filename)
