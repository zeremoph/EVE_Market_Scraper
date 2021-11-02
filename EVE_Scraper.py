import requests
from datetime import datetime

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0 :D ) Gecko/20100101 Firefox/93.0', }

url = 'https://api.evemarketer.com/ec/marketstat/json?typeid=20&regionlimit=10000002'
url2 = 'https://api.evemarketer.com/ec/marketstat/json?typeid=1228&regionlimit=10000065'

x = requests.get( url, headers=headers)

y = requests.get(url2, headers=headers)
print(x.text)
print(y.text)

most = datetime.now()
ido = most.strftime("%d_%m_%Y_%H_%M_%S")
nev = str(ido)
file = open(nev + '.json', 'a')
file.write(x.text)
file.write(y.text)
file.close()
