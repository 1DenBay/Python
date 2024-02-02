#class yapısının en büyük özelliği yapılan işlemleri hatırlaması ve diğer işlemleri geçmişteki yapılmış işlemlerin üzerine yani güncelleyerek yapması

class Person: #class tanımladık isminin baş harfini büyük yaparız okunmayı kolaylaştırması için
    #pass #tanımlama yaptıktan sonra bişeyler yazmamız gerekir eğer yazmak istemiyorsak pass metodu kullanabiliriz bu pass mesela if filan oluşturduğumuzda da kullanılabilir

#attributes -> class içine yaptığımız tanımlamalardır bu tanımlamalar class seviyesi ve object seviyesi olarak ikiye ayrılır + attributes kısaca class içindeki şeyin değişmeyen özellikleridir
    #class attributes yani genel olarak global seviyede tanımlamalar yani heryerde geçecek seviyede tanımlamalardır
    address = "no information"
      
    #metodlar init fonk. ile ifade edilir ve class içinde ki şeyin değişen ona özel özellikleridir bunları self, den sonra tek tek parametlerin isimleri girilir - self bütün metotları birbirine bağlamak aynı çatıda toplamak için kullanılır
    #contructor(yapıcı metod) -> metodlar attributesleri de genellikle kullanarak yapılan yada değişen özelliklerdir bi nevi fonksiyonlardır hesaplama falan filan
    def __init__(self,name,year): #constructor için bir fonksiyon tanımlamamız gerek init ile init parametresi(self) aşağıda tanımladığımız objelere(p1gibi) karşılık gelir illa self olmak zorunda değil istediğin şeyi yaz ancak ilk parametre olmalı ki altta tanımladığımız p1 gibi objelere karşılık gelsin - kısaca clası çağırırken paranteze gireceğimiz parametreler tanımlanır 
        #object attributes -> objeler constructor içinde tanımlanır ve değişken özelliklerdir
        self.name = name #üstte tanımladığımız parametreleri kullanıcıdan da alabiliriz ve bu şekilde aynı şeye eşitlememizin sebebi ileride çağırırken kolaylık olması (classismi.objeattributes)
        self.year = year 
        print("init metodu çalıştı")

        #instance methods -> buda yine atributes gibi yukarıdan alınan bilgileri farklı farklı şekillerde içine yazılan şekillerce kullanır ve bildiğin fonksşyondur
    def intro(self): #init metodunda tanımlanan ilk parametre, introyu kafadan yazdık kendin isim ver karışıklık olmayacak şekilde ve yine self kullanmamızın sebebi yukarıda oluşturunlan attributes ve class hakkında işlem yaptığını gösterir
        print("hello there. i am " + self.name)

    def calculateAge(self):
        return 2019 - self.year

# #object(instance)
# p1 = Person(name="ali",year=1990) #p1 objesi oluşturduk ve bu objeyi persona tanımlayıp parantez içine bişey yazınca person classtan birşeyler çekebileceğiz
# p2 = Person("deniz",1882) #üstteki gibi name ve year koyarakda yapabiliriz okunabilirlik kolaylaşır yada direkt böylede yapabiliriz

# #updating arada değişkenleri değiştirebiliriz en üstteki init metodundan alınan değişkenleri
# p1.name = "ahmet"

# #accessing object attributes
# print(f"p1 name: {p1.name} - p1 year: {p1.year} - address:{p1.address}")
# #print(p1) #direkt yazdırınca bize hangi class da olduğunuz ve bunun adresini verir her object farklı adreslere sahiptir

# #object(instance)
p1 = Person("deniz",1995,)
p2 = Person("ali",1885)
p1.intro()
p2.intro()
print(f"yaşım: {p1.calculateAge()} - yaşım: {p2.calculateAge()}")

#####################

class Circle:
    #class object attributes
    pi = 3.14 #ortak bir değer olduğundan tek tek hepsine girmemek için class seviyesinde tanımladık 

    def __init__(self,yaricap=1): #esittir 1 yapınca eğer değer verilmez ise otomatik 1 alır
        self.yaricap = yaricap #karışıklık olmasın diye yine aynı ismi veririz
    
    #methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    
    def alanhesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle() #yaricap=1 alır bişey girmediğimizden
c2 = Circle(5)

print(f"c1 : alan = {c1.alanhesapla()} - cevre = {c1.cevre_hesapla()}")
print(f"c2 : alan = {c2.alanhesapla()} - cevre = {c2.cevre_hesapla()}")

#özetle en başta class tanımlanır bunu bir dünya gibi düşün buraya tüm dünyada geçerli olan değişmeyecek bilgiler girilir
#sonra tanımlanan init ise bölge gibi düşün buradan yapılacak işlemler için gerekli bilgiler alınır yada sonradan classı çapırırken parametre olarak girilir
#inite hizmet eden diğer methodlarda ülke gibidir initte alınan değerler ve tüm dünya için girilen class daki değerleri kullanarak hepsine kendine özgü birşeyler hesaplatılır
#başına ve sonuna "__" ile yazdığımız fonksiyonlar parantezsiz direkt ismi yanınada değişken şeklinde çalışır
#clası tanımladıktan sonra init hariç birçok instance method dediğimiz bildiğimiz fonksiyonlar tanımlayabiliyoruz aynı zamanda python içinde kütüphaneden otomatik gelen bazı methotlarda vardır
#bir clas içindeki methodlara clasismi.__dir__() şeklinde yazdığımızda görebiliriz burada hem bizim tanımladığımız class attributeslerden itibaren hepsi hemde kütüphanede oto gelen methotlar var 