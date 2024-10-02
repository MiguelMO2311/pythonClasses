from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

@dataclass
class Producto(ABC):
    codigo: int
    ref: str
    nombre: str
    marca: str

    def mostrar_informacion(self) -> str:
        return f"Código: {self.codigo}, Ref: {self.ref}, Nombre: {self.nombre}, Marca: {self.marca}"

@dataclass
class Camiseta(Producto):
    tipo: str
    talla: str
    color: str
    stock: int = 15  # Stock inicializado con 15

    def mostrar_informacion(self) -> str:
        return super().mostrar_informacion() + f", Tipo: {self.tipo}, Talla: {self.talla}, Color: {self.color}, Stock: {self.stock}"

    def comprar(self, cantidad: int):
        self.stock += cantidad

    def vender(self, cantidad: int):
        if self.stock >= cantidad:
            self.stock -= cantidad
            print("Producto vendido.")
        else:
            print(f"No hay suficiente stock para vender. Solo quedan {self.stock} unidades.")

@dataclass
class Pantalon(Producto):
    tipo: str
    talla: str
    color: str
    stock: int = 15  # Stock inicializado con 15

    def mostrar_informacion(self) -> str:
        return super().mostrar_informacion() + f", Tipo: {self.tipo}, Talla: {self.talla}, Color: {self.color}, Stock: {self.stock}"

    def comprar(self, cantidad: int):
        self.stock += cantidad

    def vender(self, cantidad: int):
        if self.stock >= cantidad:
            self.stock -= cantidad
            print("Producto vendido.")
        else:
            print(f"No hay suficiente stock para vender. Solo quedan {self.stock} unidades.")

# Función para buscar productos por nombre
def buscar_producto_por_nombre(nombre: str, productos: List[Producto]) -> Producto:
    nombre = nombre.lower()
    for producto in productos:
        if producto.nombre.lower() == nombre:
            return producto
    return None

# Función para imprimir el inventario
def imprimir_inventario(productos: List[Producto]):
    print("\nInventario de productos:")
    for producto in productos:
        print(producto.mostrar_informacion())

# Lista de productos
productos = [
    Camiseta(codigo=100, ref="camiRMHom", nombre="Camiseta Real Madrid", marca="Adidas", tipo="Futbol", talla="L", color="Naranja"),
    Camiseta(codigo=101, ref="camiBarcMujer", nombre="Camiseta Barcelona", marca="Adidas", tipo="Futbol", talla="L", color="Azulgrana"),
    Pantalon(codigo=200, ref="pantaRMMujer", nombre="Pantalon Basket Real Madrid", marca="Adidas", tipo="Basket", talla="M", color="Blanco")
]

# Interacción con el usuario
nombre_producto = input("Introduce el nombre del producto que deseas buscar: ")
producto_encontrado = buscar_producto_por_nombre(nombre_producto, productos)

if producto_encontrado:
    print(f"Producto encontrado: {producto_encontrado.mostrar_informacion()}")
    accion = input("¿Deseas comprar o vender este producto? (comprar/vender): ").strip().lower()
    cantidad = int(input("Introduce la cantidad: "))
    if accion == "comprar":
        producto_encontrado.comprar(cantidad)
        print("Producto comprado.")
    elif accion == "vender":
        producto_encontrado.vender(cantidad)
    else:
        print("Acción no reconocida.")
else:
    print("Producto no encontrado.")

# Imprimir inventario actualizado
imprimir_inventario(productos)
