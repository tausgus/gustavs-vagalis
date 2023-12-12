temperaturas = {
    '1.decembris': 0.0,
    '2.decembris': -0.5,
    '3.decembris': 2.0,
    '4.decembris': 1.0,
    '5.decembris': 0.5,
    '6.decembris': -2.0,
    '7.decembris': -2.5,
}

meginajumi = 4
while meginajumi != 0: # Kamēr atlikuši mēģinājumi
    datums = input('Ievadiet datumu [<1-7>.decembris]: ')
    if datums not in temperaturas: # Ja atslēga nav temperatūru vārdnīca
        print('Nepareiza atslēga. Lūdzu, ievadiet datumu no 1. līdz 7. decembrim.')
        meginajumi -= 1 # Mēģinājumu skaitu samazina par 1
    else:
        print(f'{datums} temperatūra Celsija skalā ir: {temperaturas[datums]} grādi\n*****')
        temp_farenheits = temperaturas[datums] * (9/5) + 32 # Formula pārveidošanai no Celsija uz Fārenheitu
        print(f'{datums} temperatūra Fārenheita skalā ir: {temp_farenheits} grādi')
        break # Pēc veiksmīgas temperatūras iegūšanas, programma beidzas
        

