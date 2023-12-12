import datetime
# Input sintakse varētu būt [id] [darbība], piemēram "03 pabeigts".
darbi = []
pabeigti = []

# Pietrūkst kārtošana

print('\t- To-Do Saraksts -')
print(f'| {datetime.datetime.now().strftime("%A, %d %B")}')
print('| Lai aplūkotu iespējamās komandas, raksti \'h\'.')

while True:
    komanda = input("#> ")
    match komanda[0]:
        case "h":
            print("| Lietošanas pamācība")
            print("s - apskata aktuālo un pabeigto darbu sarakstu")
            print("p - pievieno darbu")
            print("d [id] - dzēš darbu")
            print("a [id] - atzīmē kā pabeigtu")
            print("k - sakārtot pēc prioritātes")
            print("e - eksportē kā teksta failu")
        case "s":
            print("| Darbu saraksts")
            for darbs in darbi:
                print(f'[{darbi.index(darbs)}] ~ {darbs[0]}, jāizdara līdz {darbs[1]}')
            print("| Pabeigto darbu saraksts")
            for darbs in pabeigti:
                print(f'[X] ~ {darbs[0]}, pabeigts pulkst. {darbs[1]}')
        case "p":
            print("| Darba pievienošana")
            darbi.append([input("# Nosaukums > "), input("# Termiņš [dd.mm] > "), int(input("# Prioritāte [1-10] > "))])
        case "d":
            print(f'| Darbs nr. {komanda[2:]} izdzēsts.')
            darbi.pop(int(komanda[2:]))
        case "a":
            print(f'| Darbs nr. {komanda[2:]} pabeigts.')
            darbi[int(komanda[2:])][1] = datetime.datetime.now().strftime("%d.%m %H:%M")
            pabeigti.append(darbi[int(komanda[2:])])
            darbi.pop(int(komanda[2:]))
        case "e":
            print("| Saraksta eksportēšana")
            print("Atver failu ...")
            fails = open(f'todo_{datetime.datetime.now().strftime("%d_%m_%y")}.txt', "a")
            print("Pievieno darāmos darbus ...")
            fails.write("| Darbu saraksts\n")
            for darbs in darbi:
                fails.write(f'[{darbi.index(darbs)}] ~ {darbs[0]}, jāizdara līdz {darbs[1]}\n')
            print("Pievieno pabeigtos darbus ...")
            fails.write("| Pabeigto darbu saraksts\n")
            for darbs in pabeigti:
                fails.write(f'[X] ~ {darbs[0]}, pabeigts pulkst. {darbs[1]}\n')
            print("Aizver failu ...")
            fails.close()
            print("Pabeigts.")