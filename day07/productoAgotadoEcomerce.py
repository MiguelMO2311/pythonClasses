class ProductoAgotadoError(Exception):
    def __init__(self, producto):
        self.producto = producto
        super().__init__(f"El producto '{self.producto}' está agotado.")

class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock

    def comprar(self, cantidad):
        if self.stock < cantidad:
            raise ProductoAgotadoError(self.nombre)
        self.stock -= cantidad
        print(f"Has comprado {cantidad} unidades de {self.nombre}. Quedan {self.stock} en stock.")

# Ejemplo de uso
try:
    producto = Producto("Laptop", 0)
    producto.comprar(1)
except ProductoAgotadoError as e:
    print(e)
