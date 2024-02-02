class Ucus():
    havayolu = "DENIZAIR"

    def __init__(self, ucak, kalkis, varis, kalkissaat, inissaat, kapasite, yolcu):
        self.ucak = ucak
        self.kalkis = kalkis
        self.varis = varis
        self.kalkissaat = kalkissaat
        self.inissaat = inissaat
        self.kapasite = kapasite
        self.yolcu = yolcu
    
    def __repr__(self):
        print(f"{self.ucak} sefer sayılı uçuş oluşturulmuştur ")

    def anons(self):
        print(f"{self.ucak} SAYILI UÇAĞIMIZIN {self.kalkis} - {self.varis} UÇUŞUNA HOŞGELDİNİZ")

    def koltuk_guncelle(self):
        return self.kapasite - self.yolcu

    def bilet_satis(self):
        bilet_adedi = int(input("Satılacak bilet adedini giriniz : "))
        if (self.yolcu + bilet_adedi <= self.kapasite):
            self.yolcu += bilet_adedi
            self.koltuk_guncelle()
            print(f"{bilet_adedi} Adet Bilet Satılmıştır Kalan Boş Koltuk Sayısı {self.koltuk_guncelle()}")
        else:
            print("İşlem Gerçekleştirilemedi, Yetersiz Koltuk Sayısı")
            
    def bilet_iptal(self):
        while True:
            bilet_adedi = int(input("İptal Edilecek bilet adedini giriniz : "))
            if bilet_adedi <= self.yolcu:
                self.yolcu -= bilet_adedi
                print(f"{bilet_adedi} tane biletiniz iptal edilmiştir")
                self.koltuk_guncelle()
                print(f"{bilet_adedi} Adet Bilet İptal edilmiştir Kalan Boş Koltuk Sayısı {self.koltuk_guncelle()}")
                break
            else:
                print("Lütfen doğru iptal adedi giriniz")
                cikis = input("Tekrar iptal işlemleri için 'd' tuşuna , çıkış için herhangi bir tuşa basınız : ")
                if (cikis == "d"):
                    print("İşlem yeniden başlatıldı")
                else:
                    break

ucus1 = Ucus("DNZ223", "ANK", "İST", "21:30", "24:00", 250, 150)
ucus1.anons()

