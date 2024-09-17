# Lista para guardar los números primos
numeros_primos = []

# Bucle externo para recorrer el rango de 1 a 10
for rango in range(1, 20):
    es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
    
    # Los números menores que 2 no son primos
    if rango < 2:
        es_primo = False
    else:
        for divisor in range(2, rango):
            if rango % divisor == 0:
                es_primo = False
                break
    
    # Guardar el número en la lista si es primo
    if es_primo:
        numeros_primos.append(rango)

# Imprimir los números primos
print("Números primos en el rango de 1 a 10:", numeros_primos)
