phenotype_p = input("Введите фенотип группы крови пациента(I, II, III, IV): ").strip().upper()
phenotype_d = input("Введите фенотип группы крови донора(I, II, III, IV): ").strip().upper()
if phenotype_d == "I" or phenotype_d == phenotype_p:
    print("Переливание рекомендуется")
else:
    print("Переливание не рекомендуется")