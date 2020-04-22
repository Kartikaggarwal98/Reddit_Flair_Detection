import requests
import os

directory=os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(directory,'autotest_file.txt'), 'rb')
url = 'https://flairr.herokuapp.com/automated_testing'

files = {'file': file}
r = requests.post(url, files=files)

json_data = r.json()
print(json_data)