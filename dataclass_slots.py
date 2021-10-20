from dataclasses import dataclass, field
import time
import memory_profiler

print("Speicher Anfangs:", memory_profiler.memory_usage(), "\n")    # // Speicherverbrauch


class TypeA:                            # // Slots anlegen
    __slots__ = "vorname"


class TypeB(TypeA):
    __slots__ = "nachname"


class TypeC(TypeB):
    __slots__ = "vorname", "nachname", "firmenwagen"


@dataclass                              # // Dataclass
class DataType(TypeC):
    index: int = field(init=False, repr=False)
    profil: str
    staerke: int = 100

    def __post_init__(self):            # // Attribut setzen
        object.__setattr__(self, "index", self.staerke)

    def __str__(self):                  # // Ausgabe
        return f"{self.profil}\nFirmenwagen: {self.firmenwagen}\n{self.vorname} {self.nachname}"


dt = DataType("Profil_A:")
dt.firmenwagen = "Renault Twingo"
dt.vorname, dt.nachname = "Klaus", "Kleber"

start = time.process_time()             # // Timer starten

print(dt)
print(dt.__dict__)
print(TypeC.__slots__)
#print(dt.__dir__())
data = [d for d in dir(dt) if not d.startswith("__")]
print(data)
end = time.process_time() - start       # // Timer beenden

print(f"Top Speed: {end:.10F}\n")         # // Ausgabe der benötigten Zeit
print("Speicher Ende:", memory_profiler.memory_usage())
