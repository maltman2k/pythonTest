import requests
import json
import time
import warnings


warnings.filterwarnings("ignore")

proxies = {
  'http': '165.225.86.36:10319',
  'https': '165.225.86.36:10319',
}
headers = {'accept' : 'application/json'}
#url = 'https://sisedemos.ddns.net:9090/services/ede/virtualdevices/1'
#response = requests.get('http://jsonplaceholder.typicode.com/todos/1', proxies=proxies,verify=False)
#response = requests.get('https://sisedemos.ddns.net:9090/services/ede/virtualdevices/1/items/Room Temperature/value', proxies=proxies,verify=False,headers=headers)

i = 1
while i < 5:
  i += 1
  response = requests.get('https://sisedemos.ddns.net:9090/services/ede/items/Room Temperature/value', proxies=proxies,verify=False,headers=headers)
  y = json.loads(response.text)
  print (y[u'item'][u'value'])
  time.sleep(2)
print ("end process execution")

