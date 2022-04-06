import os, time, shutil
from pathlib import Path
#os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
#import vlc

def textopen(datei):
    try:
        d = open(datei)
    except:
        print("zugriff nicht erfolgreich")

    inhalt = d.read()
    d.close()
    print("Der Inhalt der Datei:\n")
    print(inhalt)
    print("-" * 25)

'''
    try:
        if datei.endswith('.txt'):
            try:
                p=open(datei)
            except:
                print("Fehlgeschlagen")
            stuff = p.read()
            p.close()
            print("Der Inhalt der Datei:\n")
            print(stuff)
            print("*" * 30)
        elif datei.endswith('.mp3' or '.mp4'):
            vlc_instance = vlc.Instance()
            player = vlc_instance.media_player_new()
            player.video_set_aspect_ratio("16:9")
            media = vlc_instance.media_new(datei)
            player.set_media(media)
            player.play()
            time.sleep(1.5)
            dauer = player.get_length() / 1000
            time.sleep(dauer)
        elif datei.endswith('.gif' or '.JPEG' or '.PNG'):
            kissen=Image.open(datei)
            kissen.show()
    except:
        print("Fehlgeschlagen, eventuell nicht unterstuetzter Format")
            '''


def pruf_laufwerk():
    hihi = []
    for x in range(65, 90):
        if os.path.exists(chr(x) + ":"):
            hihi.append(chr(x) + ":")
        else:
            continue
    print(hihi)


def info_datei(datei):
    tupo = os.stat(datei)
    groesse = tupo[6]
    print("Bytegroesse:", groesse)
    letzzugriff = time.localtime(tupo[7])
    print("letzter zugriff", time.strftime("%d.%m.%Y %H:%M:%S", letzzugriff))
    letzaenderung = time.localtime(tupo[8])
    print("letzter aenderung", time.strftime("%d.%m.%Y %H:%M:%S", letzaenderung))
    erstellzeit = time.localtime(tupo[9])
    print("Erstelldatum", time.strftime("%d.%m.%Y %H:%M:%S", erstellzeit))
    zugriffsrecht(datei)


def zugriffsrecht(datei):
    if os.access(datei, os.F_OK and os.X_OK):
        print("der Fad ist vorhanden und ausfuehrbar")
        if os.access(datei, os.R_OK):
            print("ist lesbar")
        elif os.access(datei, os.W_OK):
            print("ist schreibbar")
    else:
        print("nicht vorhanden")


def datei_loeschen(datei):
    try:
        os.remove(datei)
        print("Ist weg")
        print("-" * 25)
    except:
        print("joa ging irgendwie net")


def datei_kopieren(datei, nach):
    try:
        shutil.copy2(datei, nach)  # kopiert in directory (also voller Pfad (mit .txt) zu directory)
    except:
        print("ging net")


def datei_bewegen(datei, nach):
    try:
        shutil.move(datei, nach)
    except:
        print("ging net")


def datei_liste(datei):
    print("Vorhandenen Ordner/Daten")
    for filenam in os.listdir(datei):
        pathi=os.path.join(datei,filenam)
        if os.path.isdir(pathi):
            print("~ ",filenam)
        elif os.path.isfile(pathi):
            print(filenam)
    print()
    pass


pruf_laufwerk()
direcon = "D:\\testingbaun\\"  # iso in den testordner      #str(input("Eingabe des Pfads\n")
# datei_liste(direcon)
#if os.path.exists(direcon):
        #starte die While
#else: break
while True:
    print("Pfad: ", direcon)
    datei_liste(direcon)
    print("was soll gemacht werden?")
    eingabe = str(input("1. auswaehlen, 2. zurueck,3. kopieren, 4. verschieben, 5. loeschen 6. info 7. beenden\n"))
    if eingabe == "auswaehlen":
        datei_liste(direcon)
        add = str(input("Ja was?\n"))
        if os.path.isfile(os.path.join(direcon, add)):
            textopen(os.path.join(direcon, add))
        elif os.path.exists(os.path.join(direcon, add)):
            datei_liste(os.path.join(direcon, add))
            direcon = os.path.join(direcon, add)
            print("-" * 25)
        #direcon = os.path.join(direcon, add)
        # print("Derzeitiger Pfad", direcon)
    elif eingabe == "zurueck":
        direcon = str(Path(direcon).parents[0])
        print(direcon)
        print("-" * 25)
    elif eingabe == "loeschen":
        loeschen = str(input("was willste loeschen \n"))
        if os.path.exists(os.path.join(direcon, add)) or os.path.isfile(os.path.join(direcon, add)):
            datei_loeschen(os.path.join(direcon, add))
        else:
            print("nicht gefunden")
            print("-" * 25)
            continue
    elif eingabe == "kopieren":
        try:
            kopa = "D:\\testingbaun\\"  # neuer Pfad aufbau
            kopier = str(input("ja welche Datei \n"))
            kopiere = os.path.join(direcon, kopier)
            print("Ja Wohin den kopieren?")
            datei_liste(kopa)
            while True:
                hierhin = str(input("1.hierhin 2.Ordner eingeben 3.abbrechen\n"))
                '''if os.path.exists(os.path.join(kopa, hierhin)):
                    datei_liste(os.path.join(kopa, hierhin))
                    neuew = os.path.join(kopa, hierhin)'''
                if os.path.exists(os.path.join(kopa, hierhin)):
                    datei_liste(os.path.join(kopa, hierhin))
                    kopa = os.path.join(kopa, hierhin)
                    print(kopa)
                elif hierhin == "hierhin":
                    datei_kopieren(kopiere, kopa)
                elif hierhin == "abbrechen":
                    break
                else:
                    break
        except:
            print("ging net")
            break
    elif eingabe == "verschieben":
        try:
            verschie = "D:\\testingbaun\\"  # neuer Pfad aufbau
            verschieb = str(input("ja welche Datei \n"))
            verschiebe = os.path.join(direcon, verschieb)
            print("Ja Wohin den verschieben?")
            datei_liste(verschie)
            while True:
                nach = str(input("1.hierhin 2.Ordner eingeben 3.abbrechen\n"))
                '''if os.path.exists(os.path.join(verschie, nach)):
                    datei_liste(os.path.join(verschie, nach))
                    neuverschieb = os.path.join(verschie, nach)'''
                if os.path.exists(os.path.join(verschie,nach)):
                    datei_liste(os.path.join(verschie,nach))
                    verschie=os.path.join(verschie,nach)
                    print(verschie)
                elif nach == "hierhin":
                    datei_bewegen(verschiebe, verschie)
                    print(verschie)
                elif nach == "abbrechen":
                    break
                else:
                    break
        except:
            print("Ging net. ")
            break
    elif eingabe == "info":
        ansehen = str(input("was willste ansehen \n"))
        if os.path.isfile(os.path.join(direcon, ansehen)) or os.path.exists(os.path.join(direcon, ansehen)):
            informieren = os.path.join(direcon, ansehen)
            info_datei(informieren)
            print(informieren)
        else:
            print("Pfad exisiert net")
    elif eingabe == "beenden":
        break
    else:
        continue
