#value type -> strings , numbers
a = 10
b = 20

a = b
b = 30

print(a,b)
#burada a ve b önce ayrı değerler verdik ve sonra birbirine eşitledik sonrada birisinin değerini değiştirince öteki değişmedi
#değişikliğin sadece birinde olmasının sebebi value type'ların direkt değeri tutması yani birbirinden bağımsız olmalarıdır

#--------------------------------------------

#reference type -> list , class(ilerideki derslerde)
x = ["banana","apple"]
y = ["banana","apple"]

x = y
y[0] = "grape" #sadece y deki 0 indexi değiştirdik

print(x,y)
#burada valueden farklı olarak eşitlikten sonra birini değiştirdiğimizde ötekide değişti mantık şöyle:
#value direkt değerleri tutuyordu ve birbirinden bağımsızdı ama referenceler liste olarak tanımlanınca listeler içindeki değerleri bir adres olarak tutarlar yani
#artık o listenin bir adresi olur ve o değerlerinde bir adresi olur ilk başta liste içinde aynı değerler olsa bile adresleri farklıydı yani bağımsızlardı ancak eşitlediğimiz zaman
#bundan sonra ikiside aynı adrese bağlandı ve birisinde yapılacak değişiklik direkt o adresteki değerlerde yapılacağından ötekide aynı adrese sahip olduğundan onun değerleri değişmekteydi
#burada amaç listede çok fazla derecede değer olunca bellekten tasarruf edip performans kaybını önlemek örneğin kopyalama yapınca bin değerlik listeyi sürekli bin değeri ordan oraya oraya tekrar tekrar
#çoğaltmak yerine sadece bin değerlik listeye bir adres veririz ve ulaşmak isteyen kopyalamak yerine o adrese gidince direkt orada bulur ve adres ile değerler farklı olduğundan performans kaybı olmaz.