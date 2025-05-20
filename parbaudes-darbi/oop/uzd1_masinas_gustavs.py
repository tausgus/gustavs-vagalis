import datetime
class Transportlidzeklis:
    
    # Konstruktors, ar definētajiem mainīgo tipiem vajadzīgajās vietās
    def __init__(self, zimols: str, modelis: str, reg_datums: datetime.date, pilna_masa: int, degvielas_veids: str):
        self.zimols = zimols
        self.modelis = modelis
        self.reg_datums = reg_datums
        self.pilna_masa = pilna_masa
        self.degvielas_veids = degvielas_veids

    # Formatēta atgriežšana
    def izdruka(self):
        # Izdrukā katru īpašību ar formatētu virkni
        # Pārveido datumu no objekta uz izdruku
        print(f'zīmols: {self.zimols}\nmodelis: {self.modelis}\nreģistrācijas datums: {datetime.date.strftime(self.reg_datums, "%d.%m.%Y")}.\npilna masa: {self.pilna_masa}\ndegvielas veids: {self.degvielas_veids}')

# Izveido testa objektu
testa_masina = Transportlidzeklis("Audi", "A4", datetime.date(2019, 10, 22), 1800, "BG")
# Izdrukā testa objektu
testa_masina.izdruka()