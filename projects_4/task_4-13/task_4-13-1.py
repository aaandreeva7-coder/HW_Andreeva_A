a = input("Введите первое число ")
b = input("Введите второе число ")
c = input("Введите третье число ")
d = input("Введите четвертое число ")

if a > b :
    min = b
else:
     min = a

if min > c :
     min = c

if min > d :
     min = d

print( min,"- самое маленькое число")