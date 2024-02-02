numbers = [1,3,5,7,9,12,19,21]
x=0
while x<8:
    print(numbers[x])
    x += 1

ba = int(input("başlangıç değeri girin : "))
bi = int(input("bitiş değeri girin : "))
while ba <= bi:
    if (ba % 2 == 1):
        print(ba)
    ba += 1

a=100
while a >= 1:
    print(a)
    a -= 1

numbers = []
a = 0
while a < 5:
    x=int(input("sayı giriniz : "))
    numbers.append(x)
    a += 1
numbers.sort()
print(numbers)

adet = int(input("Ürün Sayısını Giriniz : "))
products = []
i=0
while i < adet:
    name = input("Ürün ismi : ")
    price = input("ürün fiyatı : ")
    products.append({
        "name" : name,
        "price": price
    })
    i += 1
for product in products:
    print (f"ürün adı : {product['name']} - ürün fiyatı : {product['price']}")