class Personaje:
    def __init__(self, nombre: str, rol: str):
        self.nombre = nombre
        self.rol = rol
        self.puntos_vida = 100
        self.nivel = 1
        self.inventario = ["Espada"]  # Añadimos una espada al inventario
        print(f"Se ha creado a {self.nombre}, un {self.rol} de nivel {self.nivel}!")

    def ataque_basico(self):
        print(f"{self.nombre} ha atacado!")

    def ataque_con_espada(self, objetivo):
        if "Espada" in self.inventario:
            print(f"{self.nombre} ataca a {objetivo} con una espada!")
        else:
            print(f"{self.nombre} no tiene una espada para atacar.")

# Crear un nuevo personaje y usar los métodos de ataque
nuevo_personaje = Personaje("Legolas", "Arquero")
nuevo_personaje.ataque_basico()
nuevo_personaje.ataque_con_espada("Orco")
print(nuevo_personaje.inventario)


# esta es la version que ha hecho Joaquín

''' class Personaje:
    def __init__(self, nombre: str, rol: str):
        self.nombre = nombre
        self.rol = rol
        self.puntos_vida = 100
        self.nivel = 1
        self.inventario = []
        self.daño = 10
        print(f"Se ha creado a {self.nombre}, un {self.rol} de nivel {self.nivel}!")
 
    def ataque_basico(self, arma):
        if len(self.inventario) > 0:
            print(f"{self.nombre} ha atacado con un arma! Y su daño es {self.daño + arma.ataque}")
        else:
            print(f"{self.nombre} ha atacado! Y su daño es {self.daño}")

    def coger_arma(self, arma):
        self.inventario.append(arma)
        print(f"Has cogido un {arma.nombre}!")

class Arma:
    def __init__(self, nombre: str, ataque: int):
        self.nombre = nombre
        self.ataque = ataque
        '''