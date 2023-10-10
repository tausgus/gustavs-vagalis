# Izdrukāt skaitļus 0,1,2,3,4,5
# print(list(range(6))) ?
for i in range(6):
    print(i)

print('\t---')

for i in range(3,8,2):
    print(i)
print('\t---')

n = int(input("Ievadīt skaitli: "))
for i in range(1,11):
    print(f'{n} + {i} = {n+i}')

print('\t---')

# Atrast skaitļu 2 un 4 dalītājus, parādīt tos, kas dalās ar 2, gan ar 4, gan 2
for num in range(1,int(input("Ievadi skaitli, līdz kuram meklēt dalāmos: "))+1):
    if (num % 2 == 0) and (num % 4 == 0):
        print(f'{num} dalās gan ar 2, gan ar 4')
    elif (num % 2 == 0):
        print(f'{num} dalās ar 2')
    else:
        print(num)