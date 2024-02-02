# def greeting(name):
#     print("hello", name)

# sayhello = greeting #bir fonksiyon oluşturup onu bir değişkene eşitlediğimizde
# # değişken ile fonksiyon adresleri aynı olur ancak değişkeni del yaparsak adres kalır değişkeni silmiş oluruz sadece yani fonksiyon aynen kalır
# print(sayhello)

############################## ENCAPSULATION (kapsülleme)

# def outer(num1):
#     print("outer")
#     def inner_increment(num1): #dışarıdan çağırılamaz sadece outher üzerinden ulaşılabilir
#         print("inner")
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)

# outer(10)


def factorial(number):
    if not isinstance(number, int): #isinstance metodu girilen değerin istenilen türde miğ ona bakar
        raise TypeError("sayı , tam sayı değeri olmak zorunda")
    
    if not number >= 0:
        raise ValueError("sayı , sıfır yada pozitif olmalı")
    
    def inner_factorial(number):
        if number <= 1:
            return 1
    
        return number * inner_factorial(number-1)
    
    return inner_factorial(number)

try:
    print(factorial(5))
except Exception as ex:
    print(ex)