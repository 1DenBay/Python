x = 5

result = (x > 5) and (x < 10)
# and operatörü ve'dir yani iki şartta doğru ise true değeri verir
# result = true, true -> TRUE
# result = false, true -> FALSE
# result = true, false -> FALSE

hak = 5
devam = "e"
result = (hak > 0) and (devam == "e") 
# mesela kullanıcıdan e harfini isteyerek oyunlarda hakkına göre devam ettirebiliriz

result = (x > 0) or (x % 2 == 0)
# or operatörü yada dır şartlardan birinin true olması yeterli
# result = true, true -> TRUE
# result = false, true -> TRUE
# result = true, false -> TRUE

result = not(x > 2)
# x=5 olduğundan normalde x>2 true olur ancak not operatörü cevabın tam tersini alır

result = ((x > 5) and (x < 10)) or (x % 2 == 0)
#birden çok şart koyabiliriz

print(result)