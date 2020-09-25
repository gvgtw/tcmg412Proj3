from datetime import datetime
import urllib.request
import os
from array import *

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

if (os.path.isfile(LOCAL_FILE) == False):
    local_file, headers = urllib.request.urlretrieve(URL_PATH, LOCAL_FILE)

pLog = [[]*5]*1
avgAccess = []
avgAccessVariable = 0

totalRequest = 0
totalFailedRequest = 0
totalRedirectedRequest = 0
with open(LOCAL_FILE) as f:
    for line in f:
        line = line.split(" ")
        if len(line) != 10:
            continue
        temp = int(line[8]) 
        if (temp >= 400) and (temp <= 499):
            totalFailedRequest += 1
        elif (temp >= 300) and (temp <= 399):
            totalRedirectedRequest += 1
        timestamp = datetime.strptime(line[3].replace("[", ""), "%d/%b/%Y:%H:%M:%S")
        temp2 = timestamp.date
        if temp2 == temp3:
            avgAccess[avgAccessVariable] += 1
        else
            temp3 = temp2
            avgAccessVariable +=1    
        totalRequest += 1
        pLog.append(line)
        if totalRequest == 100:
            break
    #print("This is a Test line: Spot #1")

del pLog[0]

# print (pLog)
print("Total request made within the log: ", totalRequest)
print("What percentage of the request were not successful: ", totalFailedRequest/totalRequest * 100)
print("What percentage of the request were redirected elsewhere: ", totalRedirectedRequest/totalRequest * 100)
