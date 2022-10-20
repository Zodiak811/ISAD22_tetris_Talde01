import random
import tkinter as tk
#from model.Tableroa import Tableroa
#from model.Tableroa import tam, setTam
from model.Piezak import *
from playsound import playsound
import winsound


# from view.JokatuLeioa import JokatuLeioa
diff=1



def setDiff(z):
    global diff
    diff = z
def jolastuBtn():
    global root
    #root.withdraw()
    root.destroy()

def zailtasuna():
    global diff
    if diff==1:
        btnZ.configure(text="Normala")
        diff=2

    elif diff==2:
        btnZ.configure(text="Zaila")
        diff = 4
    else:
        btnZ.configure(text="Erraza")
        diff = 1
def sortuMenu():
    global root
    root = tk.Tk()
    root.title("Menu")
    root.geometry("200x100+650+300")
    global btnZ
    btnZ = tk.Button(root, text="Erraza", font=12)

    testua = tk.Label(root, text="Hautatu zailtasuna: ", font=12)

    btnZ.configure(command=zailtasuna)

    btnJolastu = tk.Button(root, text="Jolastu", font=16)
    btnJolastu.configure(command=jolastuBtn)

    testua.pack()
    btnZ.pack()
    btnJolastu.pack()
    root.mainloop()

sortuMenu()