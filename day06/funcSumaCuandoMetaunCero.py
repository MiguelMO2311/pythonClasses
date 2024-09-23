def suma_hasta_cero():
    suma = 0
    while True:
        numero = int(input("Introduce un número (0 para terminar): "))
        if numero == 0:
            break
        suma += numero
    return suma

# Llamada a la función y mostrar el resultado
resultado = suma_hasta_cero()
print("La suma de los números introducidos es:", resultado)

# Misma funcion pero con lambda

def suma_hasta_ceroB():
    return sum(iter(lambda: int(input("Introduce un número (0 para terminar): ")), 0))

# Llamada a la función y mostrar el resultado
resultado = suma_hasta_ceroB()
print("La suma de los números introducidos es:", resultado)
