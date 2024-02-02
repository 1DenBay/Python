x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

a = int(input("Bir sayi giriniz: "))
b = int(input("Bir sayi giriniz: "))
result = (a*b) - (x+y+z)
print(result)

print(y // x)

print(x+y+z % 3)

print(y ** x)

x, *y, z = numbers
print(z**3)

x, *y, z = numbers
print(y[0]+y[1]+y[2])
