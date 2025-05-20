# ierakstīt tekstu failā ar input metodi, failu izveido programma
# txt fails
def rakstit():
    with open('fails.txt', 'a', encoding='utf-8') as fails:
        for i in range(6):
            fails.write(input(f"Ievadiet {i+1}. ierakstu failam: ") + '\n')
    print("Teksts ierakstīts!")
#rakstit()

# nolasīt tekstu no faila, ja nav, informē
def lasit():
    try:
        with open('fails.txt', 'r', encoding='utf-8') as fails:
            print(f'Faila saturs: \n{fails.read()}')
    except FileNotFoundError:
        print('Fails nav atrasts!')
#lasit()

def lasit_ar_ciklu():
    try:
        with open('fails.txt', 'r', encoding='utf-8') as fails:
            print(f'Faila saturs: \n{fails.read()}')
            for rindina in fails.readlines():
                print(f"{rindina.strip('\n')}")
    except FileNotFoundError:
        print('Fails nav atrasts!')
#lasit_ar_ciklu()

# izveido sarakstu ar 3 vārdiem, to pievieno failam, parāda konsolē, cik vārdi ir pievienoti
def rakstit_no_saraksta():
    saraksts = ["Pirmais", "Otrais", "Trešais"]
    with open('fails.txt', 'a', encoding='utf-8') as fails:
       fails.writelines([vards+'\n' for vards in saraksts])
    print(f"Failā ierakstīti {len(saraksts)} vārdi.")
#rakstit_no_saraksta()

# ievada vārdu, ko meklēt failā, informēt, vai ir vai nav
def meklet():
    try:
        with open('fails.txt', 'r', encoding='utf-8') as fails:
            if input("Ievadiet vārdu, ko meklēt: ") in fails.read():
                print("Vārds atrasts failā!")
            else:
                print("Vārds nav atrasts!")
    except FileNotFoundError:
        print('Fails nav atrasts!')
#meklet()

# sakārtot failā esošos datus dilstošā secībā
def sakartot():
    try:
        with open('fails.txt', 'r', encoding='utf-8') as fails:
            saturs = fails.readlines()
        with open('fails.txt', 'w', encoding='utf-8') as fails:
            fails.writelines(sorted(saturs, reverse=True))
    except FileNotFoundError:
        print('Fails nav atrasts!')
#sakartot()