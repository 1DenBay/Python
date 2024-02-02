'''
    MODÜL HAKKINDA BILGI
'''
print("modül eklendi")

number = 10
numbers = [1,2,3]
person = {
    "name" : "ali",
    "age" : "25",
    "city" : "istanbul"
}

def func(x):
    '''
    FONKSIYON HAKKINDA BILGI
    '''
    print(f"x: {x}")

class Person:
    def speak(self):
        print("I am speaking...")

Person.speak("tr")
func(7)