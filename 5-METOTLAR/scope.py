x = "global x" #global scope #fonksiyon dışında yaptığımız tanımlamalar heryerde geçerlidir
def function(): #ancak fonksiyonlar içerisinde yaptığımız tanımlamalar local olarak geçer ve sadece fonksiyon içerisinde geçerlidir
    x = "local x" #local scope
function()
print(x) #global x bastırılır

##############

name = "çınar" #global
def changename(new_name):
    name = new_name #local
    print(name) #local name'i yazdırmak için
changename("deniz") 
print(name) #global name yazdırılır

###############

name = "global str"
def greeting(): #burada ki global scope ise yine kendinden önceki katman olan ana katmandır yani name = "global str"
    name = "deniz" #hello'nun global scopu
    def hello(): #iç içe fonksiyonlarda global scope kendisinden bir önceki katmandakidir yani hello fonk. global scope'u kendinden önceki katman olan greeting fonk. da tanımlananlardır
        print("hello" + name) #eğer local scope yoksa global kullanılır ama bundan önce local scope tanımlarsak hello fonk. için o zaman local deki bastırılır
    hello() #greetingi çağırınca helloda çalışacak
greeting()

################

x = 50
def test(x):
    print(f"x : {x}") #burada daha local x tanımlanmadığından global olan çalışacaktır
    x = 100 #local x
    print(f"changed x to {x}") #artık local x kullanılacak
test(x) #direkt fonksiyon çalışır içindeki local global sıralama içindeki gibidir
print(x) #burada direkt x basınca global olan basılır


x = 50 #üstteki işlemlerin aynısı
def test(x):
    #global x #eğer ki fonksiyon içinde yapılacak işlemlerin kalıcı olması için yani global x de de değişmesi için hemen fonksiyondan sonra "global x" diye eklenmesi yeterli
    print(f"x : {x}") 
    x = 100 #local x
    print(f"changed x to {x}")
test(x) 
print(x)
