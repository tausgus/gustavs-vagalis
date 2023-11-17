import tkinter 
import random

logs = tkinter.Tk()
izmers = 900
audekls = tkinter.Canvas(logs, width=izmers)
audekls.pack()

while True:
    krasa = random.choice(['yellow', 'black', 'blue'])
    koordinatas = [random.randint(0,izmers), random.randint(0, izmers)]
    diametrs = random.randint(1,izmers / 10)
    audekls.create_oval(koordinatas[0], koordinatas[1], koordinatas[0]+diametrs, koordinatas[1]+diametrs, fill=krasa, )
    logs.update()

tkinter.mainloop()