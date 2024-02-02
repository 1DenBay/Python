import mod #kendi yazdığımız bir project'yi ismi ile import ederek direkt kullanbiliriz modül gibi

# result = help(mod)
# result = help(mod.func) #içiridekiler hakkında bilgi alabiliriz
# result = mod.number
# result = mod.person["name"] #modüldeki değerleri çekebiliriz

# p = mod.Person()
# p.speak()

# print(result)

#########

#terminalde python modu seçip sys import edip sys.path çalıştırdığımızda bize bu modüllerin nerede bulunduğunu yani nereden aldığını gösterir
#bu klasör lib klasörüdür burada buildtin olan modüller bulunur aynı zamanda bizim yazdığımız mod isimli modül gibi yazdığımız dosyaları lib'e atarsak yine sistem çalışacaktır sorun olmaz
#sys.builtin_module_names dediğimiz zaman terminale bize modülleri metotları filan gösterir