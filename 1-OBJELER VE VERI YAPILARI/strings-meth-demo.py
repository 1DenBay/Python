website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- " Hello World " karakter dizisinde baş ve sondaki boşlukları Sil
hi = "  Hello World "
hi = hi.rstrip(" ") #sağ tarafı siler
hi = hi.lstrip(" ") #sol tarafı siler
print(hi)

# 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri Sil
result = "www.sadikturan.com".strip("w.moc") #tekrar eden harfleri sürekli girmeye gerek yok
print(result)

# 3- "course" karakter dizisinin tüm karakterlerini küçük yap
course = course.lower()
print(course)

# 4- "website" içinde kaç tane a karakteri vardır(count("a"))
print(website.count("a"))

# 5- "website" "www" ile başlayıp com ile bitiyor mu 
print(website.startswith("www"))
print(website.endswith("com"))

# 6- "website" içinde ".com" ifadesi var mı
print(website.find(".com"))

# 7- "course" içindeki karakterlerin hepsi alfabetik mi (isalpha, isdigit)
print(course.isalpha())

# 8- "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekle
a = "Contents"
a = a.center(50)
a = a.replace(" ", "*")
print(a)

# 9- "course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştir
course = course.replace(" ", "-")
print(course)

# 10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştir
hi = "Hello World"
hi = hi.replace("World","There")
print(hi)

# 11- "course" karakter dizisinin boşluk karakterlerinden ayırın
course = course.split(" ") 
print(course)

