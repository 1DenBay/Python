customername = "deniz"
customerlastname = "bayat"
customernamelastname = customername + " " + customerlastname
customersex = True #erkek mi kadın mı -bool ifadedir
custoemrtc = "242894648" # tırnaksız sayılar int olur
customerbrith = 1985
customeradress = "inönü"
customerage = 2022 - customerbrith

print (customeradress,customerage,customerage)

order1 = 110
order2 = 158.25
order3 = 1187

print(bool(order1)) #bool içerisinde 0dan farklı bir değer,ne olursa olsun str,int filan fark etmez true döndürür sıfır yada boş olursa false döndürür
print(str(order1)) #order1 değişkenini str ifadeye çevirdik ancak bu işlem kalıcı değildir sadece yazdığımız satır içindir

print ("total = " , order1+order2+order3)

