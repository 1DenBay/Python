a = int(input("Bir sayı giriniz : "))
result = (a > 0) and (a < 100)

result = (a > 0) and (a % 2 == 0)

email = "deniz@gmail.com"
password = "123"
email1 = input("email : ")
password1 = input("parola : ")
result = (email == email1) and (password == password1)

a = int(input("a giriniz : "))
s = int(input("s giriniz : "))
d = int(input("d giriniz : "))
abüyük = (a > s) and (a > d)
sbüyük = (s > a) and (s > d)
dbüyük = (d > a) and (d > s)
print (f"en büyük a : {abüyük} , en büyük s {sbüyük} , en büyük d {dbüyük}")

v1 = float(input("1.Vize Notunuz: "))
v2 = float(input("2.Vize Notunuz: "))
f = float(input("Final Notunuz: "))
ort = ( (((v1 + v2)/2)*0.6) + (f * 0.4) )
gecti = (ort >= 50) and (f > 50) or (f >= 70)
print(f"Geçme Durumu : {gecti}")

isim = input("İSİM : ")
kilo = float(input("KİLO : "))
boy = float(input("BOY : "))
ind = kilo / (boy**2)
z = 0 <= ind <= 18.4
n = 18.5 <= ind <= 24.9
k = 25 <= ind <= 29.9
s = 30 <= ind <= 34.9
print (f"Zayıf : {z} - Normal : {n} - Kilolu : {k} - Şişman : {s} ")