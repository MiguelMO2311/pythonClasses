def guardar_primos(limite):
    primos = []
    for num in range(2, limite + 1):
        if all(num % i != 0 for i in range(2, num)):
            primos.append(num)
    return primos

# Ejemplo de uso
limite = 20
lista_primos = guardar_primos(limite)
print("Números primos hasta", limite, ":", lista_primos)


# La función guardar_primos recorre los números desde 2 hasta el límite especificado.
# Utiliza una comprensión de lista con all para verificar si el número es primo.
# Si el número es primo, se añade a la lista de primos.