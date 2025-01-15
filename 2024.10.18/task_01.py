import requests

url = 'http://api.forismatic.com/api/1.0/'
payload  = {'method': 'getQuote', 'format': 'json', 'lang': 'ru'}
res = requests.get(url, params=payload)

data = res.json()

print(data)