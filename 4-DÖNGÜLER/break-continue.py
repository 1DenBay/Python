name = "deniz bayat"
for letter in name:
    if letter == "i":
        continue #i harfinin geldiği döngüyü atla ve devam et demek
    print(letter)
for letter in name:
    if letter == "i":
        break #i harfi gelince döngüyü kır ve çıkış yap demek
    print(letter)


x = 0
result = 0
while x <= 100:
    x += 1
    if (x % 2 == 0):
        continue
    result += x
print(result)
