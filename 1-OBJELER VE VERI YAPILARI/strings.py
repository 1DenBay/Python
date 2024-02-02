name = "Deniz"
surname = "Bayat"
age = 36

greeting ="My name is "+ name + " "+ surname + "and \nI am "+ str(age) + "years old"
# ters \n alt satıra geçiş sağlar
# tanımlamalarda her string ifade bir index sayılandırmasına karşılık gelir yani 0dan sırayla hepsinin no ları vardır sondan başlayınca da -1 den başa doğru azalarak gelir

print(len(greeting)) #len komutu bize içindeki ifadenin kaç karakter olduğunu gösterir
lenght = len(greeting) #yada direkt böyle bişey de tanımlayabiliriz karakter sayısı için
print(greeting[lenght-1]) #direkt bu şekilde sonuncu terim bastırılabilir yada direkt alta bak
print(greeting[-1])
print(greeting[5]) #bu şekilde köşeli parantez kullanırsak o ifadede ki indexe karşılık gelen terimi bastırır

print(greeting[3:7]) #iki nokta ifadesi aralık ifade eder 3 hariç 7 dahil olacak şekilde aralarda ki terimleri bastırır , başlangıç yada bitiş yazmaz ise sonuna kadar gider
print(greeting[2:40:2]) #yine aynı şekil sadece sonda ki iki nokta adım sayısını gösterir son terim adım sayısıdır

