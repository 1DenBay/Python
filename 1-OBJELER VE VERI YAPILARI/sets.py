fruits = {"orange", "banana", "apple"} #buda diğer list,tuple,dictionary gibi veri saklama yöntemi kümedir. hiçbir eleman tekrar etmez yani hepsinden 1 tane vardır
#burada veriler sırasız , yani indexsiz olarak sıralanır ve değişiklik yapılamaz sadece silme ve ekleme yapılabilir. bildiğimiz matematikteki kümelerdir
#fruits = set("sadas","dsadas") şeklinde de gösterilebilir

# for x in fruits: #alt alta düzenli yazdırır
# print(x)

# fruits.add("Mango") #tekli ekleme yapabiliriz
# fruits.update(["cherry","grape"]) #çoklu olarak dizi gibi ekleyebiliriz
# aynı veriden birden fazla olmaz bu yüzden olan veriyi tekrar eklesende yine bir kere alır

# fruits.remove("mango") #remove ve discard ile tekli silinebilir
# fruits.discard("apple")
# fruits.pop() #pop sondaki elemanı siler ancak burada yerleri sürekli değiştiği için rastgele silmiş olur
# fruits.clear #komple kümeyi siler


list = [1,2,2,4,8,9,9]
print(set(list)) #sete çevirince yani kümeye çevirince tekrar edenleri siler ve bir tane yazdırır
