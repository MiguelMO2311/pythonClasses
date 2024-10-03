from abc import ABC, abstractmethod
from typing import List, Dict, Any
from dataclasses import dataclass

class IProcesable(ABC):
    """
    Interfaz para objetos procesables.
    """

    @abstractmethod
    def procesar(self, valores_posicion: List[Any], valores_clave: Dict[str, Any]) -> None:
        """
        Procesa los valores de posición y clave.
        """
        pass

@dataclass
class Procesador(IProcesable):
    """
    Clase concreta que implementa la interfaz IProcesable.
    """

    def procesar(self, valores_posicion: List[Any], valores_clave: Dict[str, Any]) -> None:
        """
        Implementación del método procesar.
        """
        print(f"Valores de posición: {valores_posicion}")
        print(f"Valores clave: {valores_clave}")

def procesar_objeto(valores_posicion: List[Any], valores_clave: Dict[str, Any], objeto: Any) -> None:
    """
    Función que procesa los valores utilizando un objeto que implementa la interfaz IProcesable.
    
    :param valores_posicion: Lista de valores de posición.
    :param valores_clave: Diccionario de valores clave.
    :param objeto: Objeto que implementa la interfaz IProcesable.
    """
    try:
        if isinstance(objeto, IProcesable):
            objeto.procesar(valores_posicion, valores_clave)
            print(f"El objeto corresponde a la clase: {objeto.__class__.__name__}")
        else:
            raise TypeError(f"El objeto proporcionado no implementa la interfaz IProcesable. Es de la clase: {objeto.__class__.__name__}")
    except TypeError as e:
        print(e)

# Ejemplo de uso
@dataclass
class Persona(IProcesable):
    nombre: str

    def procesar(self, valores_posicion: List[Any], valores_clave: Dict[str, Any]) -> None:
        print(f"Valores de posición: {valores_posicion}")
        print(f"Valores clave: {valores_clave}")
        print(f"Nombre de la persona: {self.nombre}")

valores_posicion: List[int] = [1, 2, 3]
valores_clave: Dict[str, int] = {"a": 10, "b": 20}
objeto: IProcesable = Persona(nombre="Antonio")
procesar_objeto(valores_posicion, valores_clave, objeto)

# Otro ejemplo de uso con una clase diferente
@dataclass
class Producto(IProcesable):
    nombre: str
    precio: float

    def procesar(self, valores_posicion: List[Any], valores_clave: Dict[str, Any]) -> None:
        print(f"Valores de posición: {valores_posicion}")
        print(f"Valores clave: {valores_clave}")
        print(f"Nombre del producto: {self.nombre}")
        print(f"Precio del producto: {self.precio}")

objeto_producto: IProcesable = Producto(nombre="Laptop", precio=999.99)
procesar_objeto(valores_posicion, valores_clave, objeto_producto)

# Ejemplo de uso con un objeto que no implementa IProcesable
class NoProcesable:
    pass

objeto_no_procesable = NoProcesable()
procesar_objeto(valores_posicion, valores_clave, objeto_no_procesable)


# Definición de la Interfaz IProcesable:
# Define una interfaz abstracta con un método procesar que debe ser implementado por cualquier clase que herede de IProcesable.
# Definición de la Clase Procesador:
# Implementa la interfaz IProcesable y define el método procesar que imprime los valores de posición y clave.
# Utiliza dataclass para simplificar la definición de la clase.
# Definición de la Función procesar_objeto:
# Verifica si el objeto proporcionado implementa la interfaz IProcesable.
# Llama al método procesar del objeto.
# Imprime el nombre de la clase del objeto utilizando objeto.__class__.__name__.
# Si el objeto no implementa IProcesable, lanza un error TypeError y lo maneja con try y except.
# Ejemplo de Uso con Persona:
# Crea una instancia de Persona con el nombre “Antonio”, define los valores de posición y clave, y llama a la función procesar_objeto con estos valores y el objeto.
# Ejemplo de Uso con Producto:
# Crea una instancia de Producto con el nombre “Laptop” y precio 999.99, y llama a la función procesar_objeto con estos valores y el objeto.
# Ejemplo de Uso con un Objeto que no Implementa IProcesable:
# Crea una instancia de NoProcesable que no implementa IProcesable y trata de llamar a la función procesar_objeto. La función lanzará un error TypeError indicando que el objeto no implementa la interfaz IProcesable y lo manejará con try y except.
# Cómo se Cumplen los Principios SOLID
# Responsabilidad Única (SRP): Cada clase y función tiene una única responsabilidad clara.
# Abierto/Cerrado (OCP): Las clases pueden extenderse sin modificar su código existente.
# Sustitución de Liskov (LSP): Las clases concretas pueden sustituir a las abstracciones sin alterar el comportamiento esperado.
# Segregación de Interfaces (ISP): Las interfaces definen solo los métodos necesarios.
# Inversión de Dependencias (DIP): Las funciones y clases dependen de abstracciones en lugar de implementaciones concretas.
