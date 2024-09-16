# Diccionario que representa a una persona
persona = {
    "nombre": "Juan",
    "edad": 0,
    "ciudad": "Madrid"
}

# Validar si es mayor de edad usando un operador ternario
es_mayor_de_edad = "Mayor de edad" if persona["edad"] >= 18 else "Menor de edad"

print(f"{persona['nombre']} es {es_mayor_de_edad}.")
