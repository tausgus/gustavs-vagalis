#int pārveidošana par str
a = 5
b = 7
print(f'Skaitlis: {a + b}')
print(f'Teksts: {str(a) + str(b)}') # Concat metode'

# Izveidot 2 str tipa mainīgos ('123', '456')
# Pārveidot šos mainīgos par int tipu
# Noteikt datu tipu 

pirmais, otrais = '123', '456'
pirmais_skaitlis, otrais_skaitlis = int(pirmais), int(otrais)
print(f'Summa: {pirmais_skaitlis + otrais_skaitlis}')
print(f'Pirmā datu tips: {type(pirmais_skaitlis)}\nOtrā datu tips: {type(otrais_skaitlis)}')