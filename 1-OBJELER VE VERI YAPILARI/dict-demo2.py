denbay = {"GÜÇ" : 120,
          "HP"  : 3050
         }
canbay = {"GÜÇ" : 100,
          "HP"  : 2050
         }

def vur(vuran:dict,vurulan:dict):
    vurulan["HP"] -= vuran["GÜÇ"]

a = input("denbayın vurması için d basın -- canbayın vurması için c basın ")
x=1

while x == True:
    if a == "d" or "c":
        if a == "d":
            vur(denbay,canbay)
            print(canbay["HP"])
            if canbay["HP"] <= 0:
                print("canbay mefta")
        elif a == "c":
            vur(canbay,denbay)
            print(denbay["HP"])
            if denbay["HP"] <= 0:
                print("denbay mefta")
        else:
            print("YANLIŞ TUŞLAMA YAPTINIZ ")
    else:
        print("yanlış tuşlama yaparak çıktınız ")

    x=input("çıkış için herhangi bir tuşa basınız -- Devam için 1'e basınız ")
    if x == 0:
        break
    else:
        continue
     ######olmadı