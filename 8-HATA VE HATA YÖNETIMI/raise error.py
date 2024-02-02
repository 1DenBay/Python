#raise error -> kendi uydurduğumuz hatalardır hata fırlatmak olarak geçer mesela kullanıcı makineye göre doğru birşey girdiğinde bile ancak bizim yazdığımız sisteme göre bize uymayan birşey ise o zaman uydurduğumuz error çalışır

x = int(input("sayı gir :"))
if x > 5:
    raise Exception("x 5'ten büyük olamaz") #raise x>5 olunca çalışacak ve ne hata gelirse gelsin parantezdekini basacak

##################################################

def check_password(psw): #kullanıcak parola alırken belirlediğimiz şartlar içerisinde parola oluşturması için kullanalım
    import re #re modülü girilen input için içeride aramak yapar search metodu sayesinde bizde girdiğimiz şartları kullanıcı sağlamışmı diye bu metodu kullanacağız
    if len(psw) < 8: #en az 7 karakterli parola olmalı
        raise Exception ("parola en az 7 karakter olmalıdır") #eğer değilse burada kendi yaptığımız hata atımını gerçekleştireceğiz
    elif not re.search("[a-z]",psw): #parolada a-z arasında ki harflerin aranması yapılır elif not dedik yani eğer bu harflerden yok ise yine hata fırlatacak hepsi aynı mantık alttakilerin , psw ise hangi eleman üzerinde çalışılacağı belirtilir
        raise Exception ("parola küçük harf içermelidir")
    elif not re.search("[A-Z]",psw):
        raise Exception ("parola büyük harf içermelidir")
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam içermelidir")
    elif not re.search("[_@$]",psw):
        raise Exception ("parola alpha numeric karakter içermelidir")
    elif re.search("\s",psw): #\s boşluk karakteri için kullanılır
        raise Exception ("parola boşluk içermemelidir")
    else: #eliflerin hepsi tamamlanınca çalışacak
        print("geçerli parola")

password = "1234562aA_"

try: #burada da fırlattığımız hataların hangisinin çalıştığını göstermesi için try bloğu kullandık
    check_password(password)
except Exception as ex:
    print(ex) #uyulmayan exceptionu basacak üstte yazdığımız şekilde printi ile birlikte
else: #hata yok ise
    print("geçerli parola: else")
finally: #her zaman çalışacak
    print("valiidation tamamlandı")


class Person: #direkt bir sınıf oluşturarak da bu işlemleri yapabiliriz
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:
            self.name = name

p = Person("aliiiiiiiiiiiiiiiiii", 1998)