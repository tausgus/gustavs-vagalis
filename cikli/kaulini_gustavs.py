print('\t- Metamā kauliņa sacensības -')
speletajs_1 = input('Ievadiet pirmā spēlētāja vārdu: ')
speletajs_2 = input('Ievadiet otrā spēlētāja vārdu: ')
punkti_1, punkti_2 = 0, 0
metieni = int(input('Ievadiet metienu skaitu [>=1]: '))

print('\t---')

for i in range(1,metieni+1):
    punkti_1 += int(input(f'Ievadiet spēlētāja {speletajs_1} {i}. metiena rezultātu [1-6]: '))
    punkti_2 += int(input(f'Ievadiet spēlētāja {speletajs_2} {i}. metiena rezultātu [1-6]: '))

print('\t---')

print(f'Spēlētāja {speletajs_1} punktu summa: {punkti_1}')
print(f'Spēlētāja {speletajs_2} punktu summa: {punkti_2}')
if punkti_1 > punkti_2:
    print(f'! Uzvar {speletajs_1}')
elif punkti_2 > punkti_1:
    print(f'! Uzvar {speletajs_2}')
else:
    print('! Neizšķirts!')