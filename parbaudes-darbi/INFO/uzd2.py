import csv

galvene = ["ID", "Name", "Age"]

# funkcija, kas izveido csv failu un ieraksta trīs rindas
def izveido():
    rindinas = [
        {"ID": "3", "Name": "Pārbaude", "Age": "21"}
    ]
    with open('fails.csv', 'w', encoding='utf-8', newline='') as fails:
        rakstitajs = csv.DictWriter(fails, fieldnames=galvene)
        rakstitajs.writeheader()
        rakstitajs.writerows(rindinas)
#izveido()

# parādī saturu uz ekrāna
def lasa():
    try:
        with open('fails.csv', 'r', encoding='utf-8') as fails:
            lasitajs = csv.DictReader(fails, fieldnames=galvene)
            for row in lasitajs:
                print(f'{row[galvene[0]]}\t{row[galvene[1]]}\t{row[galvene[2]]}')
    except FileNotFoundError:
        print("Fails nav atrasts!")
#lasa()

# pievienot jaunu id, vārdu, vecumu ar input
def pievieno():
    with open('fails.csv', 'a', encoding='utf-8', newline='') as fails:
        rakstitajs = csv.DictWriter(fails, fieldnames=galvene)
        rakstitajs.writerow(
            {
                "ID": input("Ievadiet ID: "),
                "Name": input("Ievadiet vārdu: "),
                "Age": input("Ievadiet vecumu: ")
            }
        )
    print("Dati pievienoti.")
pievieno()
