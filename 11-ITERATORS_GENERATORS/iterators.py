# normalde liste içinde ki elemanları bastırmak için for döngüsü kullanırız ancak for döngüsünün arkasında iterators metodu çalışır , iterators bize üzerinde next metodu ile dolaşabileceğimiz bir tür objedir

# liste = [1,2,3,4,5]

# for i in liste: # listeyi normal bastırma
#     print(i)
#####################
# x = iter(liste) #burada iter fonksiyonu tek tek liste içinde ki elemanları alır ve bir adreste tutar
# print(next(x)) #burada tuttuğu adresi bastırınca normal bizim görebileceğimiz şekilde ekrana bastırılır burada sorun her seferin de tek bir eleman basar altına aynısını yazınca bu sefer bir sonra ki elemanı sadece basar
# print(next(x)) #en son eleman sayısından fazla yazdığımız zaman hata verir
#####################
# while True: #tek tek uğraşmak yerine while ile yapılabilir -> for döngüsünün arka planda yaptığı işlem budur
#     try:
#         element = next(x)
#         print(element)
#     except StopIteration: #while sonsuz döngü olduğundan eleman sayısından fazla iter çalıştırınca hata verir o yüzden try-except bloğu kullandık
#         break
#####################
class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def ___iter__(self):
        return self
    
    def ___next__(self):
        if self.start <= self.stop:
            x =self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(10,20)
myiter = iter(list)
print(next(myiter))

for x in list:
    print(x)
