from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Producto(ABC):
    codigo: int
    ref: str
    nombre: str
    stock: int
    marca: str

    def mostrar_informacion(self) -> str:
        return f"Código: {self.codigo}, Ref: {self.ref}, Nombre: {self.nombre}, Stock: {self.stock}, Marca: {self.marca}"

@dataclass
class Camiseta(Producto):
    tipo: str
    talla: str
    color: str

    def mostrar_informacion(self) -> str:
        return super().mostrar_informacion() + f", Tipo: {self.tipo}, Talla: {self.talla}, Color: {self.color}"

@dataclass
class Pantalon(Producto):
    tipo: str
    talla: str
    color: str

    def mostrar_informacion(self) -> str:
        return super().mostrar_informacion() + f", Tipo: {self.tipo}, Talla: {self.talla}, Color: {self.color}"

# Instanciación de los objetos
producto = Camiseta(codigo=100, ref="camiRMHom", nombre="Camiseta Real Madrid 24/25", stock=30, marca="Adidas", tipo="Futbol", talla="L", color="Naranja")
producto2 = Pantalon(codigo=200, ref="pantaRMMujer", nombre="Pantalon Basket Real Madrid 24/25", stock=22, marca="Adidas", tipo="Basket", talla="M", color="Blanco")

# Mostrar información de los productos
print(producto.mostrar_informacion())
print(producto2.mostrar_informacion())
