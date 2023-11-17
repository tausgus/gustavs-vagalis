telefons = {
    'Jānis': 259623521,
    'Rita': 26534981,
    'Anna': 23999182,
}
# Jānim ir 2 tel. nr.
print(f'šis ir Jāņa tel. nr.: {telefons["Jānis"]}')

# Vārdnīca, nenorādot vērtības

kk = ('viens', 'divi', 'trīs')
dd = dict.fromkeys(kk)
print(dd)

val = 0
dd = dict.fromkeys(kk,val)
print(dd)

# Izveidot vārdnīcu, kas satur sarakstu
valstis = {
    'Itālija': ['Roma', 'Neapole', 'Venēcija'],
    'Somija': ['Helsinki', 'Tampere', 'Turku'],
    'Latvija': ['Rīga', 'Sigulda', 'Liepāja']
}

for atslega, vertiba in valstis.items():
    for i in vertiba:
        print(f'{atslega}: {i}')