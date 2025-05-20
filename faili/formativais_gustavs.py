import string
# Struktūra - saraksts, kur katrs elements ir saraksts, kurš satur: [vards, uzvards, vecums, gala atzime]
dati = []
ielasitie_dati = []

def varda_parbaude(): # Saņem ievadi, pārbauda, vai ir tikai burti un nav tukšs
    for attempt in range(1,4): # 3 mēģinājumi
        vards = input(f'Ievadiet vārdu (mēģinājums {attempt}/3): ')
        if vards == 'STOP': # Ja nevēlas ievadīt, atgriezīs False, lai šo pēc tam var noķert
            return False
        elif vards != '' and vards.isalpha(): # Ja nav tukšs un sastāv tikai no burtiem
            return vards # Atgriež derīgo vārdu
        else:
            print('! Kļūda - ievade var saturēt tikai burtus un nevar būt tukša.')
    print("! Pārsniegts mēģinājumu skaits")
    quit()

def uzvarda_parbaude(): # Saņem ievadi, pārbauda, vai ir tikai burti un nav tukšs
    for attempt in range(1,4):
        uzvards = input(f'Ievadiet uzvārdu (mēģinājums {attempt}/3): ')
        if uzvards == 'STOP': # Ja nevēlas ievadīt, atgriezīs False, lai šo pēc tam var noķert
            return False
        elif uzvards != '' and uzvards.isalpha(): # tas pats, kas f-jā varda_parbaude()
            return uzvards
        else:
            print('! Kļūda - ievade var saturēt tikai burtus un nevar būt tukša.')
    print("! Pārsniegts mēģinājumu skaits")
    quit()

def vecuma_parbaude():
    for attempt in range(1,4):
        vecums = input(f'Ievadiet vecumu [>0] (mēģinājums {attempt}/3): ')
        if vecums == 'STOP': # Ja nevēlas ievadīt, atgriezīs False, lai šo pēc tam var noķert
            return False
        elif vecums.isdigit() and int(vecums) > 0: # Ja ir vesels skaitlis un lielāks par 0
            return int(vecums) # Atgriež kā int
        else:
            print('! Kļūda - vecums var būt tikai pozitīvs vesels skaitlis.')
    print("! Pārsniegts mēģinājumu skaits")
    quit()

def gala_atzimes_parbaude():
    for attempt in range(1,4):
        gala_atzime = input(f'Ievadiet gala atzīmi [nv=0, 1-10] (mēģinājums {attempt}/3): ')
        if gala_atzime == 'STOP': # Ja nevēlas ievadīt, atgriezīs False, lai šo pēc tam var noķert
            return False
        elif gala_atzime.isdigit() and int(gala_atzime) in range(0,11): # Ja ir no 0 līdz 10 (ieskaitot)
            return int(gala_atzime) # Atgriež kā veselu skaitli
        else:
            print('! Kļūda - gala atzīme var būt pozitīvs vesels skaitlis no 0 līdz 10.')
    print("! Pārsniegts mēģinājumu skaits")
    quit()

def izveles_parbaude(): # Piedāvā bezgalīgi izvēlēties no variantiem
    varianti = [
        "1", # Ievadīt personas datus, STOP - lai pārtrauktu
        "2", # Ierakstīt datus failā kontroldarbs.txt
        "3", # Veic sakārtotu izdruku konsolē, pēc atzīmes
        "4", # Iziet
    ]
    while True:
        izvele = input("Izvēlieties darbību:\n1 - Ievadīt datus\n2 - Saglabāt datus failā\n3 - Parādīt datus no faila, sakārtotus pēc gala atzīmes\n4 - iziet no programmas\nJūsu izvēle: ")
        if izvele in varianti: # Ja izvēle ir viena no iestatītajiem variantiem
            return izvele 
        else:
            print("! Šī nav viena no izvelēm - lūdzu mēģiniet vēlreiz.") # Bezgalīgi mēģina

# Galvenais cikls
print('\t- Atzīmju programma -')
while True:
    match izveles_parbaude():
        case "1":
            print("Ievadiet jaunu ierakstu, vai 'STOP', lai pārtrauktu.")
            while True:
                # Pārbauda, vai kādā neierakstīja stop:
                i_vards = varda_parbaude()
                if i_vards == False:
                    break
                i_uzvards = uzvarda_parbaude()
                if i_uzvards == False:
                    break
                i_vecums = vecuma_parbaude()
                if i_vecums == False:
                    break
                i_gala_atzime = gala_atzimes_parbaude()
                if i_gala_atzime == False:
                    break
                dati.append([i_vards,i_uzvards,i_vecums,i_gala_atzime])
                if input("Vai vēlaties veikt vēl vienu ierakstu? [j - jā/n - nē]: ") == 'n':
                    break
        case "2":
            if dati == []: # Ja lietotājs programmai nav devis jaunus ierakstus
                print("! Kļūda - nav dati, ko ierakstīt.\n")
            else:
                with open('kontroldarbs.txt', 'a', encoding='utf-8') as atzimju_fails: # Atver failu rakstīšanas režīmā
                    for skolens in dati:
                        atzimju_fails.write(f'{skolens[0]},{skolens[1]},{skolens[2]},{skolens[3]}\n') # Ieraksta ar tabulācijas atstarpi
                    print("! Dati veiksmīgi ierakstīi.\n")

        case "3":
            try:
                with open("kontroldarbs.txt", "r", encoding="utf-8") as atzimju_fails: # Atver failu lasīšanas režīmā
                    saturs = atzimju_fails.readlines()
                    if saturs == []:
                        raise FileNotFoundError
                    else:
                        for skolens in saturs:
                            objekts = skolens.split(',') # Atdala ar tabulācijas atstarpi
                            objekts[-1] = objekts[-1].strip('\n') # Noņem liekos simbolus
                            ielasitie_dati.append(objekts)
                        print('\nVārds\tUzvārds\tVecums\tGala atzīme')
                        for skolens in sorted(ielasitie_dati, key=lambda skolens: int(skolens[-1])): # Sakārto datus, ko ieguva no faila pēc saraksta elementa, kas satur atzīmi
                            print(f'{skolens[0]}\t{skolens[1]}\t{skolens[2]}\t{skolens[3]}')
                        ielasitie_dati = [] # Lai nerastos dublikāti
                    
            except FileNotFoundError: # Ja fails nēeksistē:
                print("! Kļūda - fails nēeksistē, vai arī tajā nav dati, ko nolasīt.\n")

        case "4":
            print("! Programma beidzas.")
            quit()