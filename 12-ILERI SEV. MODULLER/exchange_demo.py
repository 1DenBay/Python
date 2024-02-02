#ÇALIŞMIYOR SİTE DEĞİŞMİŞ

import requests
import json

api_url = "https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"

payload = {}
headers= {
  "apikey": "BUFL7TbggDTtNzwm4LFcpIpfD8FFbS0W"
}

response = requests.request("GET", api_url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

bozulan_döviz = input("bozulan döviz : ")
alinan_döviz = input("alinan döviz : ")
miktar = int(input(f"ne kadar {bozulan_döviz} bozdurmak istiyorsunuz : "))

result = requests.get(api_url+bozulan_döviz)
result = json.loads(result.text)

print(result)

