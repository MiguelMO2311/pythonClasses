class Alumno:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Notas: {self.notas}"

# Crear una lista para almacenar los alumnos
base_de_datos = []

# Añadir alumnos a la base de datos
base_de_datos.append(Alumno("Juan", 20, [85, 90, 78]))
base_de_datos.append(Alumno("María", 22, [92, 88, 95]))
base_de_datos.append(Alumno("Carlos", 21, [75, 80, 82]))

# Mostrar la base de datos
for alumno in base_de_datos:
    print(alumno)
