"""
Bestimmte Schlagwörter in 'nested-lists' durchsuchen:
"""

import memory_profiler

print("Memory Anfang: %sMb \n" % (*memory_profiler.memory_usage(),))

tab = [
    ['Vorname', "Nachname", "Geburtstag", "Beruf"],
    ["Anton", "Müller", "23.12.1987", "Aussendienst"],
    ["Maja", "Seiler", "19.09.1978", "Aussendienst"],
    ["Helge", "Meier", "01.01.2000", "Sänger"],
    ["Heiko", "Abel", "04.09.1955", "Lehrer"]
]

#print(dir(tab))

###===>>> OPTION 1: Suche mit Schlagwörtern
def searchFunc(option: str, *args: any) -> None:
    if type(option) is not str:
        print(f"Ungültiger Datentyp: {type(option).__name__.upper()}")
    else:
        arg: list = []
        if option in tab[0]:
            index: int = tab[0].index(option)
            for name in args:
                arg.append(name)
                if any(name in tab[x] for x in range(len(tab))):
                    print(*[tab[x][index] for x in range(len(tab)) if name in tab[x]])
                else:
                    print(f"{name} {type(name)} befindet sich nicht in der Liste.")
        else:
            print(f"Ungültige Eingabe: {option}")


searchFunc("Vorname", "Finanzberater", "Schauspieler", "Sänger", "Lehrer", 123)


###===>>> OPTION 2: Suche mit Index
def searchFunc2(*args, **kwargs):
    for key, val in kwargs.items():
        for opt in args:
            if opt in tab[0]:
                if 0 < val < len(tab):
                    for i in range(len(tab)):
                        if key in tab[i]:
                            index = tab[0].index(opt)
                            print(f"{opt}: {tab[val][index]}")
                    if all(key not in tab[x] for x in range(len(tab))):
                        print(f"{key} nicht gefunden")
                        break
                else:
                    print(f"Ungültiger Index.")
                    break
            else:
                print(f"Ungültige Eingabe: {opt}")


#searchFunc2("Vorname", "Nachname", "Beruf", Beruf=1)


print("\nMemory Ende: %sMb \n" % (*memory_profiler.memory_usage(),))
