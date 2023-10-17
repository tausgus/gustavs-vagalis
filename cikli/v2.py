'''atbilde = 'j'
while atbilde == 'j':
    print('Nekusties!')
    atbilde = input('Vai briesmonis ir draudzīgs? [j/n]: ')
print('Bēdz prom!')
'''

# Pārbaudīt, vai lietotājs prot reizināt ar savu ievadīto skaitli un 1-12
skaitlis = int(input('Ievadi skaitli, ar ko pārbaudīt reizināšanu: [>1]: '))
for num in range(1,13):
    atbildets = False
    while not atbildets:
        minejums = input(f'{skaitlis} x {num} = [skaitlis,stop,izlaist]: ')
        if minejums == 'stop':
            quit()
        elif minejums == 'izlaist':
            atbildets = True
        elif int(minejums) == (skaitlis*num):
            atbildets = True
        else:
            print(f'! Nav pareizi, mēģini vēlreiz. {skaitlis} x {num} = {skaitlis*num}')
print('\t- Pabeigts! -')
