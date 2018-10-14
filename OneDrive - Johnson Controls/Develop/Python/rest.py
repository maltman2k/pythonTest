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


i = 1
proxyEnabled=0;

try:
    response = requests.get('https://sisedemos.ddns.net:9090/services/ede/items/Room Temperature/value', proxies=proxies,verify=False,headers=headers)
except IOError:
    proxyEnabled=1;
finally:
    print ("success")

while i < 5:
    if proxyEnabled==0:
        response = requests.get('https://sisedemos.ddns.net:9090/services/ede/items/Room Temperature/value', proxies=proxies,verify=False,headers=headers)
    else: 
        response = requests.get('https://sisedemos.ddns.net:9090/services/ede/items/Room Temperature/value',verify=False,headers=headers)
        
    y = json.loads(response.text)
    print (y[u'item'][u'value'])
    time.sleep(2)
    i += 1
print ("end process execution")

