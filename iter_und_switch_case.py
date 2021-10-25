import os


def repeat(num: int, rep=1):
    """Wiederholungen von Zahlen"""
    # repeat(10, rep=3) --> 10, 10, 10
    for _ in range(rep):
        yield num


def sort_nums_min(nums: list) -> list:
    """Zahlen nach der Groesse sortieren, aufsteigend: (bubble sort)"""
    # print(sort_nums_min([40,10, 50, 100, 70, 20])) --> [10, 20, 40, 50, 70, 100]
    for x in range(len(nums)-1, 0, -1):     # Umgekehrt iterieren (5, 4, 3, 2 ...) step: -1
        for index in range(x):
            if nums[index] > nums[index+1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
    return nums


def sort_nums_max(nums: list) -> list:
    """Zahlen nach der Groesse sortieren, absteigend: (bubble sort)"""
    # print(sort_nums_max([40,10, 50, 100, 70, 20])) --> [100, 70, 50, 40, 20, 10]
    for x in range(len(nums)-1, 0, -1):
        for index in range(x):
            if nums[index] < nums[index+1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
    return nums


def word_slice(*args, end=1):
    """Slice durch Argumente"""
    # word_slice("Johannes", "Claudia", end=3) --> "Joh", "Cla"
    for arg in args:
        yield arg[:end]


def word_decorator(*args, pos=0, char=None):
    # word_decorator("Jürgen", "Meier", pos=1, char="*") --> "J*rgen", "M*ier"
    for arg in args:
        arg = arg[:pos] + char + arg[pos+1:]
        yield arg


def duplicate_remover(word: str, words: list) -> list:
    """Entfernt ein Wort welches mehrfach auftaucht aus der Liste"""
    # print(duplicate_remover("Joe", lst))
    while word in words:
        words.remove(word)
    return words


"""Switch/Case mit Python 3.10"""

l: list = ["Anton", "Jonny", "Angelika", "Olga"]

string = input("(1) Liste -> Unicode: \n(2) Prompt öffnen\nEingabe: ")

match string:
    case "1":
        for i, val in enumerate(l):
            print(f"\nName: {val}")
            for j, w in enumerate(val):             # Unicode aus memoryview / Namen aus der Liste encoden
                print(f"Unicode: {memoryview(val.encode('utf-8'))[j]:<20} Char: {w} ")
                if j == len(l[i])-1:
                    print("#"*40)
    case "2":
        os.system("start cmd /K python main.py")    # Prompt öffnen /main.py erforderlich
    case default:
        raise ValueError(f"Eingabe nicht gefunden: {default}")
