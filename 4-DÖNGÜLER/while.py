# while "iken" anlamı katar

x = 1
while x <= 100: # x küçük eşittir 100 iken çalış demektir yani x 100 olana kadar kod bloğunu komple çalıştırır 
    if (x % 2 == 1): 
        print(f"sayı tek : {x}")
    else:
        print(f"sayi çift : {x}")
    x += 1 #sonsuz döngü olmaması için her döngüden sonra x e adım sayısı yani 1er 1er verdik


name = "" #false anlamına gelir dikkat boşluk değil hiç bişey girilmemiş anlamı taşıyor
while not name.strip(): #not name koymamızın sebebi isim girmediği sürece false döndürecek saten while false olduğu sürece çalışacağından sürekli isim isteyecek strip kullancık çünkü boşluk girilmesin diye
    name = input("isim gir: ")
print(f"merhaba , {name}")
