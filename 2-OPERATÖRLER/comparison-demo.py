a = int(input("Bir sayi giriniz : "))
b = int(input("Bir sayi daha giriniz : "))
result = (a > b)
print(f" a: {a}  b: {b}'den büyüktür : {result} ")

v1 = float(input("1.Vize Notunuzu Giriniz : "))
v2 = float(input("2.Vize Notunuzu Giriniz : "))
f = float(input("Final Notunuzu Giriniz : "))
ort = (((v1+v2)/2) * 0.6) + (f * 0.4)   
print(f"Ortalamanız {ort} ve Dersten Geçme Durumunuz: {ort>=50}") #direkt koşulu formatlı print içinede yazabiliyoruz

a = int(input("Bir sayi giriniz : "))
tekcift = (a % 2 == 0) # a 2ye kalansız bölünüyor mu
print(f"girilen sayının çift durumu : {tekcift}")

a = int(input("Bir sayi giriniz : "))
pozneg = (a >= 0)
print(f"sayının pozitif olma durumu : {pozneg}")

email = "deniz@gmail.com"
password = "1234"
email0 = input("Email adresinizi giriniz : ")
password0 = input ("Parolanızı giriniz : ")
emailt  = (email0 == email) #büyük küçük önemsiz ise email ' in sonuna .lower koyulabilir ve stripde koyulabilir boşlukları silsin diye
passwordt = (password0 == password)
print (f"Email doğruluk : {emailt} - Parola doğruluk {passwordt}")
