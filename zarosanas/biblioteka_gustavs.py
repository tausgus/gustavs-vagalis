ir_personals = (input('Vai jūs esat personāls vai students? [p/s]: ') == 'p') # Ja personāls, tad bool - True
izdevums = input('Vai izdevums ir grāmata vai žurnāls? [g/z]: ')

# Ja atbild jā, tad pārveido uz bool
pieprasits = (input('Vai izdevums ir pieprasīto sarakstā? [j/n]: ') == 'j') 
ir_nenodoti = (input('Vai jums ir kādi laikā nenodoti izdevumi: [j/n]: ') == 'j')

if ir_nenodoti: # Pirmā pārbaude - uzreiz izslēdz nenodotus
    print('Jums ir laikā nenodoti izdevumi - vairāk grāmatas netiks izsniegtas.')
elif pieprasits: # Nav vajadzīga amata kontrole, pieprasītie izdevumi tiek vienmēr izsniegti uz 2 dienām
    print('Izdevums ir pieprasīts - izsniegts uz 2 dienām.')
elif izdevums == 'z' and not pieprasits: # Žurnālus, kas nav pieprasīti gan personālam, gan studentam izsniedz uz 7 dienām.
    print('Žurnāls, nav pieprasīts - izsniegts uz 7 dienām.')
elif izdevums == 'g' and not pieprasits: # Ja grāmata, tad pārbauda, vai personāls vai students.
    if ir_personals:
        print('Grāmata, personālam - izsniegta uz 28 dienām.')
    else:
        print('Grāmata, studentam - izsniegta uz 14 dienām.')