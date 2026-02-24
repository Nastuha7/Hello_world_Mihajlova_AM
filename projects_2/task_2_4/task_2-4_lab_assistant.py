volume = float(input("Введите объём раствора (мл): "))
salt_mass = volume * 0.009
water_volume = volume
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"Отчёт по приготовлению\n-----------------------\nОбщий объем: \t{volume} мл\nМасса соли: \t{round(salt_mass, 2)} г\nОбъем воды: \t{water_volume} мл")