class ConexionBaseDatosError(Exception):
    def __init__(self, mensaje: str):
        self.mensaje: str = mensaje
        super().__init__(f"Error de conexión a la base de datos: {self.mensaje}")

class BaseDatos:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.conectado: bool = False

    def conectar(self) -> None:
        # Simulamos un intento de conexión fallido
        if not self.conectado:
            raise ConexionBaseDatosError(f"No se pudo conectar a la base de datos '{self.nombre}'")

# Ejemplo de uso
try:
    base_datos: BaseDatos = BaseDatos("MiBaseDeDatos")
    base_datos.conectar()
except ConexionBaseDatosError as e:
    print(e)
