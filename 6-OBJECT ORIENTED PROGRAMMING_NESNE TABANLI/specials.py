mylist = [1,2,3]
mystring = "my str"
print(len(mylist))
print(len(mystring))

# class Movie():
#     pass
# m = Movie()
# print(len(m)) #dediğimiz zaman len çalışmaz çünkü movie artık python kütüphanesindeki metotları kullanamaz kendisi ayrı bir sınıftır sadece kendi içinde tanımlı olanları kullanabilir

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi oluşturuldu")
    
    def __str__(self): #normalde str yazdırınca string türünden değeri yazılır bu class olduğundan adresi filan yazacak ama biz yeni bir str fonksiyonu tanımlarsak istediğimiz şey yazılır
        return f"{self.title} adlı filmin  yönetmeni {self.director} süresi {self.duration}"

    def __len__(self): #python kütüphanesinde otomatik kayıtlı olan uzunluk bulma metodunu yaptığımız class için ayriyetten tanımlıyoruz ve istersek bunu bambaşka şeylerde bastırtabiliriz bize kalmış
        return self.duration #movie class için artık len metodu filmin süresini verir

    def __del__(self): #del objesi kullanılırken kullanıcı bu silinmeden bilgilendirilsin istersek diye tanımladık
        print("film silindi") #del objesi kullanılınca bunu bastıracak

me = Movie("film adı","yönetmen adı",198)
print(str(me))
print(len(me))

del me
print(me)