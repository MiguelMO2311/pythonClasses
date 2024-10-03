from abc import ABC, abstractmethod
from dataclasses import dataclass

# Principio de Segregación de Interfaces (ISP)
class Volador(ABC):
    """
    Interfaz para animales que pueden volar.
    """
    @abstractmethod
    def volar(self) -> str:
        pass

class Nadador(ABC):
    """
    Interfaz para animales que pueden nadar.
    """
    @abstractmethod
    def nadar(self) -> str:
        pass

class Caminador(ABC):
    """
    Interfaz para animales que pueden andar.
    """
    @abstractmethod
    def andar(self) -> str:
        pass

@dataclass
class Perro(Caminador):
    """
    Clase que representa un perro.
    """
    

    def andar(self) -> str:
        return "El perro está andando."

@dataclass
class Paloma(Volador, Caminador):
    """
    Clase que representa una paloma.
    """
    def volar(self) -> str:
        return "La paloma está volando."

    def andar(self) -> str:
        return "La paloma está andando."

@dataclass
class Ballena(Nadador):
    """
    Clase que representa una ballena.
    """
    def nadar(self) -> str:
        return "La ballena está nadando."

@dataclass
class PezVolador(Nadador):
    """
    Clase que representa un pez volador.
    """
    def volar(self) -> str:
        return "El pez volador está volando."

    def nadar(self) -> str:
        return "El pez volador está nadando."

@dataclass
class Pato(Volador, Nadador, Caminador):
    """
    Clase que representa un pato.
    """
    def volar(self) -> str:
        return "El pato está volando."

    def nadar(self) -> str:
        return "El pato está nadando."

    def andar(self) -> str:
        return "El pato está andando."

@dataclass
class Pinguino(Nadador, Caminador):
    """
    Clase que representa un pingüino.
    """
    def nadar(self) -> str:
        return "El pingüino está nadando."

    def andar(self) -> str:
        return "El pingüino está andando."

# Fábrica de animales
class FabricaDeAnimales:
    """
    Fábrica para crear instancias de animales.
    """
    @staticmethod
    def crear_animal(tipo: str):
        if tipo == "perro":
            return Perro()
        elif tipo == "paloma":
            return Paloma()
        elif tipo == "ballena":
            return Ballena()
        elif tipo == "pez_volador":
            return PezVolador()
        elif tipo == "pato":
            return Pato()
        elif tipo == "pinguino":
            return Pinguino()
        else:
            raise ValueError(f"Tipo de animal desconocido: {tipo}")

# Ejemplo de uso
if __name__ == "__main__":
    perro: Perro = FabricaDeAnimales.crear_animal("perro")
    print(perro.andar())  # Debería imprimir: El perro está andando.

    paloma: Paloma = FabricaDeAnimales.crear_animal("paloma")
    print(paloma.volar())  # Debería imprimir: La paloma está volando.
    print(paloma.andar())  # Debería imprimir: La paloma está andando.

    ballena: Ballena = FabricaDeAnimales.crear_animal("ballena")
    print(ballena.nadar())  # Debería imprimir: La ballena está nadando.

    pez_volador: PezVolador = FabricaDeAnimales.crear_animal("pez_volador")
    print(pez_volador.nadar())  # Debería imprimir: El pez volador está nadando.

    pato: Pato = FabricaDeAnimales.crear_animal("pato")
    print(pato.volar())  # Debería imprimir: El pato está volando.
    print(pato.nadar())  # Debería imprimir: El pato está nadando.
    print(pato.andar())  # Debería imprimir: El pato está andando.

    pinguino: Pinguino = FabricaDeAnimales.crear_animal("pinguino")
    print(pinguino.nadar())  # Debería imprimir: El pingüino está nadando.
    print(pinguino.andar())  # Debería imprimir: El pingüino está andando.
