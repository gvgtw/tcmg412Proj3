from datetime import datetime
import urllib.request
import os
from array import *

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

if (os.path.isfile(LOCAL_FILE) == False):
    local_file, headers = urllib.request.urlretrieve(URL_PATH, LOCAL_FILE)

pLog = [[]*5]*1


totalRequest = 0
totalLogs = 0
reqTimeFrame = 0
with open(LOCAL_FILE) as f:
    for line in f:
        line = line.split(" ")
        if len(line) < 10:
            continue
        datetime.strptime(line[3].replace("[", ""), "%d/%b/%Y:%H:%M:%S")
        totalRequest += 1
        pLog.append(line)
        if totalRequest == 100:
            break
    #print("This is a Test line: Spot #1")

del pLog[0]

print (pLog)
print("Total request made within the log: ", totalRequest)
