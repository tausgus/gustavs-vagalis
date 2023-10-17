# for cikls
#for num in range(1,10):
#    print(str(num)*num
vecums = int(input("Ievadiet suņa vecumu pilnos gados [>=0]: "))
if vecums < 0:
    print('Vecums nedrīkst būt mazāks kā 0.')
elif vecums <= 2:
    print(f'Suņa vecums cilvēka gados ir {vecums*10.5}')
else:
    print(f'Suņa vecums cilvēka gados ir {21 + vecums*4}')