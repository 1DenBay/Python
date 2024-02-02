import json

# diğer dillerde de olan cihazlar arası veri taşımayı sağlayan modüldür
# dictionary yapısı kısmen json yapısına benzer

#dict yapısıdır burada komple str türünde değildir sadece anahtar ve değerler str şeklindedir
# person = {"name" : "ali", "languages" : ["python","C#"]}{"name" : "ali", "languages" : ["python","C#"]}
# result = person["languages"][0] 

# json yapısında ise dict aynısı ancak komple str türünde
person_string = '{"name" : "ali", "languages" : ["python","C#"]}'

# load -> dict'e çevirme
# result = json.loads(person_string) #dict türüne çevirir
# result = result["name"] #bu dict yöntemi kullanılar bilir çünkü üstte dict türüne çevirdik
# with open("person.json") as f: #dict farklı dosyada olsa bile çekebiliriz
#     data = json.load(f)
#     print(data["name"])

# dump -> json'a yani strye çevirme
person_dict = {"name":"ali" , "languages":["python","C#"]}
# result = json.dumps(person_dict)
# with open("person.json","w") as f: #dosya oluşturup içine dict'i str şeklinde atabiliriz 
#     json.dump(person_dict, f)

person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent=4, sort_keys=True) #indent süslü p. sonra kaç karakter boşlukla başlıyacağı , sort keyde alt alta olması

print(result)
print(person_dict)

################################# DEMO

