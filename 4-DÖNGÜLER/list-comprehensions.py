for x in range(10): #önceki derste böyle yaptık range hemen yerimize 10luk liste yapıyo ve x içine atıyodu sırayla
    print(x)

numbers = []
for x in range(10): 
    numbers.append(x) #yada somut bir şekilde liste içine de aktarabiliriz

numbers = [x for x in range(10)] # bu bi üsttekinin kolay yolu ilk x , xleri tek tek numbersa at anlamına gelir
print(numbers) #burada yaptığımız önce range ile 10luk bir liste oluşturduk sonra bunları x e atadık sırayla en ilk x ise atama yaptığımız x lere hangi işlem yapılarak liste içine alınacağını gösterir

for x in range(10): #burda yine ilkel yol ile x e sırayla 10a kadar atama yaptık ve liste içine karelerini aldık
    print(x**2)
numbers = [x]

numbers = [x**2 for x in range(10)] #üstteki olayın kısa versiyonunu yaptık yani parantez içinde ki ilk x sonraki fonksiyondan sırayla alınan değerlere ne işlem yapılarak liste içine alınacağoını gösterir
print(numbers)

mystr = "hello"
mylist = [letter for letter in mystr] #str ifadeler de kullanılabilir
print(mylist)

years = [1983,1985,1968,2008,2005]
ages = [2019-year for year in years] #bu şekilde kısa yolları kullanabiliriz
print(ages)

result = [x if x%2==0 else "TEK" for x in range(1,10)]
print(result) # bu şekilde liste içine if ekleyerek ve str ifade de bastırabilriiz

result = [] #ilkel yol
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers) #gelişmiş yol :D
