files = ["seq1", "seq2", "seq3", "seq4"]
date = input("Введите дату: ")
for name in files:

   new_name = name + f".fasta/{date}"

   print(f"{new_name}")