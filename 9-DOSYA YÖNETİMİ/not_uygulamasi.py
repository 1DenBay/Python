def not_goster():
    with open("notlar.txt", "r", encoding="utf-8") as file:
        print(f"\n{file.readline()}")

def not_kayit():
    with open("notlar.txt", "a", encoding="utf-8") as file:
        isim = input("Öğrencinin İsmini Giriniz : ")
        soyisim = input("Öğrencinin Soyismini Giriniz : ")
        not1 = int(input("1.Notu Giriniz : "))
        not2 = int(input("2.Notu Giriniz : "))
        not3 = int(input("3.Notu Giriniz : "))
        file.write(f"{isim} {soyisim} : {not1},{not2},{not3}\n")

def ortalama_goster():
    with open("notlar.txt", "r", encoding="utf-8") as file:
        list = file.readline()
        print(list[0])

def not_guncelle():
    pass


while True:
    menu = input("1- Not Göster\n2- Not Kayıt Et\n3- Not Güncelle\n4- Ortalama Göster\n5- Çıkış\n")
    if (menu == "1"):
        not_goster()
    elif (menu == "2"):
        not_kayit()
    elif (menu == "3"):
        not_guncelle()
    elif (menu == "4"):
        ortalama_goster()
    else:
        print("Çıkış Yapıldı")
        break  