def añadir_contacto(agenda: dict[str, str]) -> None:
    """
    Añade un contacto a la agenda.
    
    Args:
        agenda (dict): Diccionario que contiene los contactos.
    """
    nombre: str = input("Introduce el nombre del contacto: ").lower()
    numero: str = input("Introduce el número del contacto: ")
    agenda[nombre] = numero
    print(f"Contacto {nombre} añadido con éxito.")

def eliminar_contacto(agenda: dict[str, str]) -> None:
    """
    Elimina un contacto de la agenda.
    
    Args:
        agenda (dict): Diccionario que contiene los contactos.
    """
    nombre: str = input("Introduce el nombre del contacto a eliminar: ").lower()
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado con éxito.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")

def actualizar_contacto(agenda: dict[str, str]) -> None:
    """
    Actualiza el número de un contacto existente en la agenda.
    
    Args:
        agenda (dict): Diccionario que contiene los contactos.
    """
    nombre: str = input("Introduce el nombre del contacto a actualizar: ").lower()
    if nombre in agenda:
        nuevo_numero: str = input("Introduce el nuevo número del contacto: ")
        agenda[nombre] = nuevo_numero
        print(f"Número del contacto {nombre} actualizado con éxito.")
    else:
        print(f"El contacto {nombre} no existe en la agenda.")

# Agenda principal
agenda: dict[str, str] = {}
while True:
    print("\nAgenda Telefónica")
    print("1. Añadir contacto")
    print("2. Eliminar contacto")
    print("3. Actualizar contacto")
    print("4. Salir")
    
    opcion: str = input("Selecciona una opción: ")
    
    if opcion == '1':
        añadir_contacto(agenda)
    elif opcion == '2':
        eliminar_contacto(agenda)
    elif opcion == '3':
        actualizar_contacto(agenda)
    elif opcion == '4':
        break
    else:
        print("Opción no válida.")

