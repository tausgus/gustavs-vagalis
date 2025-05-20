import time
while True: # Mēģina līdz iziešanai
    try:
        score = float(input("Ievadiet testa rezultātu [0-100]: "))
        if score > 100 or score < 0:
            raise ValueError # Ja skaitlis ārpus 0-100 diapzona
        if score <= 10:
            print(f'Rezultāts: {score}% - Ļoti, ļoti vāji (atzīme: 1)')
        elif score <= 20:
            print(f'Rezultāts: {score}% - Ļoti vāji (atzīme: 2)')
        elif score <= 30:
            print(f'Rezultāts: {score}% - Vāji (atzīme: 3)')
        elif  score <= 40:
            print(f'Rezultāts: {score}% - Gandrīz viduvēji (atzīme: 4)')
        elif score <= 53:
            print(f'Rezultāts: {score}% - Viduvēji (atzīme: 5)')
        elif score <= 66:
            print(f'Rezultāts: {score}% - Gandrīz labi (atzīme: 6)')
        elif score <= 76:
            print(f'Rezultāts: {score}% - Labi (atzīme: 7)')
        elif score <= 86:
            print(f'Rezultāts: {score}% - Ļoti labi (atzīme: 8)')
        elif score <= 94:
            print(f'Rezultāts: {score}% - Teicami (atzīme: 9)')
        elif score <= 100:
            print(f'Rezultāts: {score}% - Izcili (atzīme: 10)')

        while True:
            try:
                choice = input("Vai vēlaties ievadīt citu rezultātu? [j/n]: ")
                match choice:
                    case "j":
                        break
                    case "n":
                        for n in range (1,4):
                            print(f"Programma beidzas{'.'*n}")
                            time.sleep(0.4)
                        print("Programma beigusies.")
                        quit()
                    case _: # Ja izvēlēts kaut kas, kas nav j vai n
                        raise ValueError
            except ValueError:
                print("Lūdzu ievadiet vienu no piedāvātajiem variantiem.")
            
    except ValueError:
        print("Nederīga ievade. Lūdzu ievadiet skaitli no 0 līdz 100.")

