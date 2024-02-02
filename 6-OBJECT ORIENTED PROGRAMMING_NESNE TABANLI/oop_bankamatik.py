from random import randint

class bankamatik():
    banka = "DENİZBANK" 
    şube = "BAĞCILAR"

    def __init__(self, adi, soyadi, dogum_tarihi, tcno, hesapno, bakiye):
        self.adi = adi
        self.soyadi = soyadi
        self.dogum_tarihi = dogum_tarihi
        self.tcno = tcno
        self.hesapno = hesapno
        self.bakiye = int(bakiye)
        self.fatura = {}
        self.egitim = {"YKS":50, "AÇIKÖGRETIM":20, "ÜNIVERSITE":40, "OKUL":20}
    
    def bakiye_sorgula(self):
        print(f"Sayın {self.adi} {self.soyadi} - {self.hesapno} Numaralı Hesabınızda {self.bakiye} $ Bulunmaktadır ")

    def kredi_notu(self):
        global kredi_not #global olarak kullandık diğer tüm fonksiyonlarda kullanılabilir parametre olarak ama önce method olarak çalıştırılmalı ki kredi_not değeri tanımlansın diğer fonskiyonda
        kredi_not = int(self.bakiye / 100)
        print(f"{self.adi} kredi notunuz {kredi_not}")

    def ekpara_al(self): #sınırsız ekpara alınabiliyor
        if (self.bakiye < 10.000):
            ekpara = 1000
            print(f"1000$ ekparanız hesabınıza tanımlanmıştır")
        else:
            ekpara = 3000
            print(f"3000$ ekparanız hesabınıza tanımlanmıştır")    
        self.bakiye += ekpara
        self.bakiye_sorgula()
        self.kredi_notu()

    def para_yatir(self):
        print(f"HOŞGELDİN {self.adi}")
        yatir = int(input("Yatırmak istedğiniz miktarı giriniz : "))
        self.bakiye += yatir
        print("paranız yatırıldı")
        self.bakiye_sorgula()
        self.kredi_notu()

    def para_cek(self):
        print(f"HOŞGELDİN {self.adi}")
        miktar = int(input("Çekmek İstediğiniz Miktarı Giriniz : "))
        if (miktar <= self.bakiye):
            print("PARANIZI ALINIZ")
            self.bakiye -= miktar
            self.bakiye_sorgula()
        else:
            print(f"Üzgünüz yetersiz bakiye")
            ekparaevet = input("ekpara kullanmak için 'e' tuşuna , Çıkış için herhangi bir tuşa basınız : ")
            if (ekparaevet == "e"):
                print(f"ekpara işlemleri başlatılıyor")
                self.ekpara_al()
                self.para_cek()
        self.kredi_notu()

    def kredi_cek(self):
        self.kredi_notu()
        print(f"HOŞGELDİN {self.adi}")
        tür = input("Hangi Kredi türünü istersiniz = KONUT(100k) , TAŞIT(40k) , İHTİYAÇ(20k)\n").lower()
        if (tür == "konut"):
            if (kredi_not >= 500):
                print("Krediniz onaylandı")
                self.bakiye += 100000
                self.bakiye_sorgula()
            else:
                print("kredi notunuz yetersiz olduğundan krediyi kullanamazsınız")
                tekrar = input("tekrar kredi türü seçmek için 'e' tuşuna , çıkış için herhangi bir tuşa basınız : ")
                if (tekrar == "e"):
                    print(f"kredi işlemleri başlatılıyor")
                    self.kredi_cek()

        if (tür == "taşıt"):
            if (kredi_not >= 250):
                print("Krediniz onaylandı")
                self.bakiye += 40000
                self.bakiye_sorgula()
            else:
                print("kredi notunuz yetersiz olduğundan krediyi kullanamazsınız")
                tekrar = input("tekrar kredi türü seçmek için 'e' tuşuna , çıkış için herhangi bir tuşa basınız : ")
                if (tekrar == "e"):
                    print(f"kredi işlemleri başlatılıyor")
                    self.kredi_cek()

        if (tür == "ihtiyaç"):
            if (kredi_not >= 150):
                print("Krediniz onaylandı")
                self.bakiye += 20000
                self.bakiye_sorgula()
            else:
                print("kredi notunuz yetersiz olduğundan krediyi kullanamazsınız ve Diğer kredilere notunuzdan dolayı başvuru yapamazsınız")
                ekparaevet = input("ekpara kullanmak için 'e' tuşuna , Çıkış için herhangi bir tuşa basınız : ")
            if (ekparaevet == "e"):
                print(f"ekpara işlemleri başlatılıyor")
                self.ekpara_al()

    def fatura_kayıt(self):
        fatura = input("Kayıt etmek istediğiniz fatura ismi giriniz : ").lower()
        tutar = randint(1,150) #fatura tutarı rastgele 150 ye kadar olacak
        self.fatura.setdefault(fatura,tutar) #setdefault dict için yeni elemanlar ekleme metodu
    
    def fatura_bilgi(self):
        if (self.fatura == {}): #yani dict boş ise
            print("Sistemde Kayıtlı faturanız bulunmamaktadır")
            self.fatura_kayıt()
        else:
            print(self.fatura)

    def fatura_öde(self):
        self.fatura_bilgi()
        self.fatura_bilgi()
        while True:
            öde = input("Ödeme yapmak istediğiniz faturayı yazınız : ").lower()
            if (self.bakiye >= int(self.fatura.get(öde))): #get dict metodudur ve girilen şeyin karşılığını verir
                self.bakiye -= int(self.fatura.get(öde))
                print(f"Seçtiğiniz fatura başarıyla ödenmiştir TEŞEKKÜRLER")
                self.bakiye_sorgula()
                self.kredi_notu()
                break
            else:
                print(f"Bakiyeniz yetersiz olduğundan işlem gerçekleştirilemedi")
                evet = input("ekpara almak için 'e' tuşuna , çıkış yapmak için herhangi bir tuşa basınız : ")
                if (evet == "e"):
                    self.ekpara_al()
                else:
                    print("İşlem sonlandırıldı")
                    break
    
    def egitim_ödemesi(self):
        print(f"{self.egitim}")
        while True:
            öde = input("Ödeme yapmak istediğiniz sınavı yazınız (türkçe karakter kullanmayınız!) : ").upper()

            if (öde not in self.egitim):
                print("Bu ödeme sistemimizde bulunmamaktadır! Lütfen listeyi tekrardan gözden geçirin")
                cik = input("Çıkış yapmak için 'c' tuşuna, devam etmek için herhangi bir tuşa basınız : ")
                if (cik == "c"):
                    break
                else:
                    continue

            if (self.bakiye >= self.egitim.get(öde)):
                self.bakiye -= self.egitim.get(öde)
                print(f"Sayın {self.adi}, {self.tcno} kimlik numarası ile yks sınav ücretiniz yatırılmıştır")
                self.bakiye_sorgula()
                self.kredi_notu()
                break
            else:
                print(f"Bakiyeniz yetersiz olduğundan işlem gerçekleştirilemedi")
                evet = input("ekpara almak için 'e' tuşuna , çıkış yapmak için herhangi bir tuşa basınız : ")
                if (evet == "e"):
                    self.ekpara_al()
                else:
                    print("İşlem sonlandırıldı")
                    break


    def kredi_ödemesi(self):
        pass

    def sans_oyunları_ödemesi(self):
        pass

    def hesap_olustur(self): #üst düzey kolaylık için
        pass

denizhesap = bankamatik("DENIZ", "BAYAT", "2002", "46474315847", "3462", 5) #hesap bu şekilde açılmaktadır
# denizhesap.bakiye_sorgula()
# denizhesap.kredi_notu()
# denizhesap.ekpara_al()
# denizhesap.para_yatir()
# denizhesap.para_cek()
# denizhesap.kredi_cek()
# denizhesap.fatura_kayıt()
# denizhesap.fatura_bilgi()
# denizhesap.fatura_öde()
denizhesap.egitim_ödemesi()
