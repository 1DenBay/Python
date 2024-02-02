import re

# result = dir(re)

str = "deniz bayat programlama rehberi - 40 saat"

#findall
result = re.findall("saat",str) #girilen ifade içinde ifadeyi arar ve liste içine alır
result = len(result) #kaç tane saat ifadesinden bulmuş diye bakabiliriz

#split - sub
result = re.split(" ",str) #boşluk karakterlerinden bölüp liste içine alacak
result = re.sub(" ", "-", str) #değiştirme işlemi yapar il girilen yerine ikincisini koyar

#search
result = re.search("saat", str) #arama işlemi yapar bulduğu ifadenin baş ve son karakterlerini gösterir
result = result.span() #bu metot aslında search içinde saten gösterilir ancak sadece hangi karakterler arasında olduğunu öğrenmek için kullanılır
result = result.start() #start yerine end kullanıp bitip karakteride öğrenilebilir
result = result.group() #aranan kelimeyi gösterir
result = result.string() #aranan str ifadeyi gösterir


# regular expression

# [] -> içine yazılan tüm karakterler aranır
result = re.findall("[abc]", str) #str içinde kaç tane a-b-c karakterleri varsa bulur yani kelime yazsanda karakter karakter arayacak
result = re.findall("[a-e]", str) # "-" işareti arası anlamına gelir a ile e arasında ki a-b-c-d-e karakterlerini arayacak
result = re.findall("[1-5]", str) #harflerdeki gibi ara değerleri de arayacak
result = re.findall("[^adr]",str) # "^" işareti dışında anlamına gelir bu aralıkta olabilir bu şekilde direkt karakterlerde girilebilir

# . -> her hangi bir tek karakter anlamına gelir
result = re.findall("...", str) #bize str içindeki tüm 3 farklı karakterleri getirir
result = re.findall("p....n", str) #şeklinde de yapabiliriz

# ^ -> başlıyor mu anlamına gelir
result = re.findall("^p", str) #p ile başlayan ifadeleri bulur

# $ -> bitiyor mu anlamına gelir
result = re.findall("t$", str) #t ile biten ifadeleri ara

# * -> bir karakterin sıfır yada daha fazla olup olmamasına bakar
result = re.findall("sa*t", str) # sa*t ifadesinde kaç tane a var t HEMEN ÖNCE gelen ona bakar 0 yada daha fazla ise çalışır ancak t ile arasında birşey var ise çalışmaz

# + -> bir karakterin bir yada daha fazla olup olmamasına bakar 0 olunca çalışmaz
result = re.findall("sa+t", str)

# ? -> bir karakterin sıfır yada birkez olup olmamasına bakar
result = re.findall("sa?t", str) #iki tane olduğundan çalışmaz

# {} -> karakter sayısını kontrol eder
# al{2} -> a karakterinin arkasına l karakteri 2 kez tekrarlamalı
# al{2,3} -> a karakterinin arkasına l karakteri en az 2 , en fazla 3 kez tekrarlamalı
# [0-9]{2,4} -> en az 2 en çok 4 basamaklı sayılar

# | -> alternatif seçeneklerden birisi için kullanılır
result = re.findall("a|4", str) 

# () -> gruplama için kullanılır
#(a|b|c)xz -> a yada b yada c karakterleri arkasına xz gelebilir gibi ifadeler yazılabilir

#############

# \ -> özel karakterleri aramasını sağlar
# \$a -> $ karakterini algılamaz arkasına a karakterini arar

# \A -> belirtilen karakter str ifadenin başında mı
# \Athe -> the ile mi başlıyor str ifade

# \Z -> belirtilen karakter str ifadenin sonunda mı
# the\Z -> str ifade the ile mi bitiyor
result = re.findall("\Asaat", str)
print(result)