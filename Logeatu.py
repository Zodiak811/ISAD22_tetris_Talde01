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
    ###############################################PASAHITZA BERRESKURATU
    def pasLortu():
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
        def berreskPasahitza():
            db = open("database.txt", "r")
            Username = sarIzen.get()
            if not len(Username) < 1:
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
                            print("Zure pasahitza " + data[Username] + " da")
                            psh.configure(text="Zure pasahitza " + data[Username] + " da")
                        except:
                            print("Izena txarto sartu dituzu")
                            error("Izena txarto sartu dituzu")
                    else:
                        print("Erabiltzaile hori ez dago")
                        error("Erabiltzaile hori ez dago")
                except:
                    print("Erabiltzailea ez da existitzen")
                    error("Erabiltzailea ez da existitzen")
            else:
                print("Mesedez balio bat sartu")
                error("Mesedez balio bat sartu")

        window = tk.Tk()
        window.title("Berreskuratzea")
        window.geometry("300x150+600+250")
        lbl = tk.Label(window, text="Sartu erabiltzaile izena: ")
        lbl.pack()
        sarIzen = tk.Entry(window)
        sarIzen.pack()
        btn = tk.Button(window, text="Berreskuratu", command=berreskPasahitza)
        psh = tk.Label(window)
        btn.pack()
        buelt=tk.Button(window,text="Bueltatu", command=window.destroy)
        psh.pack()
        buelt.pack()


    ############################################### END PASAHITZA BERRESKURATU
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

    berreskuratu = tk.Button(root, text="Pasahitza ahaztu zait")
    berreskuratu.configure(command=pasLortu)

    txt1.pack()
    sar1.pack()

    txt2.pack()
    sar2.pack()

    igo.pack()

    berreskuratu.pack()
    root.mainloop()
