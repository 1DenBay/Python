message = "Hello There. My name is Sadık Turan"
message.split()
print(message[0]) #listelemenin küçük hali gibi düşün messengaari split ile parçalayarak liste haline dönüştürüyoruz

my_list = [1,2,3] #direkt bu şekilde köşeli parantez ile liste oluşturulabilir
my_list = list(1,2,3,"123") #köşeli parantez yerine "list()" kullanılabilir
my_list = ["bir",1,True,5.6,] #liste elemanlarının türleri farklı olabilir
print(my_list)

list1 = ["one" , "two" , "there"]
list2 = ["four" , "five" , "six"]
no = list1 + list2 #iki listeyi bu şekilde birleştirebiliriz 
print(no)
print(len(no)) #yine len ile eleman sayısını bulabiliriz

userA = ["Sadık" , 36]
userB = ["Çınar" , 2]
users = [userA , userB] #liste içinde liste yapabiliriz
print(userA)
print(userB)
print(users)
print(users[0][1]) #bu şekilde liste içindeki listeye ulaşılabilir

###############

sayilar = list(range(1,6))
sayilar2 = [*range(1,6)]
print(sayilar , sayilar2)
#sayilar listelerini ikiside aynı şeydir altta olan brackets yöntemi yani köşeli parantez yöntemidir daha kullanışlı ve kolaydır