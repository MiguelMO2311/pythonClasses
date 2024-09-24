


# sistema para subir experiencia o nivel al personaje de la clase anterior

class Personaje:
    def __init__(self, nombre: str, rol: str):
        self.nombre = nombre
        self.rol = rol
        self.puntos_vida = 100
        self.nivel = 1
        self.experiencia = 0  # Añadimos una propiedad de experiencia
        self.inventario = [] 
        print(f"Se ha creado a {self.nombre}, un {self.rol} de nivel {self.nivel}!")

    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo}!")
        self.ganar_experiencia(50)  # Gana 50 puntos de experiencia por cada ataque

    def ganar_experiencia(self, puntos):
        self.experiencia += puntos
        print(f"{self.nombre} ha ganado {puntos} puntos de experiencia.")
        if self.experiencia >= 100:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0  # Reseteamos la experiencia al subir de nivel
        print(f"¡{self.nombre} ha subido al nivel {self.nivel}!")

# Ejemplo de uso
personaje = Personaje("Aragorn", "Guerrero")
personaje.atacar("Orco")
personaje.atacar("Troll")
print(personaje.inventario)
