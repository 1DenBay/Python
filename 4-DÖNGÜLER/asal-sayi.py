sayi = int(input("sayi giriniz : "))
asalmi = True #girilen sayıyı asal olarak kabul edelim

if (sayi == 1): #bir özel durum olduğundan ayrı if bloğu yaptık
    asalmi = False #kabulu iptal ettik

for i in range(2,sayi): #2 den girdiğimiz sayıya kadar bizim için liste oluşturdu ve for çalışacak
    if (sayi % i == 0):
        asalmi = False #bölündüğü sayı var ise kabul iptal edilir
        break
if asalmi: #burada birşey yazmadığımızdan asalmi yi true kabul eder
    print("sayı asaldır")
else:
    print("sayı asal değil")