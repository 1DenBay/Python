# bellekte yer kaplamayan iteratorslardır böylece uzun işlemlerde çıkan sonuç kullanıldıktan sonra silindiği için performans açısından iyidir

# def cube():
#     for i in range(5):
#         yield i ** 3 #sonuç çıkıp kullanıldıktan sonra silinmesi için yield kullanılır
    
# for i in cube():
#     print(i)

#####################

liste = [i**3 for i in range(5)] #bu şekilde bir liste tanımladığımızda normal olarak bellekte bir adresi oluyor yani yer tutuyor ancak köşeli değilde normal parantezli yaparsak listeyi generators olarak tutar yani yer kaplamaz
print(liste)

generator = (i**3 for i in range(5))
print(generator)
for i in generator:
    print(i)