def generar_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]

# Ejemplo de uso
cantidad = 10
lista_fibonacci = generar_fibonacci(cantidad)
print("Números de Fibonacci:", lista_fibonacci)


# La funcion generar_fibonacci toma un numero "n" como argumento, que representa la cantidad de numeros de Fibonacci que deseas generar.
# Inicializa una lista fibonacci con los dos primeros numeros de la secuencia: 0 y 1.
# Utiliza un bucle for para generar los siguientes numeros de la secuencia sumando los dos ultimos numeros de la lista.
# Devuelve la lista de numeros de Fibonacci hasta la cantidad especificada.