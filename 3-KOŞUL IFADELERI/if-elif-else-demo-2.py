# num = float(input("sayi gir : "))

# if (0 < num <= 100):
#     print("sayi 0 ve 100 arasında")
# else:
#     print(" 0 - 100 arasında değil")


# num = float(input("sayi gir : "))

# if (num > 0) and ( num % 2):
#     print("sayı pozitif ve çift")
# elif (num > 0):
#     print("sayı pozitif")
# else:
#     print("sayı negatif")


# email = input("email : ")
# password = input("parola : ")

# if (email == "deniz@gmail.com") and (password == "123"):
#     print("GİRİŞ BAŞARILI")
# elif (email != "deniz@gmail.com") :
#     print("email hatalı")
# elif (password != "123"):
#     print("parola hatalı")
# else:
#     print("email ve parola hatalı")


# a = int(input("a : "))
# s = int(input("s : "))
# d = int(input("d : "))

# if (a > s) and (a > d):
#     print("en büyük a")
# elif (s > a) and (s > d):
#     print("en büyük s")
# elif (d > s) and (d > a):
#     print("en büyük d")


# v1 = int(input("1.VİZE notunu girin : "))
# v2 = int(input("2.VİZE notunu girin : "))
# f = int(input("FİNAL notunu girin : "))
# ort = ((v1+v2)/2)*0.6 + (f * 0.4)

# if (ort >= 50) and (f >= 50) or (f >= 70):
#     print("GEÇTİ")
# else:
#     print("KALDI")


name = input("İSİM : ")
kg = float(input("KİLO : "))
hg = float(input("BOY : "))
ind = kg / (hg**2)

if (0 <= ind <= 18.4):
    print("zayıf")
elif (18.5 <= ind <= 24.9):
    print("normal")
elif (25 <= ind <= 29.9):
    print("fazla kilolu")
elif (30 <= ind <= 34.9):
    print("şişman")
else:
    print("bilgileriniz yanlış")