class Doktorats:
    # Konstruktors, izveido sagatavi atribūtiem
    def __init__(self):
        self.nosaukums = ""
        self.pacientu_skaits = 0

    # Metode ievadei
    def ievade(self):
        self.nosaukums = input("Ievadiet doktorāta nosaukumu: ")
        while True:
            try:
                self.pacientu_skaits = int(input("Ievadiet doktorāta pacientu skaitu: "))
                break
            except ValueError: # Ja nevar pārveidot uz int, nav skaitlis
                print('! Kļūda - pacientu skaitam jābūt skaitlim. Mēģiniet vēlreiz.')
    
    # Metode izvadei
    def izvade(self):
        print(f'Doktorāts {self.nosaukums} apkalpo {self.pacientu_skaits} pacientus.')

# Tukšs objekts
testa_doktorats = Doktorats()
# Ievada datus šim objektam ar funkciju
testa_doktorats.ievade()
# Izdrukā datus
testa_doktorats.izvade()