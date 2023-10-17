preces = {}
pabeigts = False

while not pabeigts:
    nosaukums = input("Ievadiet preces nosaukumu [ja viss nopirkts, tad S]: ").lower() # Nosaukumu pārveido uz mazajiem burtiem, lai neveidotos dublikāti vārdnīcā
    if nosaukums == "s": # Ja preces nosaukums tika sniegts kā S, tad saraksts ir aizpildīts.
        pabeigts = True
        break

    cena = float(input("Ievadiet preces cenu [>0]: "))
    if cena <=0: quit() # Uzreiz pārbauda atbildi
    daudzums = float(input("Ievadiet preces daudzumu [>0]: "))
    if daudzums <=0: quit()

    preces[nosaukums] = cena * daudzums # Ievieto kopējo cenu precei vārdnīcā

    print('\t--- Preces:',end=' ') # Izdrukā aktuālo sarakstu ik katru ciklu
    for item in preces:
        print(item,end=',')
    print(' ---')

kopsumma = 0  
print('\t --- Čeks ---')
for item in preces:
    print(f'{item}: {preces[item]}€') # Priekš katras preces vārdnīcā, izprintē tās nosaukumu un kopējo cenu
    kopsumma += preces[item] # Tad to pieskaita kopsummai
print(f'\t= {kopsumma}€')

print('\t --- Iespējamās cenas ar atlaidi: ---')
ir_karte = (input("Vai jums ir klienta karte? [j/n]: ") == 'j') # Inputu pārveido uz True, ja atbild j
print(f'30%: {round(kopsumma - 0.3*kopsumma)}€') # 30% atlaide ir visiem
if ir_karte:
    print(f'40%, ar klienta karti: {round(kopsumma - 0.4*kopsumma)}€') # 40% un 50% atlaides dod, ja ir karte
    print(f'50%, ar klienta karti: {round(kopsumma - 0.5*kopsumma)}€')
else:
    print(f'20%: {round(kopsumma - 0.2*kopsumma)}€') # Ja nav karte, tad tikai 20%

if len(preces) >= 3:
    print(f'30%: {round(kopsumma - 0.3*kopsumma)}€') # Ja vairāk vai tieši trīs preces, 30% atlaide

print(f'Katra otrā par brīvu: {round(kopsumma/2)}€') # Katra otrā par brīvu -> puse no cenas