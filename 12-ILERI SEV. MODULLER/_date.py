# import datetime #bu şekilde tüm metotlar eklenir
from datetime import datetime, timedelta #bu şekilde sadece kullanılacak metotlar eklenebilir böyle yapınca kullanırken datetime.date şeklinde değilde direkt date olarak kullanabiliriz

result = dir(datetime) #modül çinde kullanılabilecek metotları gösterir

simdi = datetime.now() #o anlık tarihi basar
result = simdi.year #bu şekilde tek tek verilerde çekilebilir
result = simdi.second

result = datetime.ctime(simdi) #str olarak daha açıklayıcı bilgi verir
result = datetime.strftime(simdi,"%Y") #bu şekilde str bilgileri de çekebiliriz "%" ifadesi ile kodlanmış bilgileri internetten bakabilirz her bilginin kendi harfi vardır
result = datetime.strftime(simdi,"%X")
result = datetime.strftime(simdi,"%Y %B %A") #birden çokta basabiliriz

t = "21 Nisan 2019" #bu şekilde ki bilgiyi python anlamıyacaktır sonuçta normal str ifade olarak algılar
gun, ay, yil = t.split() #ama bu şekilde yaptığımız da pythona göstermiş oluruz index şeklinde verdiğimizden sıra önemli
# print(gun) #bu şekilde tek tek çekilebilir artık

t = "15 April 2019 hour 10:12:30"
result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S") #yukarıda splitlemek yerine bu şekilde daha pro ve anlaşılır kullanılabilir ve kolay yapılabilir
result = result.year

brithday = datetime(1983,5,9,12,30,10) #kendimiz tarih oluşturabilirz
result = datetime.timestamp(brithday) #belirlenen tarihi komple saniyeye çevirir
result = datetime.fromtimestamp(result) #saniyeyi geri tarihe döndürür
result = datetime.fromtimestamp(0) #bilgisayarlar için kullanılan başlangıç tarihinden itibaren hesapladığından o başlangıç tarihini verir

result = simdi - brithday #tarihler arasında hesap yapma timedelta modülünün işidir datetimedan ayrı bir modüldür
result = result.days #yapılan işlemde ki tarihi bize gün cinsinden verir
# result = result.seconds #istediğimiz her hangi bir cinsten alabiliriz 
result = simdi + timedelta(days=10, minutes=10) #tarihler içinde hesaplamalarda kullandığımızdan istediğimiz tarihin istediğimiz cinsine işlemler yapabiliriz

print(result)