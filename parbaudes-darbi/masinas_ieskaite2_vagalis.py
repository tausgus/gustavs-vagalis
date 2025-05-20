class Masina:

    def __init__(self, marka: str, modelis: str, gads: int):
        # Inicializē atribūtus
        self.marka = marka
        self.modelis = modelis
        self.gads = gads
    
    def uzsakt(self):
        # Izdruka ar konkrētiem atribūtiem
        print(f'Mašīna {self.marka} {self.modelis} sāk darboties.')

    def apstaties(self):
        # Izdruka ar konkrētiem atribūtiem
        print(f'Mašīna {self.marka} {self.modelis} ir apstādināta.')

    def info_par_auto(self):
        # Izdrukā visus atribūtus
        print(f'Marka: {self.marka}, Modelis: {self.modelis}, Gads: {self.gads}')

# Manto no Masina
class Elektro_Auto(Masina):
    # Papildus konstruktors, kurš izveido akumulatora kapacitāti, un ietilpības līmeni, kurš noklusējumā ir 100.
    def __init__(self, marka: str, modelis: str, gads: int, akumulatora_ietilp: int, akumulatora_limenis = 100):
        super().__init__(marka, modelis, gads)
        self.akumulatora_ietilp = akumulatora_ietilp
        self.akumulatora_limenis = akumulatora_limenis

    # Pārrakstīta uzsākšanas funkcija, kas pārbauda, vai uzlādes līmenis ir pietiekams
    def uzsakt(self):
        if self.akumulatora_limenis >= 20:
            print(f'{self.marka} {self.modelis} sāk darboties. Akumulators: {self.akumulatora_limenis}%')
        else:
            print(f'{self.marka} {self.modelis} nevar sākt darboties, jo akumulators ir pārāk zems: {self.akumulatora_limenis}%')
    
    # Papildināta izdrukas funkcija, lai tiek drukāta arī baterijas kapacitāte.
    def info_par_auto(self):
        super().info_par_auto() # Pamata info ņem no vecāka klases
        print(f'Akumulators: {self.akumulatora_ietilp} kWh')

# Manto no Masina
class Degvielas_Auto(Masina):
    # Papildus konstruktors, kurš izveido bākas tilpumu, un līmeni, kurš noklusējumā ir 100.
    def __init__(self, marka: str, modelis: str, gads: int, bakas_tilpums: int, degvielas_limenis = 100):
        super().__init__(marka, modelis, gads)
        self.bakas_tilpums = bakas_tilpums
        self.degvielas_limenis = degvielas_limenis

    # Pārrakstīta uzsākšanas funkcija, kas pārbauda, vai bākas līmenis ir pietiekams
    def uzsakt(self):
        if self.degvielas_limenis >= 10:
            print(f'{self.marka} {self.modelis} sāk darboties. Degvielas līmenis: {self.degvielas_limenis}%')
        else:
            print(f'{self.marka} {self.modelis} nevar sākt darboties, jo degvielas līmenis ir pārāk zems: {self.degvielas_limenis}%')

    # Papildināta izdrukas funkcija, lai tiek drukāta arī baterijas kapacitāte.
    def info_par_auto(self):
        super().info_par_auto() # Pamata info ņem no vecāka klases
        print(f'Bākas tilpums: {self.bakas_tilpums} litri')


# Punkts C. - viens objekts
auto_1 = Masina("Volvo", "V70", "2007") 
# Kā paraugā - izdruka
auto_1.info_par_auto()
auto_1.uzsakt()
auto_1.apstaties()

print('\n')

# Punkts H. - elektroauto, ar pietiekamu akumulatora uzlādes līmeni
auto_2 = Elektro_Auto("Volvo", "EX30", "2024", 75, 100)
# Kā paraugā - izdruka
auto_2.info_par_auto()
auto_2.uzsakt()
# Punkts I. - samazina līmeni, mēģina braukt
auto_2.akumulatora_limenis = 15
auto_2.uzsakt()

print('\n')

# Punkts H. - degvielas auto, ar pietiekamu akumulatora uzlādes līmeni
auto_3 = Degvielas_Auto("Volvo", "XC90", "2009", 85, 100)
# Kā paraugā - izdruka
auto_3.info_par_auto()
auto_3.uzsakt()
# Punkts I. - samazina līmeni, mēģina braukt
auto_3.degvielas_limenis = 5
auto_3.uzsakt()