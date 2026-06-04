array = list(map(int, input("Введите числа через пробел: ").split()))

sum_odd_index = 0
count = 0
for i in range(len(array)):
    if i % 2 == 0:
        sum_odd_index += array[i]
        count += 1

average = sum_odd_index / count

print("Среднее арифметическое:", average)