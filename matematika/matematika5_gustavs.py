print('Programmu izstādāja: Gustavs Vagalis\nLaukuma aprēķins ģeometriskām figūrām\n\t****')

# Mainīgo vērtības piešķiršana un pārveidošana uz float tipu
a = float(input('Ievadiet malas A garumu: '))
print(f'Malas A garums: {a}\n\t****')

b = float(input('Ievadiet malas B garumu: '))
print(f'Malas B garums: {a}\n\t****')

h = float(input('Ievadiet augstumu: '))
print(f'Augstums: {h}')

# Veic aprēķinus ar formulām iekšpus fstring formatēšanas
print(f'Laukums trijstūrim: {a*h/2}\nLaukums trapecei: {(a+b)/2*h}\nLaukums paralelogramam: {a*h}') 
print('\t****\nPaldies!')