
print("Divciparu skaitļu summas aprēķins")
divciparu_skaitlis = int(input('Ievadiet divciparu skaitli: '))

#ciparu iegūšana
pirmais_cipars, otrais_cipars = int(divciparu_skaitlis / 10), int(divciparu_skaitlis % 10)

#pirmā cipara izdruka
print(f'Pirmais cipars: {pirmais_cipars}')
#Otrā cipara izdruka
print(f'Otrais cipars: {otrais_cipars}')
#Summas izdruka
print(f'Ciparu summa: {pirmais_cipars + otrais_cipars}')