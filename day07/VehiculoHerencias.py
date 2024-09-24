class Rueda:
    def __init__(self, marca: str = "Michelin"):
        self.marca: str = marca
        self.pinchada: bool = False

    def pincharse(self) -> None:
        self.pinchada = True

    def __str__(self) -> str:
        return f"Rueda {self.marca}, pinchada: {self.pinchada}"

class Asiento:
    def __init__(self, material: str = "Tela"):
        self.material: str = material

    def __str__(self) -> str:
        return f"Asiento de {self.material}"

class Puerta:
    def __init__(self, tipo: str = "Estándar"):
        self.tipo: str = tipo

    def __str__(self) -> str:
        return f"Puerta {self.tipo}"

class Motor:
    def __init__(self, tipo: str):
        self.tipo: str = tipo

    def __str__(self) -> str:
        return f"Motor {self.tipo}"

class Vehiculo:
    def __init__(self, matricula: str, marca: str, color: str, motor: Motor):
        self.matricula: str = matricula
        self.marca: str = marca
        self.color: str = color
        self.ruedas: list[Rueda] = []
        self.asientos: list[Asiento] = []
        self.puertas: list[Puerta] = []
        self.motor: Motor = motor

    def agregar_rueda(self, rueda: Rueda) -> None:
        self.ruedas.append(rueda)

    def agregar_asiento(self, asiento: Asiento) -> None:
        self.asientos.append(asiento)

    def agregar_puerta(self, puerta: Puerta) -> None:
        self.puertas.append(puerta)

    def __str__(self) -> str:
        return f"{self.marca} {self.color} con matrícula {self.matricula}, {len(self.ruedas)} ruedas, motor {self.motor}, {len(self.asientos)} asientos y {len(self.puertas)} puertas"

class Coche(Vehiculo):
    def __init__(self, matricula: str, marca: str, color: str, motor: Motor):
        super().__init__(matricula, marca, color, motor)
        self.tipo_carroceria: str = "Deportivo"

    def __str__(self) -> str:
        return f"{super().__str__()}, tipo de carrocería {self.tipo_carroceria}"

class Moto(Vehiculo):
    def __init__(self, matricula: str, marca: str, color: str, motor: Motor):
        super().__init__(matricula, marca, color, motor)

    def __str__(self) -> str:
        return f"{super().__str__()}"

# Crear instancias de Coche y Moto con matrículas diferentes
motor_coche = Motor("V12")
motor_moto = Motor("500cc")

coche = Coche("1234-ABC", "BMW", "Rojo", motor_coche)
moto = Moto("5678-DEF", "Yamaha", "Azul", motor_moto)

# Agregar ruedas, asientos y puertas
for _ in range(4):
    coche.agregar_rueda(Rueda())

for _ in range(2):
    moto.agregar_rueda(Rueda())

for _ in range(5):
    coche.agregar_asiento(Asiento())

moto.agregar_asiento(Asiento())

for _ in range(4):
    coche.agregar_puerta(Puerta())

# Imprimir detalles de los vehículos
print(coche)
print(moto)
