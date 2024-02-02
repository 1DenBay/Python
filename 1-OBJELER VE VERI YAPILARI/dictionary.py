# Özetle -> key : value 
# kocaeli -> 41 , istanbul -> 34 götürsün istiyoruz

sehirler = ["kocaeli", "istanbul"]
plakalar = [41 , 34]
print(plakalar[sehirler.index("kocaeli")]) #burada bize sehirlerde kocaeli indexi bul ve plakalarda o indexdeki no yu yazdır
# burada ki sıkıntı sehirle ile plakalar aynı sırada yani aynı indexte olmalı bu uğraştırır

plakalar = { "key" : "value" } #bütün meselenin özeti ve kısası süslü içinde yaz

plakalar = { "kocaeli" : 41 , "istanbul" : 34} #tek tek karışıklık olmadan anahtar ile değerleri var
print(plakalar["kocaeli"]) #bu şekilde kısaca bastır
print(plakalar["istanbul"]) 
plakalar["ankara"] = 6  #yeni keyler atayabiliriz
plakalar["kocaeli"] = "new value" #yada olan keylerin valuelerini değiştirebiliriz
print(plakalar)

# şimdi daha karmaşık yani tek key ile birçok bilgiye ulaşabildiğimiz yada direk o keyin hangi bilgisini istiyorsak ona ulaşabildiğimiz sistem yapalım
users = {
    "denizbayat" : { #süslü içinde keye value atarken birçok value atamak için key ede :'den sonra bir süslü aç
       "age" : 20,  #bunlar alt kümelerdir yani keyin valuesidir aynı zamanda age gibi olanlar da bir keydir
       "roles" : ["admin" , "user"], #her valueden sonra virgül ve bir keyin birden fazla valuesi var ise köşeli parantez al
       "email" : "deniz@gmail.com",
       "phone" : "1561819"
    } , 
    "asd" : {
       "age" : 19,
       "roles" : "user",
       "email" : "asd@gmail.com",
       "phone" : "1891992"
    }
}

print(users["denizbayat"]) #direkt denizbayat yazınca bilgileri çıkıyor
print(users["asd"]["age"]) #yada direkt alt kümelerde ki valuelerede ulaşabiliriz
print(users["denizbayat"]["roles"][0])
