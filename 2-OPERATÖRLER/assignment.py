# x, y, z = 5, 10, 20

# x += 5         #x = x + 5
# x -= 5         #x = x - 5
# x *= 5         #x = x * 5
# x /= 5         #x = x / 5
# x %= 5         #x = x % 5
# x //= 5        #x = x // 5 sadece tam kısmı alır
# x **= 5        #x = x ** 5 xin 5.kuvveti alınır 5 yerine değişkende gelebilir


values = 1, 2, 3, 4, 5
x, y, *z = values #dediğimiz zaman bu x y z yi sırasıyla yukarıda ki valuesler ile eşler yıldız olana geri kalan hepsini atar

print(x,y,z) #2 values içinde de eşit sayıda eleman olmalı biri birinden eksik fazla olmaz
#eğer fazla değer var ise sayılarda harfler kısmından birinin başına * işareti koyulur bu fazla olan tüm elemanları liste şekline getirip yıldız olan harfe atar

