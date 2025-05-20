
def apskatit(saraksts): # Izdrukā visas mašīnas (piem, * Volvo V70, 2007. gada) un tās indeksu
    if saraksts == []:
        print("- Nav mašīnu, ko parādīt! -")
    else: 
        print('- Mašīnu saraksts -')
    for masina in saraksts:
        print(f'[{saraksts.index(masina)}] {masina[1]} {masina[0]}, {masina[2]}. gada')

def pievienot(saraksts): # Pievieno sarakstam mašīnu pēc formāta
    print('- Mašīnas pievienošana -')
    marka = input("Ievadi mašīnas marku: ") 
    modelis = input("Ievadi mašīnas modeli: ")
    gads = int(input("Ievadi mašīnas gadu: "))
    saraksts.append([modelis, marka, gads]) # Pareizā secībā


def atjauninat(saraksts): # Atjaunina mašīnu ar konkrēto indeksu
    print('- Mašīnas atjaunināšana -')
    indekss = int(input('Ievadi indeksu mašīnai, ko gribi atjaunināt: '))
    marka = input("Ievadi jauno marku: ") 
    modelis = input("Ievadi jauno modeli: ")
    gads = int(input("Ievadi jauno gadu: "))
    saraksts[indekss] = [modelis, marka, gads] # Pareizā secībā
    print('- Mašīna atjaunināta. -')

def dzest(saraksts): # Dzēš mašīnu
    print('- Mašīnas dzēšana -')
    indekss = int(input('Ievadi indeksu mašīnai, ko gribi dzēst: '))
    try:
        saraksts.pop(indekss)
        print('- Mašīna dzēsta. -')
    except IndexError:
        print('- Mašīna ar šādu indeksu nav atrasta! -')

# Satur sarakstus, ar formātu [modelis, marka, gads]
masinas = []

while True:
    match input("Ko vēlies darīt? [1 - apskatīt/2 - pievienot/3 - atjaunināt/4 - dzēst/5 - iziet]: "):
        case "1":
            apskatit(masinas)
        case "2":
            pievienot(masinas)
        case "3":
            atjauninat(masinas)
        case "4":
            dzest(masinas)
        case "5":
            print("- Programma beidzas. -")
            break
        case _:
            print("- Šāda izvēle nav pieejama. -")
        
