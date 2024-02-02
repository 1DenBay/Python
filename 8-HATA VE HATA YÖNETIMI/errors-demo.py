liste = ["1" , "2" , "5a" , "10b" , "abc" , "10" , "50"]

# 1-liste elemanları içindeki sayısal değerleri bulunuz
for x in liste: #if bloğu şeklinde yapılamaz "type(a) == int" gibi çünkü type(a) çalışmaz sayısal değerler listede str türünde olduğundan type str döndürür int içinde
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

###########################################

#2-kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.
while True:
    sayi = input("Sayı giriniz : ")
    if (sayi == "q"):
        print("sistem kapandı")
        break
    try:
        result = float(sayi) and str(sayi)
        print("doğru girdi")
    except:
        print("lütfen tam sayı değeri giriniz")
        continue

############################################

#3-girilen parola içinde türkçe karakter hatası veriniz
turkçe_karaterler = "şçğıöüİ"
parola = input("parola : ")
for i in parola:
    if (i in turkçe_karaterler):
        raise Exception("türkçe karakter kullanmayınız")
    else:
        print("geçerli parola")
        break

#############################################

#4-faktöriyel fonksiyonu oluşturup çalışmayacak değerler için hata mesajları verin
def faktöriyel(x):
    havuz = 1
    x = int(x)
    if (x < 0):
        raise ValueError("lütfen pozitif sayı giriniz")
    else:
        for i in range(1,x+1):
            havuz *= i
        print(f"{x}! = {havuz}")

for x in [10,20,50,"1s0"]:
    try:
        y = faktöriyel(x)   
    except ValueError as error:
        print(error)
        continue
    print(y)
        