def generar_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]

# Ejemplo de uso
cantidad = 10
lista_fibonacci = generar_fibonacci(cantidad)
print("Números de Fibonacci:", lista_fibonacci)


# La función generar_fibonacci toma un número n como argumento, que representa la cantidad de números de Fibonacci que deseas generar.
# Inicializa una lista fibonacci con los dos primeros números de la secuencia: 0 y 1.
# Utiliza un bucle for para generar los siguientes números de la secuencia sumando los dos últimos números de la lista.
# Devuelve la lista de números de Fibonacci hasta la cantidad especificada.