# 1. uzdevums
class Kubs:
    def __init__(self, malas_garums: int, krasa: str): # 1.1.
        if malas_garums >= 2:
            self.malas_garums = malas_garums
        else:
            print('Malas garums neatbilst nosacījumiem!')
            self.malas_garums = 2
        self.krasa = krasa

    def aprekinat_tilpumu(self): 
        return int(self.malas_garums**3) # V = a^3

print('Dati par kubg objektu:')
# 1.2., 1.3., 1.4. uzdevumi
kubg = Kubs(10, "Zaļa") # Objektu izveido šeit, lai kļūdas ziņa izdrukātos pēc objekta nosaukuma
print(f'Kubg krāsa un tilpums: {kubg.krasa} {kubg.aprekinat_tilpumu()}\nKubg malas garums: {kubg.malas_garums}')

print('***')

print('Dati par kubr objektu:')
# 1.5., 1.6., 1.7. uzdevumi
kubr = Kubs(1, "Sarkana")
print(f'Kubr krāsa un tilpums: {kubr.krasa} {kubr.aprekinat_tilpumu()}\nKubr malas garums: {kubr.malas_garums}')

print('***')

# 2. uzdevums
class Bloks: # Nevis apakšklase, bet saņem jau eksistējošu kuba objektu
    def __init__(self, pamata_kubs: Kubs, n_kubi: int, forma: int):
        # Dotie
        self.forma = forma

        # Saņem gatavo kubu, lai izmantotu tā īpašības
        self.pamata_kubs = pamata_kubs

        # Noklusējuma vērtība
        self.derigums = 0

        # 2.1.1. uzdevums
        if n_kubi not in range(1,5):
            print('Nepareiza kubu skaita vērtība!')
            self.n_kubi = 1
        else:
            self.n_kubi = n_kubi

        # 2.1.2. uzdevums, veic derīguma pārbaudi un attiecīgi iestata vērtību
        if self.forma in [11,12,13,14,22]:
            self.derigums = 1

        # Nosaukumam apvieno vecāka klases īpašības
        self.nosaukums = pamata_kubs.krasa + str(self.n_kubi)


    def tilpums(self):
        # Tilpums būs kubu skaita reizinājums ar viena kuba tilpumu.
        return int(self.pamata_kubs.aprekinat_tilpumu() * self.n_kubi)

# 2.2. uzdevums
# Sākumā izveido kubu, kurš veidos bloku ar vajadzīgajām īpašībām
kubl = Kubs(5, "oranža")
# 2.3. uzdevums, pēc tam no šī izveido bloku un izdrukā informāciju
print('Oranžs objekts:')
blokl = Bloks(kubl, 3, 13)
print(f"{blokl.nosaukums} {blokl.tilpums()} {'derīgs' if blokl.derigums else 'nederīgs'} {blokl.derigums}")

print('***')

# 2.4. uzdevums
# Sākumā izveido kubu, kurš veidos bloku ar vajadzīgajām īpašībām
print('Zils objekts:')
kubh = Kubs(7, "zila")
# 2.3. uzdevums, pēc tam no šī izveido nederīgu bloku un izdrukā informāciju
blokh = Bloks(kubh, 5, 23)
# 2.5. uzdevums, ja ir nederīgs, izlaiž vērtības
if blokh.derigums == 1:
    print(f"{blokh.nosaukums} {blokh.tilpums()} derīgs {blokh.derigums}")
if blokh.derigums == 0: 
    print('Forma neatbilst nosacījumiem')
    print(f"{blokh.nosaukums} nederīgs {blokh.derigums}")

print('***')

# 2.6. uzdevums
# Samaina formas numuru un attiecīgi arī derīguma vērtību
blokh.forma = 12
blokh.derigums = 1
# 2.7. uzdevums
print('Mainīta forma:')
if blokh.derigums == 1:
    print(f"{blokh.nosaukums} {blokh.pamata_kubs.malas_garums} derīgs {blokh.derigums}")
if blokh.derigums == 0: 
    print('Forma neatbilst nosacījumiem')
    print(f"{blokh.nosaukums} nederīgs {blokh.derigums}")

print('***')