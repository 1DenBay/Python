name = input("isim : ")
age = int(input("yaş : "))
education = input("eğitim : ")

if (age >= 18):
    print("yaşınız UYGUN")
else:
    print("yaşınız UYGUN DEĞİL")

if (education.lower() == "üniversite") or (education.lower() == "lise"):
    print("eğitiminiz UYGUN")
else:
    print("eğitminiz UYGUN DEĞİL")


y1 = int(input("1.YAZILI : "))
y2 = int(input("2.YAZILI : "))
s = int(input("SÖZLÜ : "))
ort = (y1+y2+s) / 3

if ( 0 <= ort <= 24):
    print("NOTUNUZ 0")
elif (25 <= ort <= 44):
    print("NOTUNUZ 1")
elif (45 <= ort <= 54):
    print("notunuz 2")
elif (55 <= ort <= 69):
    print("notunuz 3")
elif (70 <= ort <= 84):
    print("notunuz 4")
else:
    print("notunuz 5")


import datetime #kullanacağımız modülleri import etmemiz gerekir
tarih = input("trafiğe çıkış tarihi (year/month/day) : ") #önce str türünden bir tarih alacağız gün ay yıl şeklinde
tarih = tarih.split("/") #gün ay yılı tek tek çekmek için index no larına ayırdık
trafigecikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2])) #trafiğe çıkışını tarih türüne atadık ve tek tek sırasıyla gün-ay-yılı indexler ile eşleştirdik
simdi = datetime.datetime.now() #burası şimdiki tarihi yani anlık olarak bilgisayardan tarihi alacak yine tarih türünden indexlemeye gerek yok saten kendi içinden alacak tarih türünde olduğunu söyledik
fark = simdi - trafigecikis #datetime modülü kullandığımızdan tarih çıkartması yapar
days = fark.days #altta gün üzerinden hesap yaptık burdada .days ile direkt farkı güne çevirerek bize verir

if (days <= 365):
     print("1.servis aralığı")
elif (days > 365) and (days <= 365*2):
     print("2.servis aralığı")
elif (days > 365*2) and (days <= 365*3):
     print("3.servis aralığı")
else:
    print("hatalı süre 'sadece 3 senelik bilgi öğrenilebilir' ")





