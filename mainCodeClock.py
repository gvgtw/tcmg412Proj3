from datetime import datetime
import urllib.request
import os

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)


totalRequest = 0
reqTimeFrame = 0
def reader(filename):
    with open(filename) as f:
        log = f.read()
        for log in f:
            #timestamp = datetime.datetime.strptime(line.strip(), '[%d/%b/%Y:%H:%M:%S %z]')
            print(log)
   



print("Total request made within the log: ", totalRequest)
print("Total request made within the last 365 days: ", reqTimeFrame)
