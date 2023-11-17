# Piemērs sarakstam ar dažādiem datu tipiem
mixed_list = [1, 1.3, 'a', False]
print(mixed_list[2])
print(mixed_list[-1])

# Apgriezt skaitļu sarakstu
skaitli = [1,2,3,4,5,6,7,3,4,8,9,7]
skaitli.reverse()
print(skaitli)

# Filtrēt tikai pāra skaitļus
para_skaitli = [num for num in skaitli if num%2 == 0]
print(para_skaitli)

# Iegūst saraksta garumu
#garums = len(skaitli)

videjais = sum(skaitli) / len(skaitli)
print(f'Vidējas skaitlis: {videjais}')

# Atrast lielāko un mazāko
print(f'Mazākais: {min(skaitli)} Lielākais: {max(skaitli)}')

augli = ['ābols', 'banāns', 'apelsīns', 'bumbieris', 'citrons']
# Visi, kas sākas ar burtu B
varda_sakums = [name for name in augli if name[0] == 'b']
print(f'Vārdi, kas sākas ar B: {varda_sakums}')