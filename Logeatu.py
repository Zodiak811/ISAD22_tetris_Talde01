import tkinter as tk
import sqlite3
from view.menu import *
erabiltzailea="Gonbidatua"

def erabiltzaileaDago(izena):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM erabiltzaile WHERE izena=?", (izena,))
    if (res.fetchone() == None):
        return False
    else:
        print(res)
        return True

def logInZuzena(izena, pasahitza):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    res = cur.execute("SELECT izena, pasahitza FROM erabiltzaile WHERE izena = ? AND pasahitza = ?", (izena, pasahitza))
    if(res.fetchone() is None):
        return False
    else:
        return True

def erabiltzaileaSortu(izena, pasahitza):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("INSERT INTO erabiltzaile VALUES (?, ?, 0, 0, 0, 0, 0, 0)", (izena, pasahitza))
    con.commit()

def erabiltzaileaEzabatu(izena):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("DELETE FROM erabiltzaile WHERE izena=?", (izena,))
    con.commit()

def pasahitzaLortu(izena):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    res = cur.execute("SELECT pasahitza FROM erabiltzaile WHERE izena=?", (izena,))
    pas = res.fetchone()
    pasStr = ' '.join(pas)
    return pasStr

def sariakLortu():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    res = cur.execute("SELECT sariIzena FROM lortu WHERE erabIzena=?", (erabiltzailea,))
    return res

def sariaDu(puntuak, zail):
    sariIzena = zail + ": " + puntuak + " puntu lortu" ####### Adibidez:    Erraza: 1000 puntu lortu
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    res = cur.execute("SELECT sariIzena FROM lortu WHERE erabIzena=? AND sariIzena=?", (erabiltzailea, sariIzena))
    if (res.fetchone() is None):
        return False
    else:
        return True

def sariaDesblokeatu(puntuak, zail):
    sariIzena = zail + ": " + puntuak + " puntu lortu" ####### Adibidez:    Erraza: 1000 puntu lortu
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("INSERT INTO lortu VALUES (?,?)", (erabiltzailea, sariIzena))
    con.commit()

def puntuazioaEguneratu(punt, zail):
    if(zail == 1):
        zail = "Erraza"
    elif(zail == 2):
        zail = "Normala"
    elif(zail == 4):
        zail = "Zaila"
    unekoMax = getPuntuazioMax(zail, erabiltzailea)
    print(unekoMax)
    if(punt > unekoMax):
        print("entré")
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        if(zail == "Erraza"):
            cur.execute("UPDATE erabiltzaile SET puntuazioMaxErraza=? WHERE izena=?", (punt,erabiltzailea))
        elif(zail == "Normala"):
            cur.execute("UPDATE erabiltzaile SET puntuazioMaxNormala=? WHERE izena=?", (punt,erabiltzailea))
        elif(zail == "Zaila"):
            cur.execute("UPDATE erabiltzaile SET puntuazioMaxZaila=? WHERE izena=?", (punt,erabiltzailea))
        con.commit()

def sariakKonprobatu(punt, zail):
    if (zail == 1):
        zail = "Erraza"
    elif (zail == 2):
        zail = "Normala"
    elif (zail == 4):
        zail = "Zaila"
    #############   Sariak:
    #############   Zailtasun bakoitzeko: 1000, 3000, 5000 puntu lortu
    if(punt >= 5000):
        if(sariaDu("1000", zail) == False):
            sariaDesblokeatu("1000", zail)
        if (sariaDu("3000", zail) == False):
            sariaDesblokeatu("3000", zail)
        if (sariaDu("5000", zail) == False):
            sariaDesblokeatu("5000", zail)
    elif(punt >= 3000):
        if (sariaDu("1000", zail) == False):
            sariaDesblokeatu("1000", zail)
        if (sariaDu("3000", zail) == False):
            sariaDesblokeatu("3000", zail)
    elif(punt >= 1000):
        if (sariaDu("1000", zail) == False):
            sariaDesblokeatu("1000", zail)


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

    Username = sar1.get()
    Password = sar2.get()
    if not len(Username and Password) < 1:
        try:
            if (erabiltzaileaDago(Username) == True):
                try:
                    if logInZuzena(Username, Password) == True:
                        print("Ongi etorri, " + Username)
                        global erabiltzailea
                        erabiltzailea=Username
                        global root
                        root.destroy()

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
    ################################## PASAHITZA BERRESKURATU ##################
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
                try:
                    if erabiltzaileaDago(Username):
                        try:
                            print("Zure pasahitza " + pasahitzaLortu(Username) + " da")
                            psh.configure(text="Zure pasahitza " + pasahitzaLortu(Username) + " da")
                        except:
                            print("Izena txarto sartu dituzu")
                            error("Izena txarto sartu duzu")
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
        buelt = tk.Button(window, text="Bueltatu", command=window.destroy)
        psh.pack()
        buelt.pack()
#############################################END PASAHITZA BERRESKURATU##################
    global root
    root = tk.Tk()
    root.geometry("500x500+500+100")
    root.title("Sartzea")
    global sar1,sar2

    txt1=tk.Label(root,text="Sartu erabiltzaile izena: ")
    sar1=tk.Entry(root)

    txt2=tk.Label(root,text="Sartu pasahitza: ")
    sar2=tk.Entry(root)

    berreskuratu = tk.Button(root, text="Pasahitza ahaztu zait")
    berreskuratu.configure(command=pasLortu)

    igo = tk.Button(root, text="Logeatu")
    igo.configure(command=login)

    txt1.pack()
    sar1.pack()

    txt2.pack()
    sar2.pack()

    igo.pack()
    berreskuratu.pack()
    root.mainloop()
