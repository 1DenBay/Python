#tüm error türlerine python.org - docs - builtin exception ' dan ulaşılabilir

# error handling -> hata yönetimi


try: #hatalara karşı önlem bloğudur , normal çalışacak şeyleri altına yaz , except iset try bloğundan hata gelirse ne yapılacağı yazılır
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)
except (ZeroDivisionError,ValueError) as e: #hangi hataların gelebileceğini yazdık ve "e" diye takma isim yaptık bunlara genel olarak rahat kullanım için yani hangi hata gelirse "e" diye tanımlı
    print("yanlış bilgi girdiniz") #hata gelince çıkacak metni yazdırır
    print(e) #hangi hata olduğunuz bastırır


try: #blok direkt bu şekilde sade de çalıştırılabilir {sade hali}
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)
except: #ancak burada hangi hata olduğunu tespit edemeyiz sadece hata olduğunu ve hata olunca ne bastırılacak onu tespit ederiz
    print("yanlış bilgi girdiniz")


while True: 
    try:
        x = int(input("x : "))
        y = int(input("y : "))
        print(x/y)
    except Exception as ex: #Exception metodu direkt gelecek tüm hatalar için kolay kullanım sağlayan metotdur ve bizde bu hatalara ex takma ismi takalım
        print("yanlış bilgi girdiniz" , ex) #hata gelince hem metin hem de hangi hatanın olduğunu basacağız
    else: #else sadece except fonksiyonu için çalışır yani excepti if gibi düşün except çalışmaz ise else çalışacaktır
        break #while den çıkar bunun yerine direkt tryın en altınada break koysaydık aynı şeyi gelecekti
    finally: #bu fonksiyon ise her seferinde çalışır yani hata olsada olmasada amacı birden çok try fonks. olduğundan karışıklığı önlemek ve hangi tryların çalıştığını tespit etmek
        print("try except sonlandı")
