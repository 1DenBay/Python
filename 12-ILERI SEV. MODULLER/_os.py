#işletim sistemi hakkında bilgiler ve işletim sis. içinde işlemler için kullanılır
import os

result = dir(os)
result = os.name #kullanılan işletim sistemini söyler
result = os.getcwd() #klasörün yerini verir
os.mkdir("newdirectory") #aynı klasör içinde bir yeni bir klasör oluşturur

result = os.chdir("C:") #changedirectory metodu ile bulunduğumuz konumu değiştirip oraya birşeyler ekleyebiliriz
os.mkdir("newdirectory") #yaptığımızda tekrar bu sefer direkt c klasöründe olduğumuzdan oraya klasör oluşturur
os.chdir("..\..") #bu şekilde bulunduğumuz yerden bir üst klasöre geçeriz

os.makedirs("newdic/yenidic") #klasör içinde klasör açabiliriz

result = os.listdir() #bulunduğumuz dizin içide ki klasörler gösterilir
result = os.listdir("C:\\") #istediğimiz dizin altındaki klasörlerede bakabilirz
for dosya in os.listdir():
    if dosya.endswith(".py"): #şekline yaparak istediğimiz uzantılı dosyaları bulabilirz
        print(dosya)

result = os.stat("date.py") #stat içine girilen dosya hakkında bilgiler verir mesela en son ne zaman oluşturuldu gibi ancak bu bilgileri en küçük birimde verir
os.system("notepad.exe") #istediğimiz dosyayı çalıştırabiliriz
result = os.rename("dosyaadı","yeniadı") #dosya adı güncelleme
os.rmdir("yeniklasör") #klasörü siler ama alt klasörleri yoksa kullanılır
os.removedirs("yeniklasör/içyeniklas") #bu şekilde içeridekileri silebiliriz

result = os.path.abspath("os.py") #istenilen dosyanın konumunu verir
result = os.path.dirname("C:/Users/deniz/OneDrive/Masaüstü/PROGRAMLAMA/os.py") #konumu verilen dosyanın asıl ismini verir
result = os.path.dirname(os.path.abspath("os.py")) #dosyanın dizin yolunu bulur
result = os.path.exists("C:/Users/deniz/OneDrive/Masaüstü/PROGRAMLAMA/os.py") #yolıu verilen veriyi sorgular var yada yok ka göre true false döndürür
result = os.path.isdir("C:/Users/deniz/OneDrive/Masaüstü/PROGRAMLAMA") #klasörmü değilmi sorgulaması yapar
result = os.path.isfile("C:/Users/deniz/OneDrive/Masaüstü/PROGRAMLAMA/os.py") #dosyamı sorgulaması yapar
result = os.path.join("") #aralara virgüllü olarak yazılan klasörleri filan yada konumu istenilen yerlere götürür
result = os.path.split("") #üsttekinin tam tersi konumu komple tek tek ayırır indexler
result = os.path.splitext("os.py") #dosya adı ile uzantısını ayırır ve indexler


print(result)
os.rmdir("Yeni klasör")