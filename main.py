from weather import *
import json as JSON

filePath = "/Users/victormercado/Documents/Classes/CPSC223P/assignment_4-VictorMercado/"

myChoice = ""
myFile = ""
weatherData = {}
while(True):
    print("*** Tuffy Titan Weather Logger Main Menu ***")
    print("Choose an option:")
    print("1. Set data FileName")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("5. Exit the program")
     
    myChoice = input("Enter your choice: ")

    if myChoice == "1":
        myFile = input("Enter the file name: ")
        write_data("", filePath + myFile + ".dat" )
        myFile = filePath + myFile + ".dat"
    elif myChoice == "2":
        date = input("Enter the date (YYYYMMDD): ")
        time = input("Enter the time (HHMMSS): ")
        temp = int(input("Enter the temperature (F): "))
        humid = int(input("Enter the humidity (%): "))
        rain = float(input("Enter the rainfall (in): "))
        data = {date + time: {"t": temp, "h": humid, "r": rain}}
        write_data(data, myFile)
    elif myChoice == "3":
        date = input("Enter the date (YYYYMMDD): ")
        weatherData = read_data(myFile)
        print(report_daily(weatherData, date))
    elif myChoice == "4":
        print(report_historical(weatherData))
    elif myChoice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

