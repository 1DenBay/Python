def changeName(n):
    n = "ada"
name = "deniz"
changeName(name) #burada deniz bastırılacaktır çünkü en başta n diye değişken tanımladık ve onun adresine ada yı koyduk
print(name) #daha sonra name diye değişken tanımladık onada denizi koyduk ikisi farklı adresler olduğu için değerlerde farklı olur ve yeni bir atama şeklinde olmaz farklı bir atama olur önceden gördüğümüz value - referance tipler gibi adresler farklı değerler farklı


def change(n): #bu fonksiyon herhangi bir listenin 0 indexini değiştirecek
    n[0] = "istanbul"
sehirler = ["ankara" , "izmir"]
change(sehirler) #burada value type lerden farklı olarak referance type kullanılacak yani en üstteki örnek gibi farklı bir adres yani orjinal kopya olarak tutulmuyor direkt aynı adres yani orjinal verinin üstüne değişiklik yapılıyor
print(sehirler) #direkt ankara yerine istanbul yazdıracak
n = sehirler[:] #burada : diyerek sehirlerde ki elemanları n ye aktar demektir bu slicing işlemidir
print(n) #sehirleri değiştirme komutu üstte olduğundan yine n değişkeni istanbullu olanı basacak ama üstte olmasaydı direkt ankaralı basacaktı


def add(a,b): #bazen de 3 parametreli çalıştırmak için birde c parametresi ekle ve = 0 yap
    return sum((a,b)) #sum class içerisinde yani builtin olarak gelen toplama işlemi yapan bir fonksiyon
print(add(10,20))

def add(*params): #sınırsız parametre için böyle yapılır
    print(params) #bu şekilde tüm parametreleri tuple içinde görebiliriz ve ek bilgi olarak fonksiyon içinde params diye bir değişken tanımladık bunu biz uydurduk bu params sadece fonksiyon içinde tanımlıdır yani örneğin fonksiyon dışında params değişkenini bastıramazsın tanımlı olmadığından
    return sum((params))
print(add(10,20,50,60,80,70,52))


def displayUser(**args): #üstteki tuple olarak alınmıştı ancak burada iki yıldız (**) koyduğumuzdan dictionary olarak alacaktır 
    for key,value in args.items(): #args içinden itemleri key ve value olarak tek tek atıyacaz
        print(" {} is {}" .format(key,value)) #girilen bilgileri düzenli olarak bastıracak

displayUser(name = "deniz" , age = 2, city = "istanbul", phone = "1236198")


def myfunc(a,b,*args,**kwargs): #toptan değerler atanabilir sırayla herkes kendine uygunsa değer otomatik alır
    print(a) #üstte a yı tek bir değer alacak şekilde tanımladık o yüzden direkt ilk değeri alır
    print(b) #a ile aynı şekil 2. değeri alır
    print(args) #yukarıda args tuple olarak tanımlandığından a ve b değerleri aldıktan sonra kalan tüm değerleri alır ancak ondan sonra dictionary geldiğinden oraya kadar alabilir
    print(kwargs) #dictionary olarak tanımlandığından key = value şeklinde olan değerleri alır
myfunc(10,20,30,40,50, key1="value1" , key2="value2")