from abc import ABC, abstractmethod
from dataclasses import dataclass

# Interfaz para dispositivos con estado
class Estado(ABC):
    """
    Interfaz para dispositivos con estado.
    Define los métodos que deben ser implementados por cualquier dispositivo que pueda ser encendido o apagado.
    """
    @abstractmethod
    def encender(self) -> None:
        """
        Enciende el dispositivo.
        """
        pass

    @abstractmethod
    def apagar(self) -> None:
        """
        Apaga el dispositivo.
        """
        pass

# Clase para la bombilla utilizando dataclass
@dataclass
class Bombilla(Estado):
    """
    Clase que representa una bombilla.
    Implementa la interfaz Estado.
    """
    esta_encendida: bool = False

    def encender(self) -> None:
        """
        Enciende la bombilla.
        """
        self.esta_encendida = True
        print("La bombilla está encendida.")

    def apagar(self) -> None:
        """
        Apaga la bombilla.
        """
        self.esta_encendida = False
        print("La bombilla está apagada.")

# Clase para el interruptor
class Interruptor:
    """
    Clase que representa un interruptor.
    Controla el estado de un dispositivo conmutable.
    """
    def __init__(self, dispositivo: Estado) -> None:
        """
        Inicializa el interruptor con un dispositivo conmutable.

        Args:
            dispositivo (Estado): El dispositivo que será controlado por el interruptor.
        """
        self.dispositivo: Estado = dispositivo
        self.estado: str = "apagado"

    def presionar(self) -> None:
        """
        Alterna el estado del dispositivo entre encendido y apagado.
        """
        if self.estado == "apagado":
            self.dispositivo.encender()
            self.estado = "encendido"
        else:
            self.dispositivo.apagar()
            self.estado = "apagado"

# Ejemplo de uso
if __name__ == "__main__":
    bombilla: Bombilla = Bombilla()
    interruptor: Interruptor = Interruptor(bombilla)

    interruptor.presionar()  # Enciende la bombilla
    interruptor.presionar()  # Apaga la bombilla


'''
Explicación del código:
Interfaz Estado: Define los métodos encender y apagar que deben ser implementados por cualquier dispositivo que pueda ser encendido o apagado.
Clase Bombilla utilizando dataclass: Simplifica la definición de la clase Bombilla al utilizar dataclass para manejar los datos. La lógica de encender y apagar se mantiene.
Clase Interruptor: Controla el estado del dispositivo (en este caso, la bombilla) y alterna entre encendido y apagado cuando se presiona el interruptor.

Principios S.O.L.I.D.:
S (Principio de Responsabilidad Única): Cada clase tiene una única responsabilidad.
O (Principio de Abierto/Cerrado): Las clases están abiertas para extensión pero cerradas para modificación.
L (Principio de Sustitución de Liskov): La clase Bombilla puede ser sustituida por cualquier otra clase que implemente la interfaz Estado.
I (Principio de Segregación de Interfaces): La interfaz Estado es específica y no obliga a implementar métodos innecesarios.
D (Principio de Inversión de Dependencias): La clase Interruptor depende de una abstracción (Estado) en lugar de una implementación concreta.

Este código sigue siendo una base sólida y puede ser extendido en el futuro para incluir más funcionalidades y dispositivos.'''