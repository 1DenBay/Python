
x = input ("1.sayi = ") #input c++daki cindir aslında kullanıcıdan değer ister bu değer sytr olarak alınır
y = input ("2.sayi = ") #inputun avantajı direkt parantezine tırnak içinde kullanıcıya mesaj iletebilir

print (type(x)) #burada x değerinin türünü sorgulatıp bastırdık
print (type(y))

toplam = int(x) + int(y) # x ve y değeleri str olduğundan toplama yerine yanyana yazma şeklinde yapardı ama inte çevirdik
print(toplam) #toplamı bastırdık

# kısaca bir değişken tanımladığımızda o değişkeni sonradan farklı bir değişkene dönüştürmek için
# değişken = dönüşecektür(değişken) 
# toplamada hepsi aynı tür olacak ama float ile int beraber olabilir 


# daire alan ve çevre hesaplama

pi = 3.14

r = float(input("yarı çap girin = ")) #ondalıklıda girebilir input belirtmediğmiz zaan direkt str olarak alır ancak biz başına float koyunca float alır
dairealan = pi * (r ** 2) #burada terim ** kaç üslü olduğu kuvveti alır
dairecevre = 2 * pi * r
print ("daire alanı = " + str(dairealan) + " " + "daire çevresi = " + str(dairecevre))