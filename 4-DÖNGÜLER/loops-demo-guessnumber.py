import random

sayi = random.randint(1,10)
can = int(input("can gir : "))
hak = can
sayac = 0
while (hak > 0):
    hak -= 1
    sayac +=1
    tahmin = int(input("TAHMİN : "))
    if (hak == 0):
        print("canınız bitti")
        break
    if (sayi == tahmin):
        print(f"TEBRİKLER {sayac} TAHMİNDE BİLDİNİZ PUANINIZ = {100 - ((100/can) * (sayac-1))}")
        break
    elif (tahmin < sayi):
        print("yukarı")
    else:
        print("aşağı")

