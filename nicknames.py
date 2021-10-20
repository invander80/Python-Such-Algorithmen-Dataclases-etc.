class Name2Check(object):
    def __init__(self, check):
        self.check = check

    def __call__(self):
        lst = []
        num = int(input("Wieviele Namen möchtest du eintragen? "))
        for x in range(num):
            na = str(input("Namen hinzufügen: "))
            lst.append(na)
        check_names = filter(lambda name: name == self.check, lst)
        return check_names


class AddNicks(object):
    def __init__(self):
        self.string_name = str(input("Bitte den Namen zu vergleichen eingeben: "))
        self.name2check = Name2Check(self.string_name)
        self.num = 1

    def __call__(self):
        lst = []
        for name in self.name2check():
            if self.string_name == name:
                name += f"{self.num}"           # // ggf eine Liste mit Speziellen Nicks hinzufügen
                lst.append(name)
                self.num += 1
        return lst


a = AddNicks()
print(a())
