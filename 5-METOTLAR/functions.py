def sayHello(): #def fonksiyon oluşturma komutudur ve sonra fonkiyon ismi girilir
    print("Hello") #burada fonksiyon çağırılınca yapacağı gösterilir
sayHello() #fonksiyonu çağırırken direkt ismini yazmamız yeterli

def sayHello(name = "user"): #parantez içine kullanıcıdan değer alınabilir değere = yapıp bişey atayınca atanan şey kullanıcı değer girmediği zaman varsayılan olarak alınacak değerdir
    print("Hello" + name)
sayHello("çınar") #input değerini direkt fonksiyonu çağırırken parantezine yazılır

def sayHello(name = "user"): #parantez içine kullanıcıdan değer alınabilir değere = yapıp bişey atayınca atana şey kullanıcı değer girmediği zaman varsayılan olarak alınacak değerdir
    return "Hello" + name #birden çok fonksiyonu beraber kullanınca return yapmalıyız ki fonksiyonlar düzenli çalışsın yani sürekli bişey bastırmayabiliriz sadece fonksiyonda bişey hesaplayabiliriz başka bir fonksiyon için
msg = sayHello("çınar") 
print(msg) #illa bastırmak için dışarıda print yapılabilir

def toplama(ilks,ikis):
    toplama = ilks + ikis
    return toplama #eğer return kullanılmaz ise toplama fonksiyonu aşağıda çalıştırıldığın çalışır ancak sonucu adres olarak bellekte tutar yani bastırılmaya kalkıldığı zaman okuyamadığından none değeri verir 
                   #o yüzden aşağıda direkt bastırmak yerine önce fonksiyon sonunda return olarak gösterilecek sonuç belirlenir daha sonra bu sonuç print ile bastırılabilir

print(toplama(8,6))

def total(num1,num2): #ayrı ayrı birden çok değerde istenebilir çağırırken parantez içine aynı sıralamayla yazılır
    return num1 + num2
result = total(10,20)
print(result)


def yasHesapla(dogumyili):
    return 2022 - dogumyili

def Emekliligekacyilkaldi(dogumyili,isim):
    #burada fonksiyonu anlamayanlar için açıklama kısmı oluşturduk burayı aşağıda print help ile bastırarak bilgi sahibi olabiliriz. bu kısım her zaman def'den hemen sonra yazılmalıdır
    """ 
    DOCSTRİNG : dogum yiliniza göre emeklilige kac yil kaldi #fonksiyon hakkında genel bilgi
    INPUT : dogum yili #kullanıcadan istenen
    OUTPUT : hesaplanan yil #kullanıcıya verilecek bilgi
    """
    yas = yasHesapla(dogumyili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"emekliliğe {emeklilik} yıl kaldı {isim}")
    else:
        print(f"{isim} zaten emeklisiniz")

Emekliligekacyilkaldi(2002,"deniz")
print(help(Emekliligekacyilkaldi)) #help ile sadece yazılan fonksiyonun açıklama kısmındaki bilgi için değil normal class da hazır olan diğer metotlar içinde yardım alınabilir

###########

def çift_sayilari_filtrele(x): #daha profesyonel fonksiyon bu şekildedir bu fonksiyon girilen çiftleri sadece bastırır
    return x if x%2==0 else None #önce neyi döndüreceği sonra koşulu sonrada koşul sağlanmaz ise none yazdın yani hiç birşey demek aslında else hiç yazılmaz ise yine aynı şey olacak

