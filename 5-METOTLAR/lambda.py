def square(num):
    return num**2

numbers = [1,3,5,9]
result = list(map(square,numbers)) #normalde direkt fonskiyonu yazıp 1 sayının karesi alınabilir ancak liste gibi birden fazla elemanlılarda map metodu kullanılır
#map metodu listenin içindeki elemanları tek tek alır ve istenilen fonksiyona götür kullanımıda (fonksiyon,listeadı) yada (yapılacakişlem , listeadı) şeklindedir
#ama map metodu direkt map(square,numbers) bu şekilde çalışmaz bu şekilde bize işlemi yapıp adres verir , somut bişey görmek için bunu ya liste içine atıp listeyi yazdır yada for döngüsü içerisinde kullanıp yazdır
for item in map(square,numbers):
    print(item)
print(result)


numbers = [1,3,5,9]
result = list(map(lambda num : num**2,numbers)) #lambda isimsiz fonksiyondur herhangi bir fonsiyon tanımlamadan hızlıca yapılması gerekeni yazıp aynı bir fonksiyon gibi çalışabilir yada lambdayı bir değişken içine atıp o değişken üzerindende çağırılabilir
print(result)
#lambda (işlemyapılacakdeğişken) : (değişken)(işlem),(kullanılacakyer)

numbers = [1,3,5,9,10,4]
def check_even(num): 
    return num%2==0
result = list(filter(check_even,numbers)) #filter map gibi tüm elemanları almaz fonksiyon içinde belirtilen özellikteki elemanlarla işlem yapar yine burada da check_even fonk. tanımlamak yerine lambda da kullanabiliriz
print(result) 

