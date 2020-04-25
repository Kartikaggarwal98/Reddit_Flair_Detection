import requests
import os

directory=os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(directory,'file.txt'), 'rb')
url = 'https://flairr.herokuapp.com/automated_testing'

# files = {'upload_file': file}
# (2018) The new python requests library has been updated, the 'upload_file' parameter is now 'file' parameter

files = {'file': file}
r = requests.post(url, files=files)

json_data = r.json()
print(r)