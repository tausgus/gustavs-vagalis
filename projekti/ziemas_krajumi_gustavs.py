from math import ceil
aboli = float(input("Cik kg ābolu? [>=0]: "))
ir_ievarijuma = (input("Tiks izmantots ievārījuma vai parastais cukurs? [i/p]: ") == "i") # Ja atbild i, tad pārveido uz bool
perkamie_produkti = []

# Receptes proporcijas: 1 kg āboli : 300 g cukurs : 160 ml ūdens : 1/3 citrons : 1.6 ml mandeļu ekstrakts : 3.3 g kanēlis

# Cenu karte proporcijās uz 1 kg āboliem, eiro.
cenas = {
    "cukurs": 0.5, # 300 g
    "citrons": 0.13, # 1/3 
    "ūdens": 0.07, # 160 ml 
    "mandeļu ekstrakts": 0.16, # 1.6 ml 
    "kanēlis": 0.24 # 3.3 g
}

# Pieejamo produktu pārbaude
print('\t- Pieejamie produkti -')
for produkts in ['cukurs','citrons', 'ūdens','mandeļu ekstrakts', 'kanēlis']: # Priekš katras sastāvdaļas pērkamo sarakstā, paprasa vai šis atrodas mājās
    if (input(f'Vai mājās ir pieejams {produkts}? [j/n]: ') == 'n'): # Ja atbild n, tad pievieno produktu pērkamo sarakstam
        perkamie_produkti.append(produkts)
    else:
        continue

# un parāda, tos ko jāpērk
if perkamie_produkti != []:
    print('! Vēl jānopērk: ',end='')
    for produkts in perkamie_produkti:
        print(produkts,end=', ')
    print('.\n')
else:
    print('! Visi produkti ir pieejami')

print(f'\t- Apkopojums -\nPriekš {ceil(aboli)}kg āboliem vajadzīgs:')
# Paņem katru produktu kas ir pērkamo sarakstā (par tiem, kas jau ir mājās nav jāmaksā)
kopsumma = 0
for produkts in perkamie_produkti:
    # Tā cenu iegūst no cenu kartes un sareizina ar ābolu daudzumu, jo visas cenas ir norādītas proporcijā ar 1 kg āboliem.
    kopsumma += cenas[produkts] * aboli
    print(f'{produkts} - {cenas[produkts] * aboli}€') 
print(f'\t[ Summa: {ceil(kopsumma)}€ ]')