"""
Hierfür die 'personen.json' benutzen.
"""

import json

with open("personen.json", "r", encoding="utf8") as jsonFile:
    data = json.load(jsonFile)


def searchLetter(option, start, *end):
    #=> Überprüft ob der Typ = start ein String ist. (Start für die zu Suchenden Buchstaben)
    if type(start) is not str:
        print("in der Funktion: ", searchLetter.__name__, " befindet sich kein String")

    #=> Argumente überprüfen (*end)
    if any(e not in data for e in end):
        print(f"{end} eines der Argumente ist entweder falsch geschrieben oder befindet sich nicht in der JSON File")

    else:
        for key in data:
            for e in end:
                for i in range(len(data[key])):
                    if option == key:
                        #=> String Methoden: startswith() / endswith()
                        #=> für die Ausgabe, falls sich ein oder mehrere Buchstaben
                        #=> in der Datei befinden
                        if data[key][i].startswith(start) or data[key][i].endswith(start):
                            print(e, ": ", data[e][i])
        if all(option not in data for _ in range(len(data))):
            print(f"{option} nicht gefunden.")


### (1) das erste Argument (Beruf,Vorname, Nachname usw legt fest wonach gesucht werden soll
### (2) das zweite Argument ist für die Anfangs oder für die letzten Buchstaben
### (3) Die darauffolgenden Argumente geben die Suche aus.
searchLetter("Beruf", "Sch", "Vorname", "Nachname", "Alter")
