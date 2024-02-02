numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers) #direkt listede ki en küçüğü basar
val = max(numbers) #listede ki en büyüğü basar
val = min(letters) #alfabeye göre ilk geleni basar
val = max(letters) #alfabeye göre son geleni basar

val = numbers[6] #direk seçili karakteri basabiliriz
val = numbers[:4] #baştan 4e kadar basar
val = numbers[1:] #1den sona kadar basar
numbers[3] #seçilen elemana yeni değer atabiliriz

numbers.append(49) #listeye sona yeni eleman ekler tırnak ile srt olarak eklenebilir
numbers += [89] #append yerine bu şekilde de sona ekleme yapılabilir
numbers.insert(3, 84) #ekleme yapar 3.indexe 84 ekleyecek ve diğerlerinin indexleri birer tane kayacak
numbers.insert(-1, 45) #en sonuncudan hemen önceye ekler

numbers.pop() #parantezi boş olunca sonuncu elemanı siler index no yazarsan onu siler
numbers.remove() #bu da siler ancak bu indexe göre değil direk elemanı yazarsın bulup onu siler
numbers.sort() #listeyi büyükten küçüğe sıralar
letters.sort() #bu listeyide alfabetik sıralar
numbers.reverse() #listeyi olduğu gibi ters çevirir
    
print(len(numbers)) #srt methoddaki gibi eleman sayısını öğrenebiliriz
print(numbers.count(10)) #10 elemanından kaç tane olduğunu söyler
print(letters.count("a"))
numbers.clear() #tüm elemanları temizler
