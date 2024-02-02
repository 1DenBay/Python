with open("newfile.txt", "r+", encoding="utf-8") as file: #r+ hem okuma hem de yazma modudur
    print(file.read())

with open("newfile.txt", "r+", encoding="utf-8") as file:
    file.write("deneme")

with open("newfile.txt", "r+", encoding="utf-8") as file: #r+ hem okuma hem de yazma modudur
    print(file.read())

with open("newfile.txt", "a", encoding="utf-8") as file:
    file.write("\nemel feyt")

with open("newfile.txt", "r", encoding="utf-8") as file: #r+ hem okuma hem de yazma modudur
    print(file.read())

# sayfa başına bilgi eklemek içinde write metodunu kullanmadan önceki satırda seek ile imleci 0 a çekmemiz gerekir
# sayfa ortasına bilgi eklemek için önce readline metodu ile listeye çevir dosyayı sonra insert ile liste şeklindeyken parametreyi ekle sonra for döngüsü ile tekrar file.write ile txt yap (yada for döngüsü kullanma writelines(liste) şeklinde metotla for döngüsüne gerek kalmaz)