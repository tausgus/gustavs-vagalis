gads = int(input("Ievadi gadu: "))

# Sākumā pārveido gadu uz str, lai piekļūtu pēdējiem diviem cipariem.
if int(str(gads)[-2:]) % 4 == 0: # Ja pēdējie divi cipari dalās ar 4 bez atlikuma, tad garais gads
    print(f'{gads} ir garais gads.')
elif int(str(gads)[-2:]) % 4 != 0: # Ja ir atlikums, tad īsais gads
    print(f'{gads} ir īsais gads.')