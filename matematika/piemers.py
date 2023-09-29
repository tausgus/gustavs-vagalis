import math 
from random import randint, random
skaitlis = 43.7

print(f'Skaitlis noapaļots uz leju: {math.floor(skaitlis)}')
print(f'Skaitlis noapaļots uz augšu: {math.ceil(skaitlis)}')

pakapinats = math.pow(skaitlis,2)
print(f'Skaitlis pakāpē 2: {pakapinats}')

izvilkta_sakne = math.sqrt(skaitlis)
print(f'No skaitļa vilkta kvadrātsakne: {izvilkta_sakne}')

x = 16/95
print(f'Neformatēts x: {x}')
print(f'Formatēts x: {"%.3f"%x}')

decimals = random() # 0.1 - 1.0 
print(decimals)

cipars = randint(1, 50)
print(cipars)