
website = "http://www.sadikturan.com"
course = "python kursu: Baştan sona python programlama rehberiniz (40 saat)"

# 1- "course" karakter dizisinde kaç karakter var ?
print(len(course))

# 2- "website" içinde www karakterlerini al
print(website[7:10])

# 3- "website" içinde com karakterlerini al
print(website[22:25])
length = len(website) 
print(website[length-3:length]) #length son karakter sayısı -3 yapınca 3 geri geldi

# 4- "course" içinde ilk 15 ve son 15 karakterleri al
print(course[0:15], course[-15:]) #baştan başlayınca 0 yazmaya gerek yok direkt :15 olur yada sondan başlayıncada aynı

# 5- "course" ifadesinde ki karakterleri tersten yazdır
print(course[::-1]) #sadece :: koyduğumuzda tüm karakterleri alır sonunada -1 koyunca sondan basmaya başlar -1 adım sayısıdır aslında - sondan başla demek 1 de saten aralıksız bastır demek

name, surname, age, job = "bora", "yılmaz", 32, "mühendis" 

# 6- yukarada verilen değişkenler ile ekrana
# "Benim adım bora yılmaz, yaşım 32 ve mesleğim mühendis.",
print(f"Benim adım {name} {surname} , Yaşım {age} ve mesleğim {job}")

# 7- "hello world" ifadesinde ki w harfini  "W" ile değiştir
hi = "hello world"
print(hi[0:6] + "W" + hi[-4:])

# 8- "abc" ifadesini yan yana 3 defa yazdır
print("abc" * 3)