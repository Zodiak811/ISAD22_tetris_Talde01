def register():
    db = open("database.txt", "r")
    Username = input ("Erabiltzaile izena: ")
    Password = input("Pasahitza: ")
    Password1 = input("Pasahitza konfirmatu: ")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d,f))

    if Password != Password1:
        print("Pasahitzak ezberdinak dira")
        register()
    else:
        if len(Password)<=6:
            print("Pasahitza oso motza da")
            register()
        elif Username in d:
            print("erabiltzaile izen hori jada existitzen da")
            register()
        else:
            db = open("database.txt", "a")
            db.write(Username+", "+Password+"\n")
            print("Lo hise bien")

def access():
    db = open("database.txt", "r")
    print("Login: ")
    Username = input("Erabiltzaile izena: ")
    Password = input("Pasahitza: ")
    if not len(Username or Password)<1:
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
                        print("Ongi etorri, "+ Username)
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


def changePassword():
    db = open("database.txt", "r")
    Username = input("Erabiltzaile izena: ")
    Password = input("Pasahitza: ")
    Npassword = input("Pasahitz berria: ")
    if not len(Username or Password)<1:
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

def home(option=None):
    option = input("Login | Signup | Aldatu:")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    elif option == "Aldatu":
        changePassword()
    else:
        print("Mesedez opzio bat sartu")
home()