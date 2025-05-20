faila_nosaukums = 'pilsetas.txt'

# 1. uzdevums
# izveido teksta failu to pārrakstot, un ļauj ierakstīt 10 Latvijas pilsētas
# tukšas ievades pārbaude
def ievadit_pilsetas():
    with open(faila_nosaukums, 'w', encoding='utf-8') as fails:
        for pilseta_nr in range(10):
            while True:
                ievade = input(f"Ievadiet {pilseta_nr+1}. pilsētu: ")
                if ievade.strip() != "": # Ja nav tukša ievade
                    fails.write(f'{ievade}\n')
                    break
                else:
                    print("! Kļūda - pilsētas ievade nevar būt tukša.")
        print(f"Pilsētas ierakstītas failā {faila_nosaukums}.")

# 2. uzdevums
# nolasa failu ar for ciklu, noņemot liekās atstarpes
# ja fails neeksistē - kļūda
# pēdējā rinda - līnija
def izvadit_pilsetas():
    try:
        with open(faila_nosaukums, 'r', encoding='utf-8') as fails:
            print(f"Faila {faila_nosaukums} saturs: ")
            for rindina in fails.readlines():
                print(rindina.strip()) # Noņem liekos newline simbolus
            print('-'*16)
    except FileNotFoundError:
        print(f'! Kļūda - fails {faila_nosaukums} netika atrasts.')

# 3. uzdevums
# izvada alfabētiski sakārotas pilsētas
def izvadit_kartotas_pilsetas():
    try:
        with open(faila_nosaukums, 'r', encoding='utf-8') as fails:
            print(f"Sakārtots {faila_nosaukums} saturs: ")
            for pilseta in [nosaukums.strip() for nosaukums in sorted(fails.readlines())]: # Ņem katru rindiņu sarakstā, ar konstruktoru noņem liekos simbolus, to sakārto
                print(pilseta)
            print('-'*16)
    except FileNotFoundError:
        print(f'! Kļūda - fails {faila_nosaukums} netika atrasts.')

# 4. uzdevums
# pievieno trīs pilsētas ar pārbaudi
def papildinat_pilsetas():
    papildinajums = []

    try:
        with open(faila_nosaukums, 'r', encoding='utf-8') as fails: # Sākumā nosaka jau eksistējošās pilsētas
            esosas = [pilseta.strip() for pilseta in fails.readlines()]
    except FileNotFoundError:
        print(f'! Kļūda - fails {faila_nosaukums} netika atrasts.')
    
    for pilsetas_nr in range(3): # Prasa ievadi trīs reizes, kamēr izdodas
        while True:
            ievadita_pilseta = input(f"Ievadi {pilsetas_nr+1}. pilsētu, kuru pievienot: ")
            if ievadita_pilseta.strip() not in esosas: # Ja pilsēta jau neeksistē, to pievieno
                papildinajums.append(ievadita_pilseta.strip())
                break
            else:
                print("! Kļūda - ievadītā pilsēta failā jau pastāv. Mēģini vēlreiz.")

    # Papildinājumu ieraksta failā
    with open(faila_nosaukums, 'a', encoding='utf-8') as fails:
        fails.writelines([izlabots+'\n' for izlabots in papildinajums]) # Pievieno ievadei newline
    print(f'Failam {faila_nosaukums} pievienotas {len(papildinajums)} pilsētas: ', end=' ')
    for pilseta in papildinajums:
        print(pilseta, end=', ')

# Funkciju izsaukumi secībā
ievadit_pilsetas()
izvadit_pilsetas()
izvadit_kartotas_pilsetas()
papildinat_pilsetas()