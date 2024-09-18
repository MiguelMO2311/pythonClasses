def primera_y_ultima_iguales(cadena):
    # Verifica que la cadena no esté vacía
    if len(cadena) == 0:
        return False
    # Compara la primera y la última letra
    return cadena[0].lower() == cadena[-1].lower()

# Ejemplo de uso
cadena = "Anaconda"
resultado = primera_y_ultima_iguales(cadena)
print(f"La primera y última letra de '{cadena}' son iguales: {resultado}")


# otra opcion 
def primera_y_ultima_iguales(cadena):
    return cadena[0].lower() == cadena[-1].lower() if cadena else False

# Ejemplo de uso
cadena = "Anaconda"
resultado = primera_y_ultima_iguales(cadena)
print(f"La primera y última letra de '{cadena}' son iguales: {resultado}")
