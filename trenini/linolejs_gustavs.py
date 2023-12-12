from math import ceil, sqrt
print('\t- Grīdas maiņas izmaksu aprēķins -')

cena = float(input("Linoleja cena [€/m²]: "))
platums = float(input("Linoleja ruļļa platums [m]: "))
laukums = float(input("Telpas platība [m²]: "))

def uzskaite(s, w): # Uzskaites funkcija (telpas laukums, linoleja platums)
    return s * (sqrt(s) * w) # Laukums tiek pārveidots uz platumu un izdalīts ar linoleja platumu

def aprekins(p, s): # Cenas aprēķins, cena par m2 un vajadzīgais laukums
    return ceil(s) * p 

print('\t- Aprēķinātie daudzumi -')

print(f'Vajadzīgais linoleja daudzums: {round(uzskaite(laukums, platums))} m²')
print(f'Neizmantotais linolejs: {round(laukums - uzskaite(laukums, platums))} m²')
print(f'Kopējā cena: {aprekins(cena, uzskaite(laukums, platums))}€')