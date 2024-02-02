# def my_decorator(func):
#     def wrapper():
#         print("fonksiyon öncesi işlemler")
#         func()
#         print("fonksiyon sonrası işlemler")
#     return wrapper

# @my_decorator
# def sayhello():
#     print("hello")
# sayhello()

# sayhello = my_decorator(sayhello)
# sayhello() #bunu çağırınca üstte buna eşitlediğimiz my_Dec. fonskiyonu çalışır 
# 11. satır yerine 8.satırdakinin yapılması yeterli 

##########################################

import time
import math

def calculate_time(func): #içine bir fonksiyon alacak
    def inner(*args,**kwargs): #içine sınırsız iki tane değer alabilir sadece 1 tanede alabilir belli değil yani
        start = time.time() #boş olduğundan o anki saniyeyi alacak
        time.sleep(1) #1 saniye burada fonksiyon bekletilecek
        func(*args,*kwargs) #içeri alınan fonksiyon içinde aynı değerler dönecek
        finish = time.time()
        print(f"{func.__name__} fonksiyonu {str(finish-start)} saniye sürdü")
    return inner

@calculate_time #calculate içine fonksiyonu atmak için
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

usalma(8,3)
faktoriyel(5)