from abc import ABC

class PersonaAcademica(ABC):  # Interfaz
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

class Alumno(PersonaAcademica):
    def __init__(self, nombre: str, edad: int, *, delegado: bool = False):
        super().__init__(nombre, edad)
        self.notas = []
        self.es_delegado = delegado

    def estudiar(self):
        ultima_nota = self.notas[-1] if self.notas else None
        if not ultima_nota or ultima_nota < 5:
            print("El alumno está estudiando muy duramente, ya que está motivado")
        else:
            print("El alumno está estudiando")

class Profesor(PersonaAcademica):
    def __init__(self, nombre: str, edad: int, salario: float, asignatura: str):
        super().__init__(nombre, edad)
        self.salario = salario
        self.asignatura = asignatura

    @staticmethod
    def impartir_clase():
        print("El profesor está impartiendo clase")

    def asignar_delegado_de_clase(self, aula: 'Aula'):
        if not aula.alumnos:
            print("No hay alumnos en el aula para asignar como delegado")
            return

        mejor_alumno = max(aula.alumnos, key=lambda alumno: sum(alumno.notas) / len(alumno.notas) if alumno.notas else 0)
        
        for a in aula.alumnos:
            if a.es_delegado:
                a.es_delegado = False
                print(f"El alumno {a.nombre} ya no es delegado de clase")
        
        mejor_alumno.es_delegado = True
        print(f"El alumno {mejor_alumno.nombre} se ha convertido en delegado de clase")

    @staticmethod
    def puntuar_alumno(alumno: Alumno, nota: int):
        alumno.notas.append(nota)

class Aula:
    def __init__(self, nombre: str, capacidad: int, profesor: Profesor, *, alumnos: list[Alumno] = []):
        self.nombre = nombre
        self.capacidad = capacidad
        self.alumnos = alumnos
        self.profesor = profesor

    def alistar_alumno(self, alumno: Alumno) -> None:
        if len(self.alumnos) < self.capacidad:
            self.alumnos.append(alumno)
        else:
            raise ValueError("Esta clase está completa y no se pueden alistar más alumnos")
        
def gestionar_alumnos(aula: Aula, lista_alumnos: list[Alumno]) -> int:
    bucle_crear_alumnos = True
    while bucle_crear_alumnos:
        eleccion = input("¿Quieres crear un alumno? (s/n): ")
        if eleccion.lower() in ("no", "n"):
            bucle_crear_alumnos = False
        else:
            alumno = crear_alumno()
            lista_alumnos.append(alumno)
    print(f"Se van a añadir {len(lista_alumnos)} alumnos al aula {aula.nombre}")
    print(f"A esa aula le queda una capacidad de {aula.capacidad - len(aula.alumnos)}")
    alumnos_alistados = 0
    try:
        for alumno in lista_alumnos:
            aula.alistar_alumno(alumno)
            alumnos_alistados += 1
    except ValueError:
        print("Se ha llegado al límite de alumnos para esta aula")
    print(f"Se han alistado {alumnos_alistados} alumnos")
    return alumnos_alistados

def crear_alumno() -> Alumno:  # Esto es una fábrica
    nombre = input("Dime el nombre del alumno: ")
    edad = int(input("Dime la edad del alumno: "))
    return Alumno(nombre, edad)

# Ejemplo de uso
profesor = Profesor("Sr. García", 45, 3000.0, "Matemáticas")
aula = Aula("Aula 202", 30, profesor)

lista_alumnos = []
gestionar_alumnos(aula, lista_alumnos)

# Asignar delegado basado en las mejores notas
profesor.asignar_delegado_de_clase(aula)

print(f"Aula: {aula.nombre}")
print(f"Profesor: {aula.profesor.nombre}, Asignatura: {aula.profesor.asignatura}")
print("Alumnos:")
for alumno in aula.alumnos:
    print(f" - {alumno.nombre}, Edad: {alumno.edad}, Delegado: {'Sí' if alumno.es_delegado else 'No'}")
