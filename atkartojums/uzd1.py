# izdrukāt visus nepāra skaitļus no lietotāja ievadītā diapazonas
start, end = int(input("Ievadiet sākuma skaitli: ")), int(input("Ievadiet beigu skaitli: "))
print("Nepāra skaitļi: ", end='')
for i in range(start, end+1):
    if i % 2 != 0:
        print(i, end=', ')