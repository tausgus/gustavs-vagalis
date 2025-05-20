import csv
faila_nosaukums = 'pilsetas.csv'
galvene = ["nosaukums", "iedzīvotāju skaits"]

# 1. uzdevums
def ierakstit_pilsetas():
    with open(faila_nosaukums, 'w', encoding='utf-8', newline='') as fails: # Atver failu, pārrakstot
        rakstitajs = csv.DictWriter(fails, fieldnames=galvene)
        rakstitajs.writeheader()
        for pilseta_nr in range(5):
            while True:
                nosaukums = input(f"Ievadiet {pilseta_nr+1}. pilsētu: ")
                iedzivotaju_skaits = input(f'Ievadiet iedzīvotaju skaitu: ')
                ievade = {
                    "nosaukums": nosaukums, # Izveido vārdnīcu ar attiecīgajām galveņu atslēgām
                    "iedzīvotāju skaits": iedzivotaju_skaits,
                }
                if ievade["nosaukums"].strip() != "" and ievade["iedzīvotāju skaits"].strip() != "": # Ja nav tukša ievade
                    # Ieraksta rindiņu
                    rakstitajs.writerow(ievade)
                    break
                else:
                    print("! Kļūda - pilsētas ievade nevar būt tukša.")

# 2. uzdevums
# parāda visas pilsētas, starp katru atdalītājs
def izvadit_pilsetas():
    try:
        with open(faila_nosaukums, 'r', encoding='utf-8') as fails:
            print(f"Pilsētas failā {faila_nosaukums}: ")
            lasitajs = csv.DictReader(fails)
            for rindina in lasitajs: # Ignorē galveni
                print(f'{rindina["nosaukums"]}, iedzīvotāju skaits {rindina["iedzīvotāju skaits"]}\n{"-"*16}')
    except FileNotFoundError:
        print(f'! Kļūda - fails {faila_nosaukums} netika atrasts.')

# 3. uzdevums
# summē iedzīvotāju skaitu, nepārbaudot, vai tiešām ir skaitlis
def izvadit_iedzivotaju_n():
    try:
        with open(faila_nosaukums, 'r', encoding='utf-8') as fails:
            lasitajs = csv.DictReader(fails)
            # Savāc summu no ailes "iedzīvotāju skaits"
            summa = 0
            for pilseta in lasitajs:
                summa += int(pilseta["iedzīvotāju skaits"])
            # To izdrukā
            print(f'Kopējais iedzīvotāju skaits: {summa}')
    except FileNotFoundError:
        print(f'! Kļūda - fails {faila_nosaukums} netika atrasts.')

# Visu funkciju izsaukumi
ierakstit_pilsetas()
izvadit_pilsetas()
izvadit_iedzivotaju_n()