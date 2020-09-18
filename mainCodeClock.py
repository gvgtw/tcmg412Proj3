from datetime import datetime
import urllib.request
import os

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

local_file, headers = urllib.request.urlretrieve(URL_PATH, LOCAL_FILE)



totalRequest = 0
reqTimeFrame = 0
with open(LOCAL_FILE) as f:
    for line in f:
        line = line.split(" ")
        if len(line) < 10:
            continue
        timestamp = datetime.strptime(line[3].replace("[", ""), "%d/%b/%Y:%H:%M:%S")
    print("This is a Test line: Spot #1")
   



print("Total request made within the log: ", totalRequest)
print("Total request made within the last 365 days: ", reqTimeFrame)
