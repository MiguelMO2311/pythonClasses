def encontrar_narcisistas() -> list:
    """
    Encuentra los primeros cuatro números narcisistas de tres cifras.

    Un número narcisista de tres cifras es aquel que es igual a la suma de los cubos de sus dígitos.

    Returns:
        list[int]: Una lista con los primeros cuatro números narcisistas de tres cifras.
    """
    narcisistas: list[int] = []
    for num in range(100, 1000):
        suma_cubos: int = sum(int(digito) ** 3 for digito in str(num))
        if num == suma_cubos:
            narcisistas.append(num)
            if len(narcisistas) == 4:
                break
    return narcisistas

# Ejemplo de uso
resultado: list[int] = encontrar_narcisistas()
print("Los primeros 4 números narcisistas de tres cifras son:", resultado)


# FUNCION LAMBDA CON EL MISMO RESULTADO

# Define una función lambda para verificar si un número es narcisista
es_narcisista = lambda num: num == sum(int(digito) ** 3 for digito in str(num))

# Define una función lambda para encontrar los primeros 4 números narcisistas de tres cifras
encontrar_narcisistas_lambda = lambda: [num for num in range(100, 1000) if es_narcisista(num)][:4]

# Ejemplo de uso
resultado_lambda: list[int] = encontrar_narcisistas_lambda()
print("Los primeros 4 números narcisistas de tres cifras son:", resultado_lambda)
