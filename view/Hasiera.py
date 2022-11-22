import tkinter as tk
from Erregistratu import *
from Logeatu import *

def erregist():
    pant.destroy()
    datuakSartu()

def loge():
    pant.destroy()
    datuakKonprobatu()

def hasi():
    global pant
    pant = tk.Tk()
    pant.geometry("500x500+500+100")
    pant.title("HASIERA")

    txt = tk.Label(pant,text="Hautatu egin nahi duzuna: ", font=12)

    erreg = tk.Button(pant,text="Izena Eman", font=16)
    erreg.configure(command=erregist)

    log = tk.Button(pant,text="Sartu", font=16)
    log.configure(command=loge)


    txt.pack()
    log.pack()
    erreg.pack()
    pant.mainloop()
#hasi()