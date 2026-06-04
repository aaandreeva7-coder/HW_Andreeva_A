n = int(input("Введите количество обпрабатываемых чисел: "))

max_num = None

for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))
    
    if max_num is None or num > max_num:
        max_num = num

print("Самая большое число", max_num)