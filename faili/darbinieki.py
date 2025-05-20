import csv 

darbinieku_fails = 'darbinieki.csv'

darbinieki = [
    {"Vārds": "Jānis", "Amats": "Inžinieris", "Alga": 800},
    {"Vārds": "Imants", "Amats": "Galdnieks", "Alga": 500},
    {"Vārds": "Ēriks", "Amats": "Programmētājs", "Alga": 900},
    {"Vārds": "Valdis", "Amats": "Dizaineris", "Alga": 600},
    {"Vārds": "Gunārs", "Amats": "Mākslinieks", "Alga": 600}
]

galvene = ['Vārds', 'Amats', 'Alga']

with open(darbinieku_fails, 'w', encoding='utf-8', newline='') as fails:
    rakstitajs = csv.DictWriter(fails, fieldnames=galvene)
    rakstitajs.writeheader()
    rakstitajs.writerows(darbinieki)

try:
    with open(darbinieku_fails, 'r', encoding='utf-8') as fails:
        lasitajs = csv.DictReader(fails)
        for darbinieks in lasitajs:
            try:
                if int(darbinieks["Alga"]) > 1000:
                    print(f'{darbinieks["Vārds"]} - pārāk liela alga!')
                else:
                    print(f'Vārds: {darbinieks["Vārds"]}, Amats: {darbinieks["Amats"]}, Alga: {darbinieks["Alga"]}')
            except ValueError:
                print(f'{darbinieks["Vārds"]} - nepareiza algas vērtība!')
except FileNotFoundError:
    print(f'Fails {darbinieku_fails} nav atrasts!')