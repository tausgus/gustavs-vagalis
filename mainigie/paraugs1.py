'''
1. Mainīgo tipu pārveidošana
2. Datu tipu iegūšana no literāļa
3. Konkatenācija
'''

name = 'Anna'
teksts = 'teksts'
skaitlis = 9
print(name)

kombo = name, teksts # Mainīgo apvienošana
print(kombo)

varda_garums = len(teksts)
print(f'Mainīgā garums: {varda_garums}')

a = b = c = 300 # Kaskādes veida piešķiršana
print(a, b, c)

x, y = 10, 'hello'
print(x, y)