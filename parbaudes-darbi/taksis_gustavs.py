pasazieri = int(input('Cik pasažieri? [1-3]: '))
laiks = int(input('Ievadiet laiku veselās stundās [0-24]: '))
# Ja ir stāvvietā, tad True - ja cita atbilde, tad False ar salīdzinājuma operatora palīdzību
stavvieta = (input('Vai taksometrs atrodas stāvvietā? [j/n]: ') == 'j')
gaidisana = int(input('Gaidīšanas laiks minūtēs, [nav - 0]: '))
attalums = int(input('Cik tālu jābrauc? (km): '))

# Bonuss, taksis neved vairāk kā 2 čemodānus
cemodani = int(input('Cik čemodānus plānojat vest? [nav - 0]: '))

# Inicializē float tipa mainīgo kopsummai, lai turpmāk var pieskaitīt visu
kopsumma = 0.0

# Tarifi
tarifs_n = 0.77
tarifs_d = 0.37
izsaukums = 2.50
noligsana = 2.00

# Sākumā atbilžu pārbaudes neloģiskiem skaitļiem, kā negatīvu attālumu vai vairāk kā 3 pasažieru (exit ja kaut vai 1 neatbilst)
if pasazieri < 1 or pasazieri > 3 or laiks > 24 or laiks < 0 or gaidisana < 0 or attalums < 0: 
    print('! Ievadi pareizus datus')
    exit()
elif cemodani > 2: # Bonuss, taksis neved vairāk kā 2 čemodānus
    print('! Jums ir par daudz čemodānu - taksis vairāk kā divus neved.')
    exit()
else: # Turpina, ja atbilžu pārbaudes veiksmīgas
    # Čeks skaistumam
    print('\n\t--- TAKSOMETRA ČEKS ---')
    print(f'Izsaukuma laiks: {laiks}:00')
    print(f'Papildus gaidīšanas laiks: {gaidisana} minūtes')
    print(f'Attālums: {attalums} kilometri')
    print('\t--- Tarifu aprēķins ---')

    # Attāluma un tarifa reizinājumu pieskaita kopsummai
    if laiks in [23,0,1,2,3,4,5]: # Nakts tarifu stundas atrodas kopā, un pārbauda vai dotais laiks ar kādu no kopas sakrīt.
        kopsumma += (attalums * tarifs_n)
        print(f'Attāluma summa (nakts): {attalums} km * {tarifs_n}€ = {kopsumma}€') # Katrā solī izdrukā formatētu virkni čekam
    else: # Ja nav nakts tarifs, tad - diena
        kopsumma += (attalums * tarifs_d)
        print(f'Attāluma summa (dienas): {attalums} km * {tarifs_d}€ = {kopsumma}€')
    
    # Izsaukšana un nolīgšana
    if not stavvieta: # Ja nav stāvvietā, kopsummai pieskaita gan nolīgšanas, gan izsaukuma maksu.
        kopsumma += (noligsana + izsaukums)
        print(f'Izsaukums (neatradās stāvvietā): {izsaukums}€ + {noligsana}€ = {noligsana + izsaukums}€')
    else: # Ir stāvvietā
        kopsumma += (noligsana)
        print(f'Izsaukums (no stāvvietas): {noligsana}€')

    # Gaidīšana (nevajag if, ja gaida 0 minūtes reizinājums būs 0)
    kopsumma += (0.15 * gaidisana)
    print(f'Gaidīšana: 0.15 * {gaidisana} min = {0.15 * gaidisana}€')

    print(f'\t--- Kopsumma ---\n\t   [ {kopsumma}€ ]\n\nPaldies par braucienu!')

