saraksts = []

garums = int(input("Ievadiet skaitļu skaitu [>=3]: "))
while garums < 3: # Cikls, lai prasītu garumu, kamēr tiek ievadīts vismaz 3
    print("Saraksta garums nevar būt mazāks par 3.")
    garums = int(input("Ievadiet skaitļu skaitu [>=3]: "))

for i in range(1, garums+1): # Sāk range no 1, līdz prasītajam garumam
    saraksts.append(int(input(f'Ievadiet {i}. skaitli: '))) # Katru skaitli pievieno sarakstam
print(f'Saraksts ar skaitļiem: {saraksts}')

# Lielākā skaitļa atrašanai izmanto max funkciju, efektīvāk nekā for cikls.
print(f'Lielākais ievadītais skaitlis: {max(saraksts)}')
