# Inicializē tukšus mainīgos, ko izmantos tālāk
posmi = [] # Struktūra [pietura, [posms], pietura, [posms], pietura, ...]
n_skoleni = 0

# Pārbauda, vai ievade ir pieļaujamo atbilžu sarakstā, ja nē, mēģina bezgalīgi vēlreiz
def pareiza_ievade(derigas_atbildes: list, teksts):
    atbilde = input(teksts)
    while True:
        if atbilde in derigas_atbildes:
            return atbilde
        else:
            print("! Lūdzu, ievadiet pareizu atbildi.")
            atbilde = input(teksts)

def posms(sakums: str, beigas: str): # Posma izveidošanas funkcija
    print(f"( Posms {sakums.title()}-{beigas.title()} )")

    while True:
        try:
            attalums = float(input("Ievadiet attālumu [km]: ")) # Attāluma ievade
            if attalums > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("! Lūdzu, ievadiet pareizu atbildi.")

    # Pārveido uz pilno nosaukumu
    transports = pareiza_ievade(["v", "a", "k"], "Ievadiet transporta veidu [v - vilciens, a - autobuss, k - kājām]: ")
    if transports == "v":
        transports = "vilciens"
    elif transports == "a":
        transports = "autobuss"
    elif transports == "k":
        transports = "ar kājām"


    while True:
        try:
            laiks = float(input("Ievadiet laiku [h]: ")) # Laika ievade
            if laiks > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("! Lūdzu, ievadiet pareizu atbildi.")

    # Ja iet ar kājām - nav biļetes cena, ja cits transports - tad to paprasa
    if transports != "ar kājām":
        while True:
            try:
                cena = float(input("Ievadiet biļetes cenu [eiro]: ")) # Laika ievade
                if cena > 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("! Lūdzu, ievadiet pareizu atbildi.") 
    else:
        cena = 0
    
    return [ # Atgriež sarakstu pareizā secībā
        attalums,
        transports,
        laiks,
        cena
    ]


def rediget(): # Posma rediģēšanas funkcija - atļauj arī tukšas atbildes, pieņemot, ka dati jau pastāv

    pieturas = [] # Ātri izveido sarakstu ar tikai pieturām
    print("Pieejamās pieturas: ", end='')
    for viens_posms in posmi:
        if type(viens_posms) == str:
            pieturas.append(viens_posms)
            print(f"{viens_posms}, ", end='') # Parāda tās lietotājam
    print('\n')

    izvele = pareiza_ievade(['p', 't'], "Vai jūs vēlaties rediģēt pieturu vai transportu starp tām? [p - pieturu, t - transportu]: ")
    if izvele == "p":
        velama_pietura = pareiza_ievade(pieturas, "\nIevadiet rediģējamās pieturas nosaukumu [mazie burti]: ") # Pārbauda, vai izvēlētā pietura pastāv
        posmi[posmi.index(velama_pietura)] = input("Ievadi jauno pieturas nosakumu: ").lower().strip() # Samaina nosaukumu
    elif izvele == "t":
        pec_pietura = pareiza_ievade(pieturas[1], "Ievadiet pieturu, *pirms* kuras transportu vēlaties rediģēt: ")
        #posmi[posmi.index(pec_pietura)-1] = posms(posmi[posmi.index(pec_pietura)-2], posmi[posmi.index(pec_pietura)]) 
        # Prasa katru info, un ja tukša atbilde = to nemaina
        while True:
            attalums = input("Ievadiet attālumu [km] vai spiediet enter, ja nevēlaties mainīt: ") # Attāluma ievade
            if attalums == "":
                break
            else:
                try:
                    if float(attalums) > 0:
                        posmi[posmi.index(pec_pietura)-1][0] = float(attalums)
                    else:
                        raise ValueError
                except ValueError:
                    print("! Lūdzu, ievadiet pareizu atbildi.")

            # Pārveido uz pilno nosaukumu
        transports = pareiza_ievade(["v", "a", "k", ""], "Ievadiet transporta veidu [v - vilciens, a - autobuss, k - kājām] vai spiediet enter, ja nevēlaties mainīt: ")
        if transports == "":
            pass # Izlaist ciklu, ja nevēlas mainīt
        elif transports == "v":
            posmi[posmi.index(pec_pietura)-1][1] = "vilciens"
        elif transports == "a":
            posmi[posmi.index(pec_pietura)-1][1] = "autobuss"
        elif transports == "k":
            posmi[posmi.index(pec_pietura)-1][1] = "ar kājām"


        while True:
            laiks = input("Ievadiet laiku [h] vai spiediet enter, ja nevēlaties mainīt: ") # Laika ievade
            if laiks == "":
                break
            else:
                try:
                    if float(laiks) > 0:
                        posmi[posmi.index(pec_pietura)-1][2] = float(laiks)
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("! Lūdzu, ievadiet pareizu atbildi.")

        # Ja iet ar kājām - nav biļetes cena, ja cits transports - tad to paprasa
        if posmi[posmi.index(pec_pietura)-1][1] != "ar kājām":
            while True:
                cena = input("Ievadiet cenu [eiro] vai spiediet enter, ja nevēlaties mainīt: ") # Cenas ievade
                if cena == "":
                    break
                else:
                    try:
                        if float(cena) > 0:
                            posmi[posmi.index(pec_pietura)-1][3] = float(cena)
                        else:
                            raise ValueError
                    except ValueError:
                        print("! Lūdzu, ievadiet pareizu atbildi.")
        else:
            posmi[posmi.index(pec_pietura)-1][3] = 0
        

print('[ Klases eksursiju transporta plānošanas programma ]\n')

# Izveido sarakstu ar pieturām, jābūt vismaz divām
neapstradatie_posmi = input("Ievadiet ar komatiem atdalītu pieturu sarakstu [piem. Rīga,Liepāja]: ").split(',')
while True:
    if len(neapstradatie_posmi) > 1:
        break
    else:
        print("! Jābūt vismaz divu pieturu nosaukumiem. Mēģiniet vēlreiz.")
        neapstradatie_posmi = input("Ievadiet ar komatiem atdalītu pieturu sarakstu [piem. Rīga,Liepāja]: ").split(',')
# Pārveido uz mazajiem burtiem un noņem atstarpes
for viens_posms in neapstradatie_posmi:
    posmi.append(viens_posms.lower().strip())

while True:
    try:
        n_skoleni = int(input("Ievadiet skolēnu skaitu [>0]: ")) # Pārbauda, vai skolēnu skaits nav mazāks par 0
        if n_skoleni > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print("! Lūdzu, ievadiet pareizu atbildi.")

print('\n[ Posmi ]\n')
# Starp 2 posmiem ievada transportu
for i in range(len(posmi)):
    if type(posmi[i]) != list:
        posmi.insert(i+1, posms(posmi[i], posmi[i+1]))

print('\n( Visi posmi ievadīti )')

if pareiza_ievade(["j", "n"], "Vai vēlaties veikt izmaiņas pirms aprēķiniem? [j - jā, n - nē]: ") == "j":
    print('\n[ Rediģēšana ]')
    rediget()
    while True:
        if pareiza_ievade(["j", "n"], "Vai vēlaties veikt vēl izmaiņas? [j - jā, n - nē]: ") == "j": # Pēc vienu izmaiņu veikšanas, pārvaicā
            rediget()
        else:
            break
    

# Aprēķina cenu vienam skolēnam ejot cauri posmiem un iegūstot cenu
cena_skolenam = 0
for transports in posmi:
    if type(transports) == list:
        cena_skolenam += transports[-1]
# Aprēķina kopējo laiku ejot cauri posmiem un iegūstot laiku
kopejais_laiks = 0
for transports in posmi:
    if type(transports) == list:
        kopejais_laiks += transports[-2]

# Izdruka
print('\n[ Ekskursija ]')
print(f'Sākums: {posmi[0].title()} | Beigas: {posmi[-1].title()} | Kopējais laiks: {kopejais_laiks} h')
print(f'Cena vienam skolēnam: {round(cena_skolenam, 2)} eiro | Cena {n_skoleni} skolēniem: {round(cena_skolenam*n_skoleni, 2)} eiro')
for viens_posms in posmi:
    # Ja posms ir pietura, izdrukāt tās nosaukumu
    if type(viens_posms) == str:
        print(f'@ {viens_posms.title()}')
    # Ja posms ir transports, izdrukāt informāciju par to
    elif type(viens_posms) == list:
        print(f'|\n[ {viens_posms[0]} km, {viens_posms[1]}, {viens_posms[2]} h, {round(viens_posms[3], 2)} eiro\n|')

print('\n[ Paldies! Programma beidzas. ]')