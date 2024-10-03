from abc import ABC, abstractmethod
import math

# Principio de Responsabilidad Única (SRP)
class Calculadora:
    def __init__(self, operacion):
        self.operacion = operacion  # DIP: Dependemos de una abstracción (Operacion)

    def calcular(self, a, b):
        return self.operacion.ejecutar(a, b)

# Calculadora Científica que hereda de Calculadora
class CalculadoraCientifica(Calculadora):
    def __init__(self, operacion):
        super().__init__(operacion)

    def calcular(self, a):
        return self.operacion.ejecutar(a)

# Principio de Abierto/Cerrado (OCP)
class Operacion(ABC):  # ISP: Interfaz específica para operaciones
    @abstractmethod
    def ejecutar(self, a, b=None):
        pass

class Suma(Operacion):
    def ejecutar(self, a, b):
        return a + b

class Resta(Operacion):
    def ejecutar(self, a, b):
        return a - b

class Seno(Operacion):
    def ejecutar(self, a, b=None):
        return math.sin(a)

class Coseno(Operacion):
    def ejecutar(self, a, b=None):
        return math.cos(a)

# Principio de Sustitución de Liskov (LSP)
# Las clases Suma, Resta, Seno y Coseno pueden sustituir a Operacion sin alterar el funcionamiento del programa.

# Principio de Segregación de Interfaces (ISP)
# Ya está implementado mediante el uso de la interfaz específica Operacion.

# Principio de Inversión de Dependencias (DIP)
# Ya está implementado mediante la inyección de dependencias en el constructor de Calculadora.

# Ejemplo de uso
suma = Suma()
resta = Resta()
seno = Seno()
coseno = Coseno()

# Uso de Calculadora para suma y resta
calculadora = Calculadora(suma)
print(f"Suma: {calculadora.calcular(5, 3)}")  # Debería imprimir: Suma: 8

calculadora = Calculadora(resta)
print(f"Resta: {calculadora.calcular(5, 3)}")  # Debería imprimir: Resta: 2

# Uso de CalculadoraCientifica para seno y coseno
calculadora_cientifica = CalculadoraCientifica(seno)
print(f"Seno: {calculadora_cientifica.calcular(math.pi / 2)}")  # Debería imprimir: Seno: 1.0

calculadora_cientifica = CalculadoraCientifica(coseno)
print(f"Coseno: {calculadora_cientifica.calcular(math.pi / 2)}")  # Debería imprimir: Coseno: 0.0
