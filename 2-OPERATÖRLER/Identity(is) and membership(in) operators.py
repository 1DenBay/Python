# is operatörü adresler aynı mı yani "bu bumu" diye soru sorar tamamem bu budur olması için yani true olması için adreslerin aynı olması gerekir böylelikle herşey aynı olur

x = y = [1,2,3]
z = [1,2,3]

print(x==y) #x ve y adresleri aynı olduğundan değerlerde aynı olur yani yukarıda x = y (tek eşittir dikkat) adresleri eşitlediğimizden true
print(x==z) #x ve z adresleri farklı olsa bile == (2 eşittir) ile değerlerin eşit olup olmadığını soruyoruz yani true
print(x is y) #is ile x ve y nin adresleri aynı mı diye sorduk yukarı x = y yaparak adresleri eşitlemiştir o yüzden true
print(x is z) #burada her ne kadar değerler aynı olsada is adresleri sorgular o yüzden adresler farklı olduğundan false

x = [1,2,3]
y = [2,4]

del x[2] #14,15,16. satırlarda x ve y değerlerini birbirine eşitledik
y[1] = 1
y.reverse()

print(x==y) #değerleri eşitlediğimizden true olacaktır
print(x is y) #değerleri eşitlemiş olsak bile en başında farklıydı halen adresleri farklı olduğundan false
print(x is not y) #is not ilede is'in tam tersini sorgulatabiliriz "x,y değil mi" diye true gelir

###################

# in operatörü herhangi bir tanımın içinde karakter araması yapar yani "bu bunun içinde mi" sorusu sorar
 
x = ["apple","banana"] 
print("banana" in x) #banana x içerisinde mi diye soruyoruz

name = "deniz" 
print("d" in name) #string içinde bu şekilde tek tek harflerde aranabilir
print("d" not in name) #is deki gibi bu sefer başına not ile "d name içinde değil mi" diye sorarız false7

