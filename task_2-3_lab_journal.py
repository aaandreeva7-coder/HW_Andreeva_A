researcher_name = input("Введите ФИО исследователя: ")
experiment_date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment_title = input("Введите название эксперимента: ")
experiment_conclusion = input("Введите вывод/результат эксперимента: ")
LINE_WIDTH = 50
BORDER = "+" + "-" * (LINE_WIDTH - 2) + "+"
with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(BORDER + "\n")
    file.write(f"|{' Электронный лабораторный журнал':<{LINE_WIDTH-1}}|\n")
    file.write(BORDER + "\n")
    file.write(f"| ФИО исследователя : {researcher_name:<{LINE_WIDTH-24}}|\n")
    file.write(f"| Дата             : {experiment_date:<{LINE_WIDTH-24}}|\n")
    file.write(f"| Эксперимент      : {experiment_title:<{LINE_WIDTH-24}}|\n")
    file.write(BORDER + "\n")
    file.write(f"|{' Вывод:':<{LINE_WIDTH-1}}|\n")
    max_text_width = LINE_WIDTH - 6  
    words = experiment_conclusion.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_text_width:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            if current_line:
              file.write(f"|   {current_line:<{max_text_width}}|\n")
              current_line = word
            if current_line:
                file.write(f"|   {current_line:<{max_text_width}}|\n")
    file.write(BORDER + "\n")