# Sākumā lietotājs izveido savu sarakstu ar skaitļiem
saraksts = []

garums = int(input("Ievadiet skaitļu skaitu [>=10]: "))
while garums < 10: # Cikls, lai prasītu garumu, kamēr tiek ievadīts vismaz 10
    print("Saraksta garums nevar būt mazāks par 10.")
    garums = int(input("Ievadiet skaitļu skaitu [>=10]: "))

for i in range(1, garums+1): # Sāk range no 1, līdz prasītajam garumam
    saraksts.append(int(input(f'Ievadiet {i}. skaitli: '))) # Katru skaitli pievieno sarakstam

print(f'Saraksts ar skaitļiem: {saraksts}')

# Pāra un nepāra skaitļu meklēšana
nr_para, nr_nepara = 0, 0
for j in saraksts:
    if j % 2 == 0: # Dalās ar divi bez atlikuma, tātad pāra
        nr_para += 1
    elif j % 2 > 0: # Dalās ar divi ar atlikumu, tātad nepāra
        nr_nepara += 1

print(f'Pāra skaitļu skaits: {nr_para}\nNepāra skaitļu skaits: {nr_nepara}')