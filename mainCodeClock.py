from datetime import datetime
import urllib.request
import os

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

if (os.path.isfile(LOCAL_FILE) == False):
    local_file, headers = urllib.request.urlretrieve(URL_PATH, LOCAL_FILE)
    
timeFrame = int(input('how many days back in the log file would you like counted: '))

totalRequest = 0
reqTimeFrame = 0
with open(LOCAL_FILE) as f:
    for line in f:
        line = line.split(" ")
        if len(line) < 10:
            continue
        timestamp = datetime.strptime(line[3].replace("[", ""), "%d/%b/%Y:%H:%M:%S")
        totalRequest += 1
        diffTime = datetime(1995,10,11,14,14,17) - timestamp
        if diffTime.days <= timeFrame:
            reqTimeFrame += 1
    print("This is a Test line: Spot #1")
   



print("Total request made within the log: ", totalRequest)
print("Total request made within the last ", timeFrame, " days: ", reqTimeFrame)
