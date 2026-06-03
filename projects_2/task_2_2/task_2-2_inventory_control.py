reagent_name = input("Введите название реактива: ")
reagent_quantity = int(input("Введите количество (целое число): "))
result = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."
print(result)
with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(result)

print("Отчет сохранен в файл inventory.txt")