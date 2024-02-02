#methotlarda ne olursa olsun sonuna () koyulmalı

message = "Hello There. My name is Sadık Turan"

message = message.upper() #Tüm harfleri büyük yapar
message = message.lower() #Tüm harfleri küçük yapar
message = message.title() #Sadece kelimelerin baş harfleri büyütür
message = message.capitalize() #Sadece cümle başını büyük yapar gerisini küçültür
message = message.strip() #Cümle başında boşluk varsa onu siler bu şifre alırken yararlıdır
message = message.split() #Birşey yazmadığımız için paranteze cümleyi boşluklardan bölecek ve her kelime bir karakter dizisine dönüşecek 0dan itibaren her kelimenin index no oluşur
message = message.split(".") #noktalardan itibaren ayırır
message = " ".join(message) #split ile ayırdığımızı tekrar birleştirir önünde ki tırnak içine de birleşim yerlerine ne geleceğini yazarsın split kullanmadan direkt kullanırsan harflerin arasına yazdığını koyar
message = message.count("i") #burada count içindeki karakterden kaçtane var onu sayar

index = message.find("Sadık") #cümle içerisinde arama yapmamızı sağlar ve bize ilk harfinin index nosunu verir
print(index) #o index nosunu yazdırdık görmek için negatif sayı gelirse öyle bişey yok

isFound = message.startswith("H") #Cümlenin H ile mi başladığını soruyoruz
isFound = message.endswith("n") # Bu da bittiği harfi kontrol eder
print(isFound) #cevabı görmek için true yada false

message = message.replace("Sadık" , "Çınar") #değiştirme methodudur ilk baştaki yerine ikinciyi yazar
message = message.center(50) #ortalama yapar yani parantezdeki sayı kadar alana kelimeyi ortalar

print(message)
print(message[1]) #split için örnek