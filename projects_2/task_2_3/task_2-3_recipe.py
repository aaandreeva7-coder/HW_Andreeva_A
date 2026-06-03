name_nutrient_medium = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агар-агара (%): ")
temperuture = input("Введите температуру для стерилизации (°C): ")
with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"Рецепт приготовления питательной среды\n")
    recipe.write(f"Питательная среда:\t{name_nutrient_medium}\n")
    recipe.write(f"Концентрация агар-агара:\t{agar_concentration}%\n")
    recipe.write(f"Температура стерилизации:\t{temperuture}°C\n")
