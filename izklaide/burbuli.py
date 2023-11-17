import tkinter 
import random
import math

# Zemūdene spridzina burbuļus, tiek skaitīti punkti

logs = tkinter.Tk()
logs.title("Burbuļu spridzinātājs")
izmers = 700
audekls = tkinter.Canvas(logs, width=izmers, height=izmers, background='lightblue')
audekls.pack()

kuga_id = audekls.create_oval(10, 10, 160, 60, width=10)

audekls.update()

tkinter.mainloop()