valstis = {
    "Vācija": 83294633,
    "Norvēģija": 5474360,
    "Somija": 5545475,
    "Šveice": 8796669,
    "Čehija": 10495295,
    "Grieķija": 10341277,
    "Latvija": 1830211,
    "Luksemburga": 654768,
    "Islande": 375318,
    "Ukraina": 36744634,
}

print('\t- Valstu programma -')
print('1 - sakārto pēc nosaukuma, augoša secība')
print('2 - sakārto pēc nosaukuma, dilstoša secība')
print('3 - sakārto pēc iedzīvotāju skaita, augoša secība')
print('4 - sakārto pēc nosaukumiem, dilstoša secība')
print('5 - pievieno jaunu valsti un tās iedz. skaitu')
print('6 - apskata visas valstis')
print('stop - apstādina programmu')
print('\t\t---')

def formateta_izdruka(atslegas): # Saņem sarakstu ar atslēgām, kas jau sakārtotas vajadzīgajā veidā ārpus funkcijas
    for atslega in atslegas: 
        print(f'* {atslega} - {valstis[atslega]} iedzīvotāji') # Tad ar šīm atslēgām izdrukā valsti
    print('\t\t---')

while True:
    izvele = input("Izvēlaties vēlamo darbību [1/2/3/4/5/6/stop]: ")
    if izvele == "stop":
        print('\t! Programma apstādināta')
        break # Iziet no bezgalīgā while cikla
    elif izvele == "1":
        print('\t- Valstu nosaukumi augošā secībā -')
        formateta_izdruka(sorted(valstis)) # Nemodificē oriģinālo vārdnīcu
    elif izvele == "2":
        print('\t- Valstu nosaukumi dilstošā secībā -')
        formateta_izdruka(sorted(valstis, reverse=True)) 
    elif izvele == "3":
        print('\t- Valstis pēc iedzīvotājiem augošā secībā -')
        formateta_izdruka(sorted(valstis, key=valstis.get)) # ar key izmanto vērtību kārtošanai, nevis atslēgu
    elif izvele == "4":
        print('\t- Valstis pēc iedzīvotājiem dilstošā secībā -')
        formateta_izdruka(sorted(valstis, key=valstis.get, reverse=True)) 
    elif izvele == "5":
        print('\t- Jaunas valsts ievade -')
        # Nosaukumu drošības pēc automātiski pārveido ar lielo pirmo burtu
        nosaukums, iedz_sk = input("Ievadiet vēlamo valsts nosaukumu [str]: ").capitalize(), int(input("Ievadiet valsts iedzīvotāju skaitu [vesels skaitlis]: "))
        valstis[nosaukums] = iedz_sk # Pievieno jaunu valsti ar atslēgu kā ievadīto nosaukumu un vērtību kā iedz. skaitu
        print(f'\t- Valsts {nosaukums} ar iedzīvotāju skaitu {iedz_sk} pievienota veiksmīgi! -') 
    elif izvele == "6":
        print('\t- Visu valstu izdruka -')
        formateta_izdruka(valstis)