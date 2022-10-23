import random
import tkinter as tk

import Logeatu
#from model.Tableroa import Tableroa
#from model.Tableroa import tam, setTam
from model.Piezak import *
from playsound import playsound
import winsound


#from view.JokatuLeioa import JokatuLeioa
diff=1


def error(mezua):
    def bueltatu():
        window.destroy()

    window = tk.Tk()
    window.title("Errorea")
    window.geometry("300x100+600+250")
    lbl = tk.Label(window, text=mezua)
    lbl.pack()
    btn = tk.Button(window, text="Bueltatu", command=bueltatu)
    btn.pack()

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
        #diff=2
        setDiff(2)

    elif diff==2:
        btnZ.configure(text="Zaila")
        #diff = 4
        setDiff(4)
    else:
        btnZ.configure(text="Erraza")
        #diff = 1
        setDiff(1)

def kudeatuErabiltzaileak():
    def bueltatu():
        window.destroy()
    print("Kudeatzen")
    if Logeatu.erabiltzailea=="admin":
        ############################################################### EZABATU ERABILTZAILEA
        def ezabatuErabil():
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
                                print(Username + "Erabiltzailea ezabatzen")
                                file = open("database.txt", "r")
                                replacement = ""

                                for line in file:
                                    line = line.strip()
                                    changes = line.replace(Username + ", " + Password, "")
                                    replacement = replacement + changes + "\n"

                                file.close()

                                fout = open("database.txt", "w")
                                fout.write(replacement)
                                fout.close()
                                with open('database.txt') as reader, open('database.txt', 'r+') as writer:
                                    for line in reader:
                                        if line.strip():
                                            writer.write(line)
                                    writer.truncate()
                                window.destroy()

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
        ############################################################### END EZABATU ERABILTZAILEA
        print("Admin da, paso eman")
        window = tk.Tk()
        window.title("Kudeatzailea")
        window.geometry("600x300+500+300")
        lbl = tk.Label(window, text="Ezabatu nahi duzun erabiltzailearen izena eta pasahitza sartu: ")
        sar1 = tk.Entry(window)
        sar2 = tk.Entry(window)
        btnEzabatu=tk.Button(window, text="Ezabatu", command=ezabatuErabil)

        txtLista=tk.Label(window,text="Hemen duzu erabiltzaile guztien zerrenda: \n [Izena, pasahitza]")
        db = open("database.txt", "r")
        txt = db.read()
        lista = tk.Label(window, text=txt)

        lbl.pack()
        sar1.pack()
        sar2.pack()
        btnEzabatu.pack()
        txtLista.pack()
        lista.pack()

    else:
        print("Ez da admin")
        error("Ezin dituzu erabiltzaileak kudeatu \n administratzailea ez zarelako")


def pasahitzaAldatu():
    def bueltatu():
        window.destroy()
    if (Logeatu.erabiltzailea != "Gonbidatu bat"):
        def pasAldatu():
            db = open("database.txt", "r")
            Username = sar1.get()
            Password = sar2.get()
            Npassword = sar3.get()
            if not len(Username or Password or Npassword)<1:
                d = []
                f = []
                for i in db:
                    a, b = i.split(", ")
                    b = b.strip()
                    d.append(a)
                    f.append(b)
                data = dict(zip(d, f))
                if len(Npassword) > 3:
                    try:
                        if data[Username]:
                            try:
                                if Password == data[Username]:
                                    print("Pasahitza aldatzen, "+ Username)
                                    file = open("database.txt", "r")
                                    replacement = ""
                                    # using the for loop
                                    for line in file:
                                        line = line.strip()
                                        changes = line.replace(Username + ", " + Password, Username + ", " + Npassword)
                                        replacement = replacement + changes + "\n"

                                    file.close()
                                    # opening the file in write mode
                                    fout = open("database.txt", "w")
                                    fout.write(replacement)
                                    fout.close()
                                    with open('database.txt') as reader, open('database.txt', 'r+') as writer:
                                        for line in reader:
                                            if line.strip():
                                                writer.write(line)
                                        writer.truncate()
                                    window.destroy()

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
                    print("Pasahitza oso motza da")
                    error("Pasahitza oso motza da")
            else:
                print("Mesedez hutsune guztiak bete")
                error("Mesedez hutsune guztiak bete")

        window = tk.Tk()
        window.title("Kudeatzailea")
        window.geometry("600x300+500+300")
        lbl = tk.Label(window, text="Sartu zure erabiltzailea, pasahitza, eta pasahitz berria: ")
        sar1 = tk.Entry(window)
        sar2 = tk.Entry(window)
        sar3 = tk.Entry(window)
        btnAldatu = tk.Button(window, text="Aldatu", command=pasAldatu)

        lbl.pack()
        sar1.pack()
        sar2.pack()
        sar3.pack()
        btnAldatu.pack()
    else:
        print("Ez dago logeatuta")



def sortuMenu():
    global root
    root = tk.Tk()
    root.title("Menu")
    root.geometry("300x200+650+300")
    global btnZ
    btnZ = tk.Button(root, text="Erraza", font=12)
    txtErabil=tk.Label(root,text=Logeatu.erabiltzailea + " bezala jolasten ari zara, ongi etorri")
    txtEdo=tk.Label(root,text="edo:")
    testua = tk.Label(root, text="Hautatu zailtasuna: ", font=12)

    btnZ.configure(command=zailtasuna)

    btnJolastu = tk.Button(root, text="Jolastu", font=16)
    btnJolastu.configure(command=jolastuBtn)

    btnKudeatu = tk.Button(root, text="Erabiltzaileak kudeatu")
    btnKudeatu.configure(command=kudeatuErabiltzaileak)

    btnPasAldatu = tk.Button(root, text="Pasahitza aldatu")
    btnPasAldatu.configure(command=pasahitzaAldatu)


    txtErabil.pack()
    testua.pack()
    btnZ.pack()
    btnJolastu.pack()
    txtEdo.pack()
    btnKudeatu.pack()
    btnPasAldatu.pack()
    root.mainloop()
    return diff

#sortuMenu()