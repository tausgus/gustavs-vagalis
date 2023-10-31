user = 'gustavs'
passwd = '123456'

print('\t- Paroles programma [lai beigtu, ievadiet \'stop\'] -')

# Cikls ar 5 mēģinājumiem
for i in [5,4,3,2,1]:
    # Pārbauda stop
    entered_user = input('Ievadiet savu lietotājvārdu: ')
    if entered_user == 'stop': 
        quit()
        print('\t! Programmas beigas')
    entered_passwd = input('Ievadiet savu paroli: ')
    if entered_passwd == 'stop': 
        quit()
        print('\t! Programmas beigas')

    if entered_user == user and entered_passwd == passwd: # Ja abi sakrīt
        print('\t! Pieslēgšanās veiksmīga')
        break
    elif len(entered_passwd) < len(passwd):
        print(f'\t! Parolei ir jābūt vismaz {len(passwd)} rakstzīmes garai') # Parāda vajadzīgo paroles garumu atkarībā no ievadītās
    else:
        print('\t! Ievadītie dati nepareizi')
    
    if i == 1: # Programma beidzas, ja izmantoti visi mēģinājumi
        print(f'\t! Izmantoti visi mēģinājumi, dati ievadīti nepareizi.')
        quit()
    else:
        print(f'\t! Vēl palikuši {i-1} mēģinājumi')

# 2. daļa, turpinās, ja autentifikācija veiksmīga

# Ja stop, tad iziet, bet ja nē - mainīgos pārveido uz int vieglākām turpmākām darbībām
num_1 = input('Ievadiet veselu skaitli [>0]: ')
if num_1 == 'stop': 
    print('\t! Programmas beigas')
    quit()
else: num_1 = int(num_1)

num_2 = input('Ievadiet otru veselu skaitli [>0]: ')
if num_2 == 'stop': 
    print('\t! Programmas beigas')
    quit()
else: num_2 = int(num_2)

# Pārbauda, vai negatīvi
if num_1 < 0 or num_2 < 0:
    print('\t! Ievadītie skaitļi nevar būt negatīvi')
elif num_2 < num_1: # Ja otrs mazāks nekā pirmais, 0
    print(f'\t= 0 (otrais skaitlis ievadīts mazāks nekā pirmais)')
else: # Ja viss pareizi, tad turpina ar aprēķinu
    summa = 0
    for j in range(num_1,num_2+1): # Izveido range no ievadītajiem sākuma un beigu skaitļiem, tos pakāpeniski saskaita
        summa += j
    print(f'\t= {summa}')