numbers = [1,2,3,4,5] #liste
for a in numbers: #for döngüsü burada "numbers içindekileri a değişkenine at" işini yapar tek tek atarken her seferinde for kod bloğunu çalıştırır
    print("hello") #for 5 eleman var ve 5 kere atama yapacağı için 5 kere dönecek böylece 5 kere hello basar

names = ["çınar" , "sadık" , "deniz"]
for name in names: #burada yine aynı tek tek sırayla names listesindekileri name içine atar
    print(f"my name is {name}") #başka şeyde basabilirsin en üstteki gibi ama sırayla name içine attığından kullanada biliriz

name = "deniz bayat"
for n in name: #string de bir karakter dizisi olduğundan aynı görevi görür
    print(n)

tuple = (1,2,3,4,5)
for t in tuple: #yine liste gibi tek tek bastırır her elemanı ayrı ayrı
    print(t)

tuple = [(1,2),(1,3),(3,5),(5,7)] #liste tanımlayıp içinede bölüm bölüm yapınca ayrılabilir
for a,b in tuple:  #burda mantık virgülü baz alarak çalışır yani her parantez içindekini virgülden öncekini a'ya (çünkü for döngüsünde atama yapılacak karakter a,b diye yazdık virgülden önce a var) yine aynı mantık virgülden sonraki değerlerde b ye atanır sırayla
    print(a) #burada da ister ayrı ayrı sadece virgülden önceki değerleri sonraki değerleri yada direkt ikisinide bastırabiliriz


d = {"k1":1, "k2":2, "k3":3}
for item in d: #dediğimizde sadece key bilgilerini alır
    print(item)

for item in d.items(): #items metodu bu şekilde bastır yaparsak komple key,value şeklinde komple eleman grubunu alır parantezli şekilde bastırır sebebi virgülsüz tek kelimelik bir değişkenin içine atıyor olduğumuzdan
    print(item) 

for key,value in d.items(): #burada ise d.items ile eleman grupları şekline koyduk yani yukarıda ki gibi parantezli sonrada yine virgüle göre key,value diye tanımladık
    print(key,value) #items metodu ile key value şeklinde aldık şimdi burada da virgülden önce sonra yada komple olarak bastırabiliriz