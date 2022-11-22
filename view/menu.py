import sqlite3
import tkinter as tk
import Logeatu
#from model.Tableroa import Tableroa
#from model.Tableroa import tam, setTam
from Logeatu import *

#from view.JokatuLeioa import JokatuLeioa
diff=1

def erabiltzaileGuztiakLortu():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM erabiltzaile")
    return res

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
            #db = open("database.txt", "r")
            Username = sar1.get()
            Password = sar2.get()
            if not len(Username or Password) < 1:
                """
                d = []
                f = []
                for i in db:
                    a, b = i.split(", ")
                    b = b.strip()
                    d.append(a)
                    f.append(b)
                data = dict(zip(d, f))
                """

                try:
                    if erabiltzaileaDago(Username):
                        try:
                            if logInZuzena(Username, Password):
                                print(Username + "Erabiltzailea ezabatzen")
                                """
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
                                """
                                erabiltzaileaEzabatu(Username)
                                window.destroy()

                            else:
                                print("Izena edo pasahitza txarto sartu dituzu")
                        except:
                            print("Izena edo pasahitza txarto sartu dituzu")
                    else:
                        print("Erabiltzaile hori ez dago")
                except:
                    print("Erabiltzailea edo pasahitza ez dira existitzen")
            else:
                print("Mesedez balio bat sartu")
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
        #db = open("database.txt", "r")
        #txt = db.read()

        lbl.pack()
        sar1.pack()
        sar2.pack()
        btnEzabatu.pack()
        txtLista.pack()
        erabLista = erabiltzaileGuztiakLortu()
        for row in erabLista:
            lista = tk.Label(window, text=row)
            lista.pack()
        #lista.pack()

    else:
        print("Ez da admin")
        window = tk.Tk()
        window.title("Errorea")
        window.geometry("200x100+700+400")
        lbl=tk.Label(window, text="Ezin dituzu erabiltzaileak kudeatu!")
        lbl2=tk.Label(window, text="Ez zara administratzailea")
        lbl.pack()
        lbl2.pack()
        btn=tk.Button(window, text="Bueltatu", command=bueltatu)
        btn.pack()
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


    txtErabil.pack()
    testua.pack()
    btnZ.pack()
    btnJolastu.pack()
    txtEdo.pack()
    btnKudeatu.pack()
    root.mainloop()
    return diff

#sortuMenu()