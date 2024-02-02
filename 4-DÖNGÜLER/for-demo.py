numbers = [1,3,5,7,9,12,19,21]
for num in numbers:
    if (num % 3 == 0):
        print(num)

result = 0
for num in numbers:
    result += num
print(result)

for num in numbers:
    if (num % 2 == 1):
        print(num ** 2)


citys = ["kocaeli" , "istanbul" , "ankara" , "izmir" , "rize"]
for c in citys:
    if(len(c) <= 5):
        print(c)


#çok çok çok güzel önemli bir örnek
products = [ 
    {"name" : "samsung s6", "price": "3000"},
    {"name" : "samsung s7", "price": "4000"},
    {"name" : "samsung s8", "price": "5000"},
    {"name" : "samsung s9", "price": "6000"},
    {"name" : "samsung s10", "price": "7000"}
]

result = 0 #telefonların toplam fiyatını verecek
for product in products:
    price = int(product["price"])
    result += price
print(result)

for product in products:
    price = int(product["price"])
    if (price <= 5000):
        print(product["name"])