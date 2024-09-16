# Solicitar al usuario que ingrese un número
numero = int(input("Introduce un número: "))

# Calcular si el número es par o impar
resultado = "par" if numero % 2 == 0 else "impar"

# Imprimir el resultado
print(f"El número {numero} es {resultado}.")
