class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def simplify(self):
        gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
        gcd_value = gcd(self.numerator, self.denominator)
        self.numerator //= gcd_value
        self.denominator //= gcd_value

# Ejemplo de uso
fraction1 = Fraction(4, 5)
fraction2 = Fraction(1, 8)
resultado = fraction1.add(fraction2)
print(resultado)  # Salida: 37/40
