import string
import random

horoskopi = [
    "Auns", "Vērsis", "Dvīņi", "Vēzis", \
    "Lauva", "Jaunava", "Svari", "Skorpions", \
    "Strēlnieks", "Mežāzis", "Ūdensvīrs", "Zivis"
]

apgalvojumi = []
teicieni = []
rikojumi = []

def prognoze(horoskopa_nosaukums, teicienu_saraksts, apgalvojumu_saraksts, rikojumu_saraksts):
    random.shuffle(teicienu_saraksts)
    random.shuffle(apgalvojumu_saraksts) # Sarakstu elementus sajauc vietām nejaušā kārtībā
    random.shuffle(rikojumu_saraksts)
    print(f'\t--- {horoskopa_nosaukums} ---')
    print(f'Apgalvojums: {teicienu_saraksts.pop().capitalize()}, {random.choice(["taču", "bet", "jo"])} {apgalvojumu_saraksts.pop()}.')
    print(f'Apgalvojums: {apgalvojumu_saraksts.pop().capitalize()}, un {apgalvojumu_saraksts.pop()}.') # .pop bez argumentiem noņem pēdējo elementu un to atgriež
    print(f'Rīkojums: {rikojumu_saraksts.pop().capitalize()}.')

# Sarakstu piepildīšana
for faila_nosaukums in ["apgalvojumi", "teicieni" , "rikojumi"]: # Automātiski iziet cauri visiem 3 failiem
    fails = open(f'svg/gustavs-vagalis/projekti/astrologs/{faila_nosaukums}.txt', 'r') # Atver tikai lasīšanas režīmā
    for apgalvojums in fails: # Katra līnija - apgalvojums, to pievieno sarakstam, noņemot lieko newline kodu
        globals()[faila_nosaukums].append(apgalvojums.strip("\n")) # Ar globals pārveido str uz mainīgā nosaukumu no for loop saraksta
    fails.close()

izvele = input("Ievadiet horoskopa nosaukumu vai 0, lai izdrukātu pilnu prognožu lapu: [nosaukums/0]: ")
if izvele == "0":
    for horoskops in horoskopi:
        prognoze(horoskops, teicieni, apgalvojumi, rikojumi) # Atkārto prognozes funkciju katram horoskopam
else:
    prognoze(izvele.capitalize(), teicieni, apgalvojumi, rikojumi) # Veic prognozi tikai izvēlētajam