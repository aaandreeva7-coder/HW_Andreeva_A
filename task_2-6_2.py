temp = float(input("\nКакая температура листа сейчас? "))

if temp < 5:
    print("\n\tСлишком холодно. Фотосинтез почти не идёт.")
elif 5 <= temp <= 25:
    print("\n\tОптимально для растений с C3-метаболизмом")
elif 25 < temp <= 35:
    print("\n\tХорошо для растений C4-метаболизмом")
else:
    print("\n\tIt's hot as hell! Cool down, bro.")