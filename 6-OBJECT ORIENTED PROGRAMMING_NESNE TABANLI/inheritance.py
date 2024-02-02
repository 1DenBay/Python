# inheritance (kalıtım) : miras alma , classların birbirinden özelliklerini alması

#person => name,lastname,age,eat(),run()
#person classında tanımlanan attributesler ve metotlar filan herşey aşağıda studente yapınca hepsi aynen orayada geçer

#student(Person) => yapınca direkt personun özelliklerini kendine alır ancak person studentten etkilenmez böylece person süperclass , student altclass olur

# class Person():
#     def __init__(self):
#         print("Person Created")
# class Student():
#     def __init__(self):
#         print("Student Created") #böyle yapınca persondaki print ile çakışır ve student personu ezer buna override denir
# p1 = Person()
# s1 = Student()


class Person():
    def __init__(self, fname, lname): #parametreleri kalıtım yapacağımız diğer classların initlerine de yazılmalı
        self.firstname = fname #bunları burada tanımladığımızdan bir daha studentde tanımlamamız gerekmez
        self.lastname = lname
        print("Person Created")
    
    def who_am_i(self):
        print("i am a person")

class Student(Person):
    def __init__(self, fname, lname, number): #kalıtım yaptık bunları bir daha tanımlamaya gerek yok ama init içine yazmalıyız
        Person.__init__(self, fname, lname)  #bu çakışmayı önler yani önce personu çalıştırır ondan sonra studenti devam ettirir
        self.studentnumber = number
        print("Student Created")

    def who_am_i(self): #böyle yaparak persondakini ezebiliriz (override)
        print("i am a student")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) #bu super metodu "Person.__init__(self)" yerine kullanılır
        self.branch = branch
    
    def who_am_i(self):
        print(f"i am a {self.branch} teacher")

p1 = Person("ali" , "baba")
s1 = Student("deniz" , "baba", 1518)
t1 = Teacher("serkan", "yılmaz", "math")
print(p1.firstname + " " + p1.lastname)
print(s1.firstname + " " + s1.lastname + " " + str(s1.studentnumber))
p1.who_am_i()
s1.who_am_i() #student classda olmamasına rağmen yinede çalışır personda olduğundan 
t1.who_am_i()