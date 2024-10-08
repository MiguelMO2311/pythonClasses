#primera forma
claves = [1, 2, 3, 4, 5]
valores = ["Juan", "Ana", "Raquel", "Antonio", "Belen"]

diccionario = dict(zip(claves, valores))
print(diccionario)

# segunda forma (elegante)

claves = [1, 2, 3, 4, 5]
valores = ["Juan", "Ana", "Raquel", "Antonio", "Belen"]

diccionario = {clave: valor for clave, valor in zip(claves, valores)}
print(diccionario)

# tercera forma (bucle)

claves = [1, 2, 3, 4, 5]
valores = ["Juan", "Ana", "Raquel", "Antonio", "Belen"]

diccionario = {}
for clave, valor in zip(claves, valores):
    diccionario[clave] = valor

print(diccionario)

# cuarta forma con enumerate
claves = [1, 2, 3, 4, 5]
valores = ["Juan", "Ana", "Raquel", "Antonio", "Belen"]

diccionario = {}
for indice, valor in enumerate(valores):
    diccionario[claves[indice]] = valor

print(diccionario)

# separa el dicionario clave/valor en dos listas con las claves por un lado y los valores por otro

diccionario = {1: 'Juan', 2: 'Ana', 3: 'Raquel', 4: 'Antonio', 5: 'Belen'}

# Lista de claves
claves = list(diccionario.keys())

# Lista de valores
valores = list(diccionario.values())

print("Claves:", claves)
print("Valores:", valores)


# llaves, valores = diccionario.items() Joaquin

diccionario = {"A":1,"B":2,"C":3,"D":4}

#1
numeros = list(diccionario.values())
letras = list(diccionario.keys())

#2
for clave in diccionario:
    letras.append(clave)
    numeros.append(diccionario[clave])

#3
for clave,valor in diccionario.items():
    letras.append(clave)
    numeros.append(valor)