#1 .YÖNTEM (her modül için geçerli)

import math #math import ettik artık kullanabiliriz
import math as islem #burada math modülüne islem diye takma isim verdik artık math modülünü "islem" diye çağırabiliriz
value = dir(math) #dir komutu bir modülün içindeki bileşenleri görmek içidir
value = help(math) #help komutu bileşenleri detaylıca anlatır kullanımını filan
value = help(math.factorial) #direkt istenilen bileşen hakkınada gidilebilir - factorial burada math modülü içindeki bir bileşendir
value = math.sqrt(5) #bileşenler bu şekilde çalıştırılır

print(value)

########################

#2 .YÖNTEM (her modül için geçerli)

from math import * # mathdan al *(tüm bileşenleri alır) yada yerine tek tek kullanılacak bileşenler yazılır bunun güzel yanı bileşenleri kullanırken artık math.sqrt gibi çağırmayız direkt sqrt yazabiliriz
# mesela math da olan bir fonksiyonun aynı isimlisinden bizde burada tanımlarsak sistem en son hangisi tanımlanmış ise onu baz alacaktır

value = sqrt(6)
print(value)

##########################################################

import random

value = random.random() #direkt 0-1 arasında rastgele float değerler üretir
value = random.random() * 100 #yanına istediğimiz gibi işlemlerde ekleyebiliriz
value = random.uniform(1,10) # 1-10 arası float değerler üretir bu float sayıyı int parantezine alıp ondalık kısmı yok edilebilir
value = random.randint(1,100) #1-100 arası direkt tam sayı int üretir

names = ["ali","deniz","yağmur"]
result = names[random.randint(0,len(names)-1)] #listeden rastgele eleman seçimi için 0 dan eleman sayısı kadar rastgele sayı üretip bastırır
result = random.choice(names) #bu metot üstteki karışık kodların kolay yoludur yani direkt liste elemanları içinden rastgele seçer

liste = list(range(10)) #(range10) - 0 dan 9 a kadar sırayla liste oluşturur
random.shuffle(liste) #shuffle seçilen liste içindeki elemanları rastgele karıştırır
result = liste

liste = range(100)
result = random.sample(liste,3) #listeden rastgele istenen kadar eleman getirir

print(result)
