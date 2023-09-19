import math 
import random
print("Ievadiet riņķa līnijas rādiusu:")
r=float(input())
print(r)
print(f'Riņķa līnijas garums: {round(2*math.pi*r, 2)} \nRiņķa līnijas laukums: {round(math.pi*r**2, 2)}')
print("Ievadiet taisnleņķa trijstūra pirmās katetes garumu: ")
k1=int(input())
print("Ievadiet taisnleņķa trijsūtra otrās katetes garumu: ")
k2=int(input())
print(f'Taisnleņķa trijstūra hipotenūzas garums: {round(math.sqrt(k1**2+k2**2), 2)}')
print(f'Gadījuma skaitlis no 0 -1:  {random.random()}')