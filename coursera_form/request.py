import requests
from requests.auth import HTTPBasicAuth

url = 'https://datasend.webpython.graders.eldf.ru/submissions/1/'

r = requests.post(url, auth=HTTPBasicAuth('alladin', 'opensesame'))
print(r.text)

url1 = 'https://datasend.webpython.graders.eldf.ru/submissions/super/duper/secret/'

r = requests.put(url1, auth=HTTPBasicAuth('galchonok', 'ktotama'))
print(r.text)

