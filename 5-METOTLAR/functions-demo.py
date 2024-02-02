def yaz(kelime,adet): #girilen kelimeyi girilen adet kadar yazdır
    print(kelime * adet)
yaz("merhaba\n",10)


def listcev(*args): #girilen sınırsız sayıdaki değişkeni listele demektir başına * koymak
    list = []
    for arg in args:
        list.append(arg)
    return list
result = listcev(10,20,30,"merhaba")
print(result)


def asalbul(s1,s2): #girilen 2 sayı arasındaki asalları bulma
    for i in range(s1,s2):
            if s1 > 1:
                for i in range(2,s1):
                    if (s1 % i == 0):
                        break
                else:
                    print(s1)
            else:
                print("1'den büyük sayi giriniz")
    s1 = int(input("sayı 1 : "))
    s2 = int(input("sayı 2 : "))
    asalbul(s1,s2)


def bölenler(s1): #girilen sayının tam bölenlerini bulma
    for i in range(1,s1):
        if (s1 % i == 0):
            print(i)
s1 = int(input("sayı 1 : "))
bölenler(s1)
