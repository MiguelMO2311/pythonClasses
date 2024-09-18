class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

# Base de datos de usuarios
base_de_datos = []

# Funcion para validar la contraseña
def validar_contrasena(contrasena):
    if (len(contrasena) >= 12 and
        any(c.islower() for c in contrasena) and
        any(c.isupper() for c in contrasena) and
        any(c.isdigit() for c in contrasena)):
        return True
    return False

# Funcion para añadir un nuevo usuario
def anadir_usuario():
    nombre = input("Introduce el nombre de usuario: ")
    contrasena = input("Introduce la contraseña: ")
    if validar_contrasena(contrasena):
        nuevo_usuario = Usuario(nombre, contrasena)
        base_de_datos.append(nuevo_usuario)
        print("Usuario añadido correctamente.")
    else:
        print("Contraseña errónea. Debe tener al menos 12 caracteres, una mayúscula, una minúscula y un número.")


anadir_usuario()

# Clase Usuario: Define la estructura de los datos del usuario.
# Base de datos: Utiliza una lista para almacenar los usuarios.
# Funcion validar_contrasena: Verifica que la contraseña cumpla con los requisitos.
# Funcion anadir_usuario: Pide al usuario que introduzca un nombre y una contraseña, valida la contraseña y añade el usuario a la base de datos si la contraseña es valida.
# Al ejecutar anadir_usuario(), se pedirá al usuario que introduzca un nombre
#  y una contraseña. Si la contraseña cumple con los requisitos, se añadira el usuario a la base de datos;
#  de lo contrario, se mostrara un mensaje de error.