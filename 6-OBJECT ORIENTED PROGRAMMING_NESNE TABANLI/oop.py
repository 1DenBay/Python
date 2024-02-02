#class -> class kavramı bize python tarafından verilmiş kullanmamız için hazır özellikler , metotlardır. bizde kendimize göre class oluşturup bu classların içerisinede instance oluşturup kendi metotlarımızı yapabiliriz
#kendi classımızı oluşturmak için birden fazla kez kullanacak olmalıyız ki yaptığımıza değsin

#instance(object) -> classların içerisinde ayrı ayrı olacak şekilde istenen yada girilmesi gereken bilgi diyebiliriz. classlardaki metotlar fonksiyonlar bu bilgiler üzerinden çalışır

#örneğin bir list class oluşturursak class bize liste için eklenmiş olan özellikleri sunar ve hazır bir şekilde hemen list.(----) yaparak kullanırız

# list = [1,2,3,6]
# result=type(list) burada listenin türünü sorguladığımızda class list olarak verir yani listeleme özelliği pythonun bize built-in yani class olarak hazır verdiği bir özelliktir
# print(result)

#mesela bir person class oluşturup bunun içinde : name,surname,yearofbirth gibi instrance'lar tutabiliriz ve calculatorage() diye bir fonksiyon yazıp yearofbirth üzerinden name.calculatorage() yapıp yaş hesaplatabiliriz