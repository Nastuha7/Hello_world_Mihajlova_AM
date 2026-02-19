name_op = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Па):")
with open("sensor_log.txt", "w", encoding="utf-8") as card:
   card.write(f"Имя оператора: {name_op}\nТекущее значение давления: {pressure} Па\n")
   print("Данные успешно сохранены в sensor_log.txt")