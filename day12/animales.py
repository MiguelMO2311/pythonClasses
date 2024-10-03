from abc import ABC, abstractmethod

# Principio de Segregación de Interfaces (ISP)
class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Nadador(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Perro:
    def ladrar(self):
        return "Guau!"

class Paloma(Volador):
    def volar(self):
        return "La paloma está volando."

class Ballena(Nadador):
    def nadar(self):
        return "La ballena está nadando."

class PezVolador(Volador, Nadador):
    def volar(self):
        return "El pez volador está volando."

    def nadar(self):
        return "El pez volador está nadando."

class Pato(Volador, Nadador):
    def volar(self):
        return "El pato está volando."

    def nadar(self):
        return "El pato está nadando."

class Pinguino(Nadador):
    def nadar(self):
        return "El pingüino está nadando."

# Ejemplo de uso
perro = Perro()
print(perro.ladrar())  # Debería imprimir: Guau!

paloma = Paloma()
print(paloma.volar())  # Debería imprimir: La paloma está volando.

ballena = Ballena()
print(ballena.nadar())  # Debería imprimir: La ballena está nadando.

pez_volador = PezVolador()

print(pez_volador.nadar())  # Debería imprimir: El pez volador está nadando.

pato = Pato()
print(pato.volar())  # Debería imprimir: El pato está volando.
print(pato.nadar())  # Debería imprimir: El pato está nadando.

pinguino = Pinguino()
print(pinguino.nadar())  # Debería imprimir: El pingüino está nadando.
