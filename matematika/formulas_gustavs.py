import math 
import random

r=float(input('Ievadiet rinķa līnijas rādiusu: '))
print(r)
# Rinķa līnijas garuma un laukuma aprēķins pēc formulas, un noapaļošana līdz 2 skaitļiem aiz komata
print(f'Riņķa līnijas garums: {round(2*math.pi*r, 2)} \nRiņķa līnijas laukums: {round(math.pi*r**2, 2)}')
 
# Taisnleņķa trijstūra hipotenūzas garuma aprēķins ar forumulu un noapaļošana līdz 2 skaitļiem aiz komata
k1=float(input('Ievadiet taisnleņķa trijstūra pirmās katetes garumu: '))
k2=float(input('Ievadiet taisnleņķa trijsūtra otrās katetes garumu: '))
print(f'Taisnleņķa trijstūra hipotenūzas garums: {round(math.sqrt(k1**2+k2**2), 2)}')

# Nejauša float skaitļa izvēle no 0 - 1
print(f'Gadījuma skaitlis no 0 - 1:  {random.random()}')