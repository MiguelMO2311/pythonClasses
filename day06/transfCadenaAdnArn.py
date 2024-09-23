# Diccionario de traducción
traduccion = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}

# Función para convertir ADN a ARN
def adn_arn(adn):
    return ''.join(traduccion[base] for base in adn)

# Ejemplo de uso
cadena_adn = "ATCGTTAAC"
cadena_arn = adn_arn(cadena_adn)
print("La cadena de ARN es:", cadena_arn)
