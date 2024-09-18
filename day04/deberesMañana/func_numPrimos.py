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


# La funcion guardar_primos recorre los numeros desde 2 hasta el limite especificado.
# Utiliza una comprension de lista con "all" para verificar si el numero es primo.
# Si el numero es primo, se añade a la lista de primos.
