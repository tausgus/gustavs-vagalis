# 30 dienas Python programmēšanas valodā

# Mainīgo definīcijas
vards, uzvards = "Vārds ", "Uzvārds"
vards_uzvards = vards + uzvards
vecums = 16
gads = 2023
valsts = "Latvija"
pilseta = "Sigulda"

# Mainīgo izdruka ar formatētu virkni un jaunas līnijas simbolu
print(f'Vārds un uzvārds: {vards_uzvards}\nValsts: {valsts}\nPilsēta: {pilseta}\nVecums: {vecums}\nGads: {gads}')

# Priekš katra mainīgā, kas atrodas virknē pārbaudīt tā tipu
for mainigais in [vards,uzvards,vards_uzvards,vecums,gads,valsts,pilseta]:
    print(type(mainigais)) 

