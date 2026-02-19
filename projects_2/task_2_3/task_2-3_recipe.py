name_ps = input("Введите название питательной среды: ")
agar = input("Введите концентрацию агара в %: ")
temp_s = input("Введите температуру стерилизации в °C: ")
with open("recipe.txt", "w", encoding="utf-8") as card:
   card.write(f"Питательная среда: {name_ps}\n Концентрация агар-агара: {agar}%\n Температура стерилизации: {temp_s}°C\n")
   print("Файл 'recipe.txt' успешно сформирован!")