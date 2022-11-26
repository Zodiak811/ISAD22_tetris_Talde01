import tkinter as tk
from Logeatu import *

def izenaEman():
    def error(mezua):
        def bueltatu():
            window.destroy()

        window = tk.Tk()
        window.title("Errorea")
        window.geometry("300x150+600+250")
        lbl = tk.Label(window, text=mezua)
        lbl.pack()
        btn = tk.Button(window, text="Bueltatu", command=bueltatu)
        btn.pack()
    Username = sar1.get()
    Password = sar2.get()
    Password1 = sar3.get()

    if Password != Password1:
        print("Pasahitzak ezberdinak dira")
        error("Pasahitzak ezberdinak dira")
    else:
        if len(Password) <= 3:
            print("Pasahitza oso motza da")
            error("Pasahitza oso motza da")
        elif erabiltzaileaDago(Username):
            print("Erabiltzaile izen hori jada existitzen da")
            error("Erabiltzaile izen hori jada existitzen da")
        else:
            erabiltzaileaSortu(Username, Password)
            print("Erabiltzaile berria erregistratuta")
            Logeatu.erabiltzailea=Username
            root.destroy()

def datuakSartu():
    global root
    root = tk.Tk()
    root.geometry("500x500+500+100")
    root.title("Erregistroa")
    global sar1,sar2,sar3

    txt1=tk.Label(root,text="Sartu erabiltzaile izena: ")
    sar1=tk.Entry(root)

    txt2=tk.Label(root,text="Sartu pasahitza: ")
    sar2=tk.Entry(root)

    txt3=tk.Label(root,text="Errepikatu pasahitza: ")
    sar3=tk.Entry(root)

    igo = tk.Button(root, text="Erregistratu")
    igo.configure(command=izenaEman)

    txt1.pack()
    sar1.pack()

    txt2.pack()
    sar2.pack()

    txt3.pack()
    sar3.pack()

    igo.pack()
#    root.mainloop()

