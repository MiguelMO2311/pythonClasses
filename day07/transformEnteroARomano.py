def int_to_roman(numero: int) -> str:
    """
    Convierte un número entero en su equivalente en números romanos.

    Args:
        numero (int): El número entero a convertir.

    Returns:
        str: El número en formato romano.
    """
    valores_romanos = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV",
        1: "I"
    }
    numero_romano: str = ''
    for valor, simbolo in valores_romanos.items():
        while numero >= valor:
            numero_romano += simbolo
            numero -= valor
    return numero_romano

# Ejemplo de uso
numero: int = int(input("Introduce un número: "))
print(f"El número {numero} en números romanos es: {int_to_roman(numero)}")
