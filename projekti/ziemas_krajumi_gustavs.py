from math import ceil
aboli = float(input("Cik kg ābolu? [>=0]: "))
ir_ievarijuma = (input("Tiks izmantots ievārījuma vai parastais cukurs? [i/p]: ") == "i") # Ja atbild i, tad pārveido uz bool
if input("Vai jums ir labi ar sirdi? [j/n]: ") != 'j':
    exit()

# Receptes proporcijas: 1 kg āboli : 300 g cukurs : 160 ml ūdens : 1/3 citrons : 1.6 ml mandeļu ekstrakts : 3.3 g kanēlis

cenas = {
    "cukurs": 0.00126, # 1 g
    "ievārījuma cukurs": 0.0028, # 1g
    "citrons": 0.67, # 1 gab
    "ūdens": 0.00017, # 1 ml 
    "mandeļu ekstrakts": 0.08, # 1 ml 
    "kanēlis": 0.03 # 1 g
}

recepte = {
    "cukurs": 300.0,
    "ievārījuma cukurs": 250.0,
    "citrons": 0.3,
    "ūdens": 160.0,
    "mandeļu ekstrakts": 1.6,
    "kanēlis": 3.3
}

produkti = {}

# Pieejamo produktu pārbaude
print('\t- Pieejamie produkti -')

vajadzigie = ['cukurs','citrons', 'ūdens','mandeļu ekstrakts', 'kanēlis']
if ir_ievarijuma:
    vajadzigie[0] = 'ievārījuma cukurs'

for produkts in vajadzigie: # Priekš katras sastāvdaļas pērkamo sarakstā, paprasa vai tas atrodas mājās
    produkti[produkts] = float(input(f'Cik daudz mājās ir {produkts}? [daudz./0]: '))  

print('\t- Pirkumu saraksts -')

kopsumma = 0

for produkts in produkti:
    if (recepte[produkts] * aboli - produkti[produkts]) <= 0: # Atņem jau esošā produkta daudzumu no vajadzīgā, lai uzzinātu, vai vēl jāpērk
        print(f'* {produkts} nav jāpērk, mājās ir pietiekami.')
    else:
        # Ar formulu (<vajadzīgais daudzums> - <esošais daudzums>) * cena aprēķina tikai vajadzīgā produkta cenu, to noapaļo
        vajadziga_cena = round((recepte[produkts] * aboli - produkti[produkts]) * cenas[produkts], 2) 
        print(f'* {recepte[produkts] * aboli - produkti[produkts]} {produkts} = {vajadziga_cena}€')
        kopsumma += vajadziga_cena        

print(f'\t- Kopsumma: {ceil(kopsumma)}€ -')