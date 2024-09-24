# Diccionario de traducción de ADN a ARN
traduccion = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "C"
}

def adn_a_arn(hebra: str) -> str:
    """
    Convierte una hebra de ADN en su correspondiente hebra de ARN.

    Args:
        hebra (str): Una cadena de caracteres que representa la hebra de ADN.

    Returns:
        str: La hebra de ARN resultante de la traducción.
    """
    resultado: str = ""
    for par in hebra:
        resultado += traduccion[par]
    return resultado

# Ejemplo de uso
hebra: str = "ATAGATCATAGGCATAACCA"
arn: str = adn_a_arn(hebra)
print(hebra)
print(arn)


# Hecho con lambda
''' trad = lambda base_nitrogenada: traduccion[base_nitrogenada]
resultado = ""
for par in hebra:
    resultado += trad(par)
print(resultado)
'''