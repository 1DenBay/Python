#elif "eğer buysa" gibi bir anlam katar ve else gibi if'in alt katmanıdır ifden sonra istediğimiz kadar elif ekleyebiliriz if ile aynı sistemde çalışır

x = int(input(" x : "))
y = int(input(" y : "))

if x > y :
    print("x y den büyük")
elif x ==  y:
    print("x y eşittir")
else :
    print ("y x den büyüktür")


num = int(input("sayı : "))

if num > 0 :
    print("sayı pozitif")
elif num < 0 :
    print("sayı negatif")
else:
    print("sayı sıfırdır")

    ##############################

a = input("şifre belirleyniz")
if "abc" not in a: #in operatörüne aitlik operatörü denir
    print("şifre içinde abc kullanılması zorunludur")

 
a=8
b=8
if a==b :
    print("a bye eşit")
if a is b :
    print("a ile b kimlik olarak da eşittir")


sayilar = "516515489481656"
for sayi in sayilar: #karakterleri tek tek sırayla sayi değişkenine atar 
    print(sayi)

