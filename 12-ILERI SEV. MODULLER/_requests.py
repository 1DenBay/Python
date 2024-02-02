import json
import requests 

# herhangi bir site kaynak görüntüle kısmında ki html kodlarından json bilgileri alır

result = requests.get("https://jsonplaceholder.typicode.com/")
result = json.loads(result.text) # sadece text gelen json bilgiyi yazdırır ancak loads modülü öğrenmiştik bilgiler str basılacağından text ile bunu dict'te çevirir 

print(result[0]["title"])#buşekilde de tek tek istediğimiz veriyi çekebiliriz
print(type(result))

for i in result: #tüm satırları bastırır
    print(i) #fordan sonra araya ifler ekleyerek filtre uygulayabiliriz

