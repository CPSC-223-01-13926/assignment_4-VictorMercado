import json as JSON
import calendar

# takes a filename, laods the json into a dictionary, and returns the dictionary
def read_data(filename):
    try: 
        with open(filename, 'r') as f:
            return JSON.loads(f.read())
    except FileNotFoundError:
        return {}

def write_data(data, filename):
    try:
        with open(filename, 'w') as f:
            f.write(JSON.dumps(data))
    except FileNotFoundError:
        return "File not found"

def max_temperature(data, date):
    x = 0 
    for key in data:
        if key[0:8] == date:
            if data[key]["t"] > x:
                x = data[key]["t"]
    return x                 

def min_temperature(data, date):
    x = 9999
    for key in data:
        if key[0:8] == date:
            if data[key]["t"] < x:
                x = data[key]["t"]
    return x

def max_humidity(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if data[key]["h"] > x:
                x = data[key]["h"]
    return x

def min_humidity(data, date):
    x = 9999
    for key in data:
        if date == key[0:8]:
            if data[key]["h"] < x:
                x = data[key]["h"]
    return x

# will return a float of the total rainfall for the given date
def tot_rain(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            x += data[key]["r"]
    return x

# data must be a dictionary, date is a string in the format YYYYMMDD
def report_daily(data, date):
    # data is an json dumps object
    display =           "========================= DAILY REPORT ========================\n"
    display = display + "Date                      Time  Temperature  Humidity  Rainfall\n"
    display = display + "====================  ========  ===========  ========  ========\n"
    for key in data:
        if date == key[0:8]:
            monthdayyear = calendar.month_name[int(date[4:6])] + " " + str(date[6:8]).lstrip("0") + ", " + str(date[0:4])
            time = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
            display = display + f'{monthdayyear:22}{time:10}{data[key]["t"]:11}{data[key]["h"]:10}{round(data[key]["r"],2):10}'+"\n"
    return display

def alterList(list):
    for i in range(len(list)):
        list[i] = list[i][0:8]
    return list
# data has all dates
def report_historical(data):
    display =           "============================== HISTORICAL REPORT ===========================\n"
    display = display + "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    display = display + "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    display = display + "====================  ===========  ===========  ========  ========  ========\n"
    newList = list(set(alterList(list(data.keys()))))
    newList.sort()
    current_date = newList[0]
    loopConditional = True
    while loopConditional:
        min_temp = min_temperature(data, current_date)
        max_temp = max_temperature(data, current_date)
        min_humid = min_humidity(data, current_date)
        max_humid = max_humidity(data, current_date)
        total_rain = tot_rain(data, current_date)
        monthdayyear = calendar.month_name[int(current_date[4:6])] + " " + str(current_date[6:8]).lstrip("0") + ", " + str(current_date[0:4])
        display = display + f'{monthdayyear:22}{min_temp:11}{max_temp:13}{min_humid:10}{max_humid:10}{"":6}' + f'{total_rain:.2f}' + "\n"
        if current_date == newList[-1]:
            loopConditional = False
        else:
            current_date = newList[1]
    
    return display
