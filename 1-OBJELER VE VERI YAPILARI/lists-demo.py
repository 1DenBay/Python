
car = ["BMW" , "Mercedes" , "Opel" , "Mazda"]
print(car)
print(len(car)) #kaç eleman var
print(car[0])
print(car[3])
car[-1] = "Toyota" #artık -. indexte toyota var
result = "Mercedes" in car #merc car listesinde var mı kontrolü
result = car[-2]
result = car[:3]
result = car[2:] = ["Toyota","Renault"]
result = car #indexten sonrasını toyo ve rena ile değiştirdik
result = car + ["Audi","Nissan"] #car listesine extra bi liste daha ekledilk
del car[-1] #- indexli str yi sildik
result = car
result = car[::-1] #tüm listeyi :: yaparak seçtik ve -1 yaparak tersten yazdırdık
print(result)

studentA = ["Yiğit" , "Bilgi" , 2010 , [70,60,70]]
studentB = ["Sena" , "Turan" , 1999 , [80,80,70]]
studentC = ["Ahmet" , "Turan" , 1998 , [80,70,90]]
ort = ((studentA[3][0] + studentA[3][1] + studentA[3][2])/3)

result = f"{studentA[0]} {studentA[1]} {2022-2010} Yaşında ve Not Ortalaması {ort:1.4}"#yuvarlama yaptık ort:1.4
print(result)