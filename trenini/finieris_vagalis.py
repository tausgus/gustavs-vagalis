# Konstantās cenas
cenas = {
    "liste": 0.41,
    "sturis": 0.29,
}

print('\t- Podesta pasūtījums -')
skaits = int(input('Ievadiet podestu skaitu [>=1]: '))
# Ievieto katru dimensiju sarakstā
dimensijas = [float(input('Ievadiet podesta garumu [>0 mm]: ')), float(input('Ievadiet podesta platumu [>0 mm]: ')), float(input('Ievadiet podesta augstumu [>0 mm]: '))] 
biezums = int(input('Ievadiet plāksnes biezumu [12-21 mm]: '))

def materialuUzskaite(tips, skaits, dimensijas=[]):
    match tips:
        case "finieris":
            # S = 2(ab+ah+bh) * n, paralēlskaldņa laukums
            return 2 * (dimensijas[0]*dimensijas[1] + dimensijas[0]*dimensijas[2] + dimensijas[1]*dimensijas[2]) * skaits
        case "liste":
            # Ja vairāki, tad 12 līstes starp katru pāri
            if skaits == 1:
                return 0
            else:
                return skaits * 12 - 12
        case "sturis":
            # Katram 8 stūra savienojumi
            return 8 * skaits

# Finiera cena uz m2 ir aptuveni vienāda ar biezumu (prof.lv).

def materialuAprekins(skaits, dimensijas):
    summa = 0.0

    summa += materialuUzskaite("finieris", skaits, dimensijas) / 1000000 * biezums
    summa += materialuUzskaite("liste", skaits) * cenas["liste"]
    summa += materialuUzskaite("sturis", skaits) * cenas["sturis"]

    return summa

        
print('\t- Materiālu uzskaite -')
print(f'* Dimensijas: {dimensijas[0]}x{dimensijas[1]}x{dimensijas[2]} mm, ar biezumu {biezums} mm')
print(f'* Skaits: {skaits} gab.\n\tMateriāli >>>')
print(f'* Finieris: {materialuUzskaite("finieris", skaits, dimensijas) / 1000000} m2')
print(f'* Leņķveida līstes: {materialuUzskaite("liste", skaits)} gab.')
print(f'* Stūra savienojumi: {materialuUzskaite("sturis", skaits)} gab.')

print(f'\t- Izmaksas -')
print(f'* Cena par vienu vienību: {round(materialuAprekins(1, dimensijas),2)}€')
print(f'* Kopsumma par {skaits} vienībam: {round(materialuAprekins(skaits, dimensijas),2)}€')