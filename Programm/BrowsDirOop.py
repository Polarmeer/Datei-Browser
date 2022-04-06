import os, time, shutil

# os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
# import vlc
# from PIL import Image
Laufwerk = "D:\\"


class browsdir():
    def __init__(self, datpfad):
        self.datenpfad = datpfad

    def setDatpfad(self, neupfad):
        self.datenpfad = neupfad

    def getDatpfad(self):
        return self.datenpfad

    def datei_liste(self):
        print("Vorhanden Ordner\Daten")
        for datname in os.listdir(self.datenpfad):
            print(datname)
        print()
        pass

    def datatxt(self, pfad):
        try:

            p = open(pfad)

        except:
            print("Fehlgeschlagen")
        stuff = p.read()
        p.close()
        print("Der Inhalt der Datei:\n")
        print(stuff)
        print("*" * 30)

        '''
        try:
            if pfad.endswith('.txt'):
                try:
                    p=open(pfad)
                except:
                    print("Fehlgeschlagen")
                stuff = p.read()
                p.close()
                print("Der Inhalt der Datei:\n")
                print(stuff)
                print("*" * 30)
            elif pfad.endswith('.mp3' or '.mp4'):
                vlc_instance = vlc.Instance()
                player = vlc_instance.media_player_new()
                player.video_set_aspect_ratio("16:9")
                media = vlc_instance.media_new(pfad)
                player.set_media(media)
                player.play()
                time.sleep(1.5)
                dauer = player.get_length() / 1000
                time.sleep(dauer)
            elif pfad.endswith('.gif' or '.JPEG' or '.PNG'):
                pilli=Image.open(pfad)
                pilli.show()
        except:
            print("Fehlgeschlagen, eventuell nicht unterstuetzter Format")
            '''

    def deli(self, datei):
        try:
            os.remove(datei)
            print("Ist weg")
            print("*" * 30)
        except:
            print("joa ging irgendwie net")

    def detail_data(self, data):
        tupel = os.stat(data)
        bytegross = tupel[6]
        print("Bytegroesse:", bytegross)
        lasttake = time.localtime(tupel[7])
        print("letzter zugriff", time.strftime("%d.%m.%Y %H:%M:%S", lasttake))
        lastchange = time.localtime(tupel[8])
        print("letzter aenderung", time.strftime("%d.%m.%Y %H:%M:%S", lastchange))
        creati = time.localtime(tupel[9])
        print("Erstelldatum", time.strftime("%d.%m.%Y %H:%M:%S", creati))
        if os.access(data, os.F_OK and os.X_OK):
            print("der Fad ist vorhanden und ausfuehrbar")
            if os.access(data, os.R_OK):
                print("ist lesbar")
            elif os.access(data, os.W_OK):
                print("ist schreibbar")
        else:
            print("nicht vorhanden")


class io():  # copy/move
    def __init__(self, coppfad):
        self.coppa = coppfad

    def datei_liste(self):
        print("Vorhanden Ordner\Daten")
        for ordn in os.listdir(self.coppa):
            print(ordn)
        print()
        pass

    def setCopy(self, copy):
        self.coppa = copy

    def getCopy(self):
        return self.coppa

    def copydat(self, von, nach):
        try:
            shutil.copy2(von, nach)  # kopiert in directory (also voller Pfad (mit .txt) zu directory)
            print("Fertig")
        except:
            print("Fehlgeschlagen =(")
            print("*" * 30)

    def movedat(self, von, nach):
        try:
            shutil.move(von, nach)
        except:
            print("Fehlgeschlagen =(")
            print("*" * 30)


def check_laufwerk():
    vh_werk = []
    for x in range(65, 90):
        if os.path.exists(chr(x) + ":"):
            vh_werk.append(chr(x) + ":")
        else:
            continue
    print(vh_werk)


check_laufwerk()

hierbei = browsdir(Laufwerk)
# hierbei.check_laufwerk()
while True:
    print("Derzeitiger Pfad ", hierbei.getDatpfad())
    hierbei.datei_liste()
    print("Was soll gemacht werden?")
    eingabe = str(input("1. auswaehlen, 2. zurueck,3. kopieren, 4. verschieben, 5. loeschen 6. info 7. beenden\n"))
    if eingabe == "auswaehlen":
        hierbei.datei_liste()
        dat = str(input("Was soll ausgewaehlt werden?\n"))
        if os.path.isfile(os.path.join(hierbei.getDatpfad(), dat)):
            hierbei.datatxt(os.path.join(hierbei.getDatpfad(), dat))
        elif os.path.exists(os.path.join(hierbei.getDatpfad(), dat)):
            hierbei.setDatpfad(os.path.join(hierbei.getDatpfad(), dat))
            # print(hierbei.getDatpfad())
            # hierbei.datei_liste()
        else:
            continue
    elif eingabe == "zurueck":
        hierbei.setDatpfad(os.path.normpath(hierbei.getDatpfad() + os.sep + os.pardir))
        # print(hierbei.getDatpfad())
    elif eingabe == "loeschen":
        deli = str(input("Was soll geloescht werden?\n"))
        if os.path.exists(hierbei.getDatpfad()) or os.path.isfile(os.path.join(hierbei.getDatpfad())):
            hierbei.deli(hierbei.getDatpfad())
        else:
            print("Fehlgeschlagen")
            print("*" * 30)
    elif eingabe == "kopieren":
        try:
            copi1 = "D:\\testingbaun\\"
            copi2 = str(input("Welche Datei/Ordner soll kopiert werden?\n"))
            copi3 = os.path.join(hierbei.getDatpfad(), copi2)
            print("Wohin soll", copi2, "kopiert werden", sep=" ")
            copyby = io(copi1)
            copyby.datei_liste()
            while True:
                anfrage = str(input("1.hierhin 2.Ordner eingeben 3.abbrechen\n"))
                if os.path.exists(os.path.join(copi1, anfrage)):
                    copyby.setCopy(os.path.join(copi1, anfrage))
                    print(copyby.getCopy())
                    copyby.datei_liste()
                elif anfrage == "hierhin":
                    copyby.copydat(copi3, copyby.getCopy())
                    break
                elif anfrage == "abbrechen":
                    break
                else:
                    break
        except:
            print("lol", copi2, "ist wohl keine Datei/Ordner", sep=" ")
            break
    elif eingabe == "verschieben":
        try:
            move1 = "D:\\testingbaun\\"
            move2 = str(input("Welche Datei/Ordner soll verschoben werden?\n"))
            move3 = os.path.join(hierbei.getDatpfad(), move2)
            print("Wohin soll", move2, "kopiert werden", sep=" ")
            copyby = io(move1)
            copyby.datei_liste()
            while True:
                anfrage1 = str(input("1.hierhin 2.Ordner eingeben 3.abbrechen\n"))
                if os.path.exists(os.path.join(move1, anfrage1)):
                    copyby.setCopy(os.path.join(move1, anfrage1))
                    print(copyby.getCopy())
                    copyby.datei_liste()
                elif anfrage1 == "hierhin":
                    copyby.movedat(move3, copyby.getCopy())
                    break
                elif anfrage1 == "abbrechen":
                    break
                else:
                    break
        except:
            print("lol", move2, "ist wohl keine Datei/Ordner", sep=" ")
            break
    elif eingabe == "info":
        information = str(input("Welche Datei/Ordner willst du ansehen? \n"))
        if os.path.isfile(os.path.join(hierbei.getDatpfad(), information)) or \
                os.path.exists(os.path.join(hierbei.getDatpfad(), information)):
            informieren = os.path.join(hierbei.getDatpfad(), information)
            print(informieren)
            hierbei.detail_data(informieren)
        else:
            print("Pfad mit", information, "exisiert net ", sep=" ")
    elif eingabe == "beenden":
        break
    else:
        continue
