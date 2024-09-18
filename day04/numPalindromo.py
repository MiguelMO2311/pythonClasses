def es_palindromo(numero):
    return str(numero) == str(numero)[::-1]

# Ejemplo de uso
numero = 12321
resultado = es_palindromo(numero)
print(f"El número {numero} es palíndromo: {resultado}")

# opcion para que si es un numero palidromo me sume sus numeros

def es_palindromo_y_suma(numero):
    # Convertir el número a una cadena
    cadena = str(numero)
    # Verificar si es palíndromo
    if cadena == cadena[::-1]:
        # Calcular la suma de los dígitos
        suma = sum(int(digito) for digito in cadena)
        return f"El número {numero} es palíndromo y la suma de sus dígitos es {suma}."
    else:
        return f"El número {numero} no es Capicúa."

# Ejemplo de uso
def es_palindromo_y_suma(numero):
    # Convertir el número a una cadena
    cadena = str(numero)
    # Verificar si es palíndromo
    if cadena == cadena[::-1]:
        # Calcular la suma de los dígitos
        suma = sum(int(digito) for digito in cadena)
        return f"El número {numero} es palíndromo y la suma de sus dígitos es {suma}."
    else:
        return f"El número {numero} no es Capicúa."

# Ejemplo de uso
numero = 12321
resultado = es_palindromo_y_suma(numero)
print(resultado)
