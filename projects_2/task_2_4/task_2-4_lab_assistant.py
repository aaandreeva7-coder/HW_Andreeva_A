volume_ml = float(input("Введите нужный объем физиологического раствора (мл): "))
salt_mass = volume_ml * 0.009
salt_volume_ml = salt_mass / 2.16
water_volume = volume_ml - salt_volume_ml
with open("solutionrecipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-----------------------\n")
    file.write(f"Общий объем: {volume_ml:.2f} мл\n")
    file.write(f"Масса соли:  {salt_mass:.2f} г\n")
    file.write(f"Объем воды:  {water_volume:.2f} мл\n")
    file.write("\nИНСТРУКЦИЯ:\n")
    file.write("1. Отмерьте указанный объем дистиллированной воды\n")
    file.write("2. Добавьте рассчитанную массу NaCl\n")
    file.write("3. Перемешивайте до полного растворения соли\n")

print("\nРецепт успешно сохранен в файл solutionrecipe.txt")