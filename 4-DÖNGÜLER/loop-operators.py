for item in range(50,100,10): #range for ile adım sayılı aralıklı gibi sayılar yazdırırken kolaylık sağlar hemen bizim için liste oluşturur ve yimne aynı muabbete devam eder tek tek iteme atama yapar
    print(item)

#parantez içine bir sayı girilirse 0 dan o sayıya kadar girilen değişkene atama yapar
print(list(range(50,100,10))) #görüldüğü gibi bir liste oluşturuyor kolaylık için

#enumarete bize for döngüsünde tek tek atama yaparken hangi karakterin kaçıncı indexe geldiğini söyler

greeting = "hello"

for index,  item in enumerate(greeting): #aynı şekil for döngüsü tanımla sadece karakterlerin alınacığı diziye enumaret parantezi içine ekle
    print(f"index : {index} - letter : {item}")

zip()# listeleri eşleştirme işlemidir

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3))) #sırasıyla önce zip ile 3 listeyi eşleştirdik sonra bunu listeye çevirdik sonrada ekrana bastırdık

for item in zip(list1,list2,list3): #üçlü üçlü olarak tek tek sırayla item içine attık
    print(item) #bunları 3lü olarak bastırdık

for a,b,c in zip(list1,list2,list3): #burda yine 3lü atamalar yapar ancak atama yapacağı değişken virgüllü olduğundan yine virgülü baz alarak atamaları yapar sırasıyla atar
    print(a,b,c) #burda tek tek de bastırabiliriz bu şekil komplede ama böyle virgüllü basınca parantez şeklinde ayırmaz çünkü tek tek atadı
