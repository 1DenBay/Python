# def usalma(number):
#     def inner(power):
#         return number ** power

#     return inner #usalma çalışınca ilk parametreyi taban olarak alır sonra inner döndürdüğümüzden yine parametre ister ve bunu da üs yapar

# two = usalma(2)(3) #iç içe fonksiyonda iki parametre bu şekil yanyana olabilir
# print(two)

# three = usalma(3) #yada bu şekilde önce ilk parametre sonra 2.parametre ayrı şekildede yazılabilir
# print(three(4))

#######################################

# def yetki_sorgula(page):
#     def inner(role):
#         if (role == "admin"):
#             return (f"{role} rolü {page} sayfasına ulaşabilir")
#         else:
#             return (f"{role} rolü {page} sayfasına ulaşamaz")
#     return inner

# user = yetki_sorgula("design")
# print(user("admin"))
# print(user("user"))

########################################

def islem(islem_adi):
    
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if (islem_adi == "toplama"):
        return toplama
    else:
        return carpma

toplama = islem("toplama")
print(toplama(8,5,6,78,58))

carpma = islem("çarpma")
print(carpma(8,5,9,2))