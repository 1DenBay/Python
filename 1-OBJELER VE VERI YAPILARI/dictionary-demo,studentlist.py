a = input("Öğrenci numaranızı giriniz: ")
aname = input("Adınız giriniz: ")
asurname = input("Soyadınızı giriniz: ")
aphone = input("Telefon numaranızı giriniz")

b = input("Öğrenci numaranızı giriniz: ")
bname = input("Adınız giriniz: ")
bsurname = input("Soyadınızı giriniz: ")
bphone = input("Telefon numaranızı giriniz")

c = input("Öğrenci numaranızı giriniz: ")
cname = input("Adınız giriniz: ")
csurname = input("Soyadınızı giriniz: ")
cphone = input("Telefon numaranızı giriniz")

students = {
     a : {
         "Name" : aname,
         "Surname" : asurname,
         "Phone" : aphone
     },

     b : {
         "Name" : bname,
         "Surname" : bsurname,
         "Phone" : bphone
     },

     c : {
         "Name" : cname,
         "Surname" : csurname,
         "Phone" : cphone
     }
}

print(students[input("Öğrenci Bilgisi İçin Numarasını Giriniz: ")])