from datetime import datetime
import urllib.request
import os
from array import *

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

if (os.path.isfile(LOCAL_FILE) == False):
    local_file, headers = urllib.request.urlretrieve(URL_PATH, LOCAL_FILE)

pLog = [[]*5]*1
avgAccess = [0]
avgAccessMonthly = [0]
uniqueDays = 0
uniqueMonths = 0

totalRequest = 0
totalFailedRequest = 0
totalRedirectedRequest = 0
previousDate = 0
previousMonth = 0

with open(LOCAL_FILE) as f:
    for line in f:
        line = line.split(" ")
        if len(line) != 10:
            continue
        temp = int(line[8]) 

        # Counting portion for failed and redirected functions
        if (temp >= 400) and (temp <= 499):
            totalFailedRequest += 1
        elif (temp >= 300) and (temp <= 399):
            totalRedirectedRequest += 1

        # Counting portion for time functions
        timestamp = datetime.strptime(line[3].replace("[", ""), "%d/%b/%Y:%H:%M:%S")
        temp2 = timestamp.day
        if temp2 == previousDate:
            avgAccess[uniqueDays] += 1
        else:
            previousDate = timestamp.day
            uniqueDays += 1
            avgAccess.append(1) 

        temp3 = timestamp.month
        if temp3 == previousMonth:
            avgAccessMonthly[uniqueMonths] += 1
        else:
            previousMonth = timestamp.month
            uniqueMonths += 1
            avgAccessMonthly.append(1)
        

        totalRequest += 1
        pLog.append(line)
        """
        if totalRequest == 100:
            break
        """
    # Auto Closing of file stream

sumofDays = sum(avgAccess)
totalofDays = len(avgAccess) - 1
averageofDays = sumofDays / totalofDays
averageofWeeks = sumofDays / (totalofDays / 7)

sumofMonths = sum(avgAccessMonthly)
totalofMonths = len(avgAccessMonthly) - 1
averageofMonths = sumofMonths / totalofMonths

del pLog[0]

# print (pLog)
print("Total request made within the log:                                   |   ", totalRequest)
print("-----------------------------------------------------------------------------------------------------")
print("Unique Days:                                                         |   ", uniqueDays)
print("-----------------------------------------------------------------------------------------------------")
print("Average access request per day:                                      |   ", averageofDays)
print("-----------------------------------------------------------------------------------------------------")
print("Average access request per week:                                     |   ", averageofWeeks)
print("-----------------------------------------------------------------------------------------------------")
print("Average access request per month:                                    |   ", averageofMonths)
print("-----------------------------------------------------------------------------------------------------")
print("What percentage of the request were not successful:                  |   ", totalFailedRequest/totalRequest * 100)
print("-----------------------------------------------------------------------------------------------------")
print("What percentage of the request were redirected elsewhere:            |   ", totalRedirectedRequest/totalRequest * 100)
print("-----------------------------------------------------------------------------------------------------")
