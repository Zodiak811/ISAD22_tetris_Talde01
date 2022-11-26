import sqlite3
import tkinter as tk
import Logeatu
from tkinter import ttk
import model.Piezak
import view.JokatuLeioa
#from model.Tableroa import Tableroa
#from model.Tableroa import tam, setTam
from Logeatu import *

#from view.JokatuLeioa import JokatuLeioa
diff=1
"""
laukiKol='yellow'
ZutabeKol='cyan'
LformaKol='blue'
LformaAldKol='orange'
ZformaKol='green'
ZformaAldKol='red'
TformaKol='purple'
"""

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

def pertsonalizatu():
    def KolAldatu():
        if(laukiSel.get()=="Horia"):
            model.Piezak.laukiKol = 'yellow'
        elif(laukiSel.get()=="Cian"):
            model.Piezak.laukiKol = 'cyan'
        elif(laukiSel.get() == "Urdina"):
            model.Piezak.laukiKol = 'blue'
        elif (laukiSel.get() == "Laranja"):
            model.Piezak.laukiKol = 'orange'
        elif (laukiSel.get() == "Berdea"):
            model.Piezak.laukiKol = 'green'
        elif (laukiSel.get() == "Gorria"):
            model.Piezak.laukiKol = 'red'
        elif (laukiSel.get() == "Morea"):
            model.Piezak.laukiKol = 'purple'
        elif (laukiSel.get() == "Marroia"):
            model.Piezak.laukiKol = 'brown'
        elif (laukiSel.get() == "Larrosa"):
            model.Piezak.laukiKol = 'pink'
        elif (laukiSel.get() == "Grisa"):
            model.Piezak.laukiKol = 'gray'

        if (zutabeSel.get() == "Horia"):
            model.Piezak.zutabeKol = 'yellow'
        elif (zutabeSel.get() == "Cian"):
            model.Piezak.zutabeKol = 'cyan'
        elif (zutabeSel.get() == "Urdina"):
            model.Piezak.zutabeKol = 'blue'
        elif (zutabeSel.get() == "Laranja"):
            model.Piezak.zutabeKol = 'orange'
        elif (zutabeSel.get() == "Berdea"):
            model.Piezak.zutabeKol = 'green'
        elif (zutabeSel.get() == "Gorria"):
            model.Piezak.zutabeKol = 'red'
        elif (zutabeSel.get() == "Morea"):
            model.Piezak.zutabeKol = 'purple'
        elif (zutabeSel.get() == "Marroia"):
            model.Piezak.zutabeKol = 'brown'
        elif (zutabeSel.get() == "Larrosa"):
            model.Piezak.zutabeKol = 'pink'
        elif (zutabeSel.get() == "Grisa"):
            model.Piezak.zutabeKol = 'gray'

        if (LformaSel.get() == "Horia"):
            model.Piezak.LformaKol = 'yellow'
        elif (LformaSel.get() == "Cian"):
            model.Piezak.LformaKol = 'cyan'
        elif (LformaSel.get() == "Urdina"):
            model.Piezak.LformaKol = 'blue'
        elif (LformaSel.get() == "Laranja"):
            model.Piezak.LformaKol = 'orange'
        elif (LformaSel.get() == "Berdea"):
            model.Piezak.LformaKol = 'green'
        elif (LformaSel.get() == "Gorria"):
            model.Piezak.LformaKol = 'red'
        elif (LformaSel.get() == "Morea"):
            model.Piezak.LformaKol = 'purple'
        elif (LformaSel.get() == "Marroia"):
            model.Piezak.LformaKol = 'brown'
        elif (LformaSel.get() == "Larrosa"):
            model.Piezak.LformaKol = 'pink'
        elif (LformaSel.get() == "Grisa"):
            model.Piezak.LformaKol = 'gray'

        if (LformaAldSel.get() == "Horia"):
            model.Piezak.LformaAldKol = 'yellow'
        elif (LformaAldSel.get() == "Cian"):
            model.Piezak.LformaAldKol = 'cyan'
        elif (LformaAldSel.get() == "Urdina"):
            model.Piezak.LformaAldKol = 'blue'
        elif (LformaAldSel.get() == "Laranja"):
            model.Piezak.LformaAldKol = 'orange'
        elif (LformaAldSel.get() == "Berdea"):
            model.Piezak.LformaAldKol = 'green'
        elif (LformaAldSel.get() == "Gorria"):
            model.Piezak.LformaAldKol = 'red'
        elif (LformaAldSel.get() == "Morea"):
            model.Piezak.LformaAldKol = 'purple'
        elif (LformaAldSel.get() == "Marroia"):
            model.Piezak.LformaAldKol = 'brown'
        elif (LformaAldSel.get() == "Larrosa"):
            model.Piezak.LformaAldKol = 'pink'
        elif (LformaAldSel.get() == "Grisa"):
            model.Piezak.LformaAldKol = 'gray'

        if (ZformaSel.get() == "Horia"):
            model.Piezak.ZformaKol = 'yellow'
        elif (ZformaSel.get() == "Cian"):
            model.Piezak.ZformaKol = 'cyan'
        elif (ZformaSel.get() == "Urdina"):
            model.Piezak.ZformaKol = 'blue'
        elif (ZformaSel.get() == "Laranja"):
            model.Piezak.ZformaKol = 'orange'
        elif (ZformaSel.get() == "Berdea"):
            model.Piezak.ZformaKol = 'green'
        elif (ZformaSel.get() == "Gorria"):
            model.Piezak.ZformaKol = 'red'
        elif (ZformaSel.get() == "Morea"):
            model.Piezak.ZformaKol = 'purple'
        elif (ZformaSel.get() == "Marroia"):
            model.Piezak.ZformaKol = 'brown'
        elif (ZformaSel.get() == "Larrosa"):
            model.Piezak.ZformaKol = 'pink'
        elif (ZformaSel.get() == "Grisa"):
            model.Piezak.ZformaKol = 'gray'

        if (ZformaAldSel.get() == "Horia"):
            model.Piezak.ZformaAldKol = 'yellow'
        elif (ZformaAldSel.get() == "Cian"):
            model.Piezak.ZformaAldKol = 'cyan'
        elif (ZformaAldSel.get() == "Urdina"):
            model.Piezak.ZformaAldKol = 'blue'
        elif (ZformaAldSel.get() == "Laranja"):
            model.Piezak.ZformaAldKol = 'orange'
        elif (ZformaAldSel.get() == "Berdea"):
            model.Piezak.ZformaAldKol = 'green'
        elif (ZformaAldSel.get() == "Gorria"):
            model.Piezak.ZformaAldKol = 'red'
        elif (ZformaAldSel.get() == "Morea"):
            model.Piezak.ZformaAldKol = 'purple'
        elif (ZformaAldSel.get() == "Marroia"):
            model.Piezak.ZformaAldKol = 'brown'
        elif (ZformaAldSel.get() == "Larrosa"):
            model.Piezak.ZformaAldKol = 'pink'
        elif (ZformaAldSel.get() == "Grisa"):
            model.Piezak.ZformaAldKol = 'gray'

        if (TformaSel.get() == "Horia"):
            model.Piezak.TformaKol = 'yellow'
        elif (TformaSel.get() == "Cian"):
            model.Piezak.TformaKol = 'cyan'
        elif (TformaSel.get() == "Urdina"):
            model.Piezak.TformaKol = 'blue'
        elif (TformaSel.get() == "Laranja"):
            model.Piezak.TformaKol = 'orange'
        elif (TformaSel.get() == "Berdea"):
            model.Piezak.TformaKol = 'green'
        elif (TformaSel.get() == "Gorria"):
            model.Piezak.TformaKol = 'red'
        elif (TformaSel.get() == "Morea"):
            model.Piezak.TformaKol = 'purple'
        elif (TformaSel.get() == "Marroia"):
            model.Piezak.TformaKol = 'brown'
        elif (TformaSel.get() == "Larrosa"):
            model.Piezak.TformaKol = 'pink'
        elif (TformaSel.get() == "Grisa"):
            model.Piezak.TformaKol = 'gray'

        if (pantKolSel.get() == "Horia"):
            view.JokatuLeioa.pantKol = 'yellow'
        elif (pantKolSel.get() == "Cian"):
            view.JokatuLeioa.pantKol = 'cyan'
        elif (pantKolSel.get() == "Urdina"):
            view.JokatuLeioa.pantKol = 'blue'
        elif (pantKolSel.get() == "Laranja"):
            view.JokatuLeioa.pantKol = 'orange'
        elif (pantKolSel.get() == "Berdea"):
            view.JokatuLeioa.pantKol = 'green'
        elif (pantKolSel.get() == "Gorria"):
            view.JokatuLeioa.pantKol = 'red'
        elif (pantKolSel.get() == "Morea"):
            view.JokatuLeioa.pantKol = 'purple'
        elif (pantKolSel.get() == "Marroia"):
            view.JokatuLeioa.pantKol = 'brown'
        elif (pantKolSel.get() == "Larrosa"):
            view.JokatuLeioa.pantKol = 'pink'
        elif (pantKolSel.get() == "Grisa"):
            view.JokatuLeioa.pantKol = 'gray'

        window.destroy()
    global window
    window = tk.Tk()
    window.geometry("300x500")
    window.title("Pertsonalizazioa")
    toplbl = tk.Label(window, text="Nahi dituzun pertsonalizazioak aukeratu: ")
    laukilbl=tk.Label(window, text="Laukiaren kolorea hautatu:")
    laukiSel= ttk.Combobox(window, state="readonly", values=["Horia", "Cian", "Urdina", "Laranja", "Berdea", "Gorria", "Morea", "Marroia", "Larrosa", "Grisa"])

    zutabelbl = tk.Label(window, text="Zutabearen kolorea hautatu:")
    zutabeSel= ttk.Combobox(window, state="readonly", values=["Horia", "Cian", "Urdina", "Laranja", "Berdea", "Gorria", "Morea", "Marroia", "Larrosa", "Grisa"])

    Lformalbl = tk.Label(window, text="L formaren kolorea hautatu:")
    LformaSel= ttk.Combobox(window, state="readonly", values=["Horia", "Cian", "Urdina", "Laranja", "Berdea", "Gorria", "Morea", "Marroia", "Larrosa", "Grisa"])

    LformaAldlbl = tk.Label(window, text="Alderantzizko L formaren kolorea hautatu:")
    LformaAldSel= ttk.Combobox(window, state="readonly", values=["Horia", "Cian", "Urdina", "Laranja", "Berdea", "Gorria", "Morea", "Marroia", "Larrosa", "Grisa"])

    Zformalbl = tk.Label(window, text="Z formaren kolorea hautatu:")
    ZformaSel= ttk.Combobox(window, state="readonly", values=["Horia", "Cian", "Urdina", "Laranja", "Berdea", "Gorria", "Morea", "Marroia", "Larrosa", "Grisa"])

    ZformaAldlbl = tk.Label(window, text="Alderantzizko Z formaren kolorea hautatu:")
    ZformaAldSel= ttk.Combobox(window, state="readonly", values=["Horia", "Cian", "Urdina", "Laranja", "Berdea", "Gorria", "Morea", "Marroia", "Larrosa", "Grisa"])

    Tformalbl = tk.Label(window, text="T formaren kolorea hautatu:")
    TformaSel= ttk.Combobox(window, state="readonly", values=["Horia", "Cian", "Urdina", "Laranja", "Berdea", "Gorria", "Morea", "Marroia", "Larrosa", "Grisa"])

    pantKollbl = tk.Label(window, text="Atzeko kolorea hautatu:")
    pantKolSel= ttk.Combobox(window, state="readonly", values=["Horia", "Cian", "Urdina", "Laranja", "Berdea", "Gorria", "Morea", "Marroia", "Larrosa", "Grisa"])


    koloreaGorde= tk.Button(window, text="Pertsonalizazioa gorde")
    koloreaGorde.configure(command=KolAldatu)

    toplbl.pack()
    laukilbl.pack()
    laukiSel.pack()
    zutabelbl.pack()
    zutabeSel.pack()
    Lformalbl.pack()
    LformaSel.pack()
    LformaAldlbl.pack()
    LformaAldSel.pack()
    Zformalbl.pack()
    ZformaSel.pack()
    ZformaAldlbl.pack()
    ZformaAldSel.pack()
    Tformalbl.pack()
    TformaSel.pack()
    pantKollbl.pack()
    pantKolSel.pack()
    koloreaGorde.pack()

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

    btnPertsonalizatu = tk.Button(root, text="Pertsonalizatu")
    btnPertsonalizatu.configure(command=pertsonalizatu)


    txtErabil.pack()
    testua.pack()
    btnZ.pack()
    btnJolastu.pack()
    txtEdo.pack()
    btnPertsonalizatu.pack()
    btnKudeatu.pack()
    root.mainloop()
    return diff

#sortuMenu()