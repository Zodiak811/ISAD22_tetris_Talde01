import tkinter as tk
from view.menu import *
erabiltzailea="Gonbidatu bat"
def login():
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

    db = open("database.txt", "r")
    Username = sar1.get()
    Password = sar2.get()
    if not len(Username or Password) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("Ongi etorri, " + Username)
                        global erabiltzailea
                        erabiltzailea=Username
                        global root
                        #root.withdraw()
                        root.destroy()
                        #sortuMenu()


                    else:
                        print("Izena edo pasahitza txarto sartu dituzu")
                        error("Izena edo pasahitza txarto sartu dituzu")
                except:
                    print("Izena edo pasahitza txarto sartu dituzu")
                    error("Izena edo pasahitza txarto sartu dituzu")
            else:
                print("Erabiltzaile hori ez dago")
                error("Erabiltzaile hori ez dago")
        except:
            print("Erabiltzailea edo pasahitza ez dira existitzen")
            error("Erabiltzailea edo pasahitza ez dira existitzen")
    else:
        print("Mesedez balio bat sartu")
        error("Mesedez balio bat sartu")

def datuakKonprobatu():
    global root
    root = tk.Tk()
    root.geometry("500x500+500+100")
    root.title("Sartzea")
    global sar1,sar2

    txt1=tk.Label(root,text="Sartu erabiltzaile izena: ")
    sar1=tk.Entry(root)

    txt2=tk.Label(root,text="Sartu pasahitza: ")
    sar2=tk.Entry(root)

    igo = tk.Button(root, text="Logeatu")
    igo.configure(command=login)

    txt1.pack()
    sar1.pack()

    txt2.pack()
    sar2.pack()

    igo.pack()
    root.mainloop()
