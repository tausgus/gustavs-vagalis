import datetime

def pareiza_ievade(zina: str, variants: int): # Funkcija, kas nodrošina pareizu ievadi un to atgriež
    match variants:
        case 0: # Pilnīgi jebkāda teksta ievade
            return input(f'{zina}: ')
        case 1: # Tikai pozitiīvi veseli skaitļi
            while True:
                input = (f'{zina} [>0]: ')
                try:
                    skaitlis = int(input)
                    if skaitlis > 0:
                        return skaitlis
                    else:
                        raise TypeError
                except TypeError:
                    print('! Ievade drīkst būt tikai vesels pozitīvs skaitlis. Mēginiet vēlreiz.')
        case 2: # Tikai datums formātā DD/MM/YY
            pass