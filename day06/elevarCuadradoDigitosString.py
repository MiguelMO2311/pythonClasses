from typing import List

def elevar_cuadrado(cadena: str) -> List[int]:
    resultado = []
    for caracter in cadena:
        if caracter.isdigit():
            resultado.append(int(caracter) ** 2)
    return resultado

# Ejemplo de uso
cadena_entrada = "jba 2 4nlnlms11mlkms9"
resultado = elevar_cuadrado(cadena_entrada)
print("Resultado:", resultado)


# igual pero con funcion lambda

from typing import List

elevar_cuadrado = lambda cadena: [int(digito) ** 2 for digito in cadena if digito.isdigit()]

# Ejemplo de uso
cadena_entrada = "jba 2 4nlnlms11mlkms9"
resultado = elevar_cuadrado(cadena_entrada)
print("Resultado:", resultado)
