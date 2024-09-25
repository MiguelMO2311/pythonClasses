'''class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name="Adam"):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name="Eva"):
        super().__init__(name)

def creation():
    return [Man(), Woman()]

# Ejemplo de uso
adam_and_eve = creation()
print(adam_and_eve[0].name)  # Salida: Adam
print(adam_and_eve[1].name)  # Salida: Eva
'''

# forma de hacerlo por el profe con Interface: 
from abc import ABC, abstractmethod

def God():
    adan = Man("Adan")
    eva = Woman("Eva")
    return [adan, eva]

# Clase padre
class Human(ABC):
    def __init__(self, nombre : str):
        self.nombre = nombre

    def __str__(self):
        return f"{self.__class__.__name__}"
    
    @abstractmethod
    def mear(self):
        ...

# Herederos
class Man(Human):
    def mear(self):
        return "Meo de pie"

class Woman(Human):
    def mear(self):
        return "Meo sentada"

creacion = God()
print(creacion[0], creacion[1], creacion[0].mear())
