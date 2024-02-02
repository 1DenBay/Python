name = "Deniz"
surname = "Bayat"
age = 20
 
# print("My name is {} {}" .format(name, surname)) #bu şekilde format yapabilriz sırayla süslülerin içersine koyar
# print("My name is {1} {0}" .format(name, surname)) #burada da formattan sonra her değişkenin 0 dan itibaren index no vardır print içinde süslüde indexi yazarak da çağırılabilir
# print("My name is {n} {s}" .format(n=name, s=surname)) #format içindekilere isim verip printte o sembol yada isimlerlede çağırabiliriz
# print ("My name is {} {} and I'm {} years old." .format(name, surname, "36")) #formatta illa değişken olmasına gerek yok string şeklinde de attırabiliriz yada yukarıda age tanımladık 36 yerine direkt age de yazılabilir

result = 100000/700
print("the result is {r:1.4} " .format(r=result)) #r den sonraki 1 direkt sayıyı yazdır demek ama 1 haricinde sayı yazınca o da tam kısım dahil kaç karakterlik boşluk bırakacağı eğer tam kısım o kadar uzun değilse boşluk basar extra
# 4 ise toplam sayının virgülden sonra da dahil kaç basamak olacağını yazar

# print (f"My name is {name} {surname} and I'm {age} years old.")
# bu özellik yeni direkt bu şekilde de yapılır ve bu çok tercih edilir


#print(f"{a+b}") #format metodu ile print içinde süslü parantez kullanarak değişkenler yazılabilir


# b="denbay"
# a="| {:<30}|".format(b) #süslü içden iki noktadan sonra <,>,^(ortalama),s(sadece strleri basar),d(sayıları),b(ikilik sistemdeki karşılıkları)
# print(a)


# a = """
# istanbul   : {}
# ankara     : {}
# izmir      : boyoz
# """.format("bogazı","") 
# print(a)


a="123456"
for b in a:
    print(f"sayi {b}")