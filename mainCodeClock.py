from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

def reader(filename):
  with open(filename) as f:
    log = f.read()
    print(log)
    
if __name__ == '__main__':
  reader('log')
