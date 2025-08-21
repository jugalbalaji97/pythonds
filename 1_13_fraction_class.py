class Fraction:

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other_frac):
        numerator = self.numerator * other_frac.denominator + self.denominator * other_frac.numerator
        denominator = self.denominator * other_frac.denominator
        gcd = self._gcd(numerator, denominator)
        return Fraction(numerator // gcd, denominator // gcd)
    
    def __sub__(self, other_frac):
        numerator = self.numerator * other_frac.denominator - self.denominator * other_frac.numerator
        denominator = self.denominator * other_frac.denominator
        gcd = self._gcd(numerator, denominator)
        return Fraction(numerator // gcd, denominator // gcd)
    
    def __mul__(self, other_frac):
        numerator = self.numerator * other_frac.numerator
        denominator = self.denominator * other_frac.denominator
        gcd = self._gcd(numerator, denominator)
        return Fraction(numerator // gcd, denominator // gcd)
    
    def __truediv__(self, other_frac):
        numerator = self.numerator * other_frac.denominator
        denominator = self.denominator * other_frac.numerator
        gcd = self._gcd(numerator, denominator)
        return Fraction(numerator // gcd, denominator // gcd)

    def __eq__(self, other_frac):
        return self.numerator * other_frac.denominator == self.denominator * other_frac.numerator
    
    def __ne__(self, other_frac):
        return self.numerator * other_frac.denominator != self.denominator * other_frac.numerator
    
    def __lt__(self, other_frac):
        return self.numerator * other_frac.denominator < self.denominator * other_frac.numerator

    def __le__(self, other_frac):
        return self.numerator * other_frac.denominator <= self.denominator * other_frac.numerator

    def __gt__(self, other_frac):
        return self.numerator * other_frac.denominator > self.denominator * other_frac.numerator

    def __ge__(self, other_frac):
        return self.numerator * other_frac.denominator >= self.denominator * other_frac.numerator
    
    def _gcd(self, m, n):
        while m % n != 0:
            m, n = n, m % n
        return n
    
def main():
    frac1 = Fraction(1, 2)
    print('Frac1:', frac1)
    frac2 = Fraction(1, 4)
    print('Frac2:', frac2)
    print('Sum:', frac1 + frac2)
    print('Subtraction:', frac1 - frac2)
    print('Product:', frac1 * frac2)
    print('Division:', frac2 / frac1)
    frac3 = Fraction(2, 4)
    print('Frac3:', frac3)
    print('Frac1 equals Frac2:', frac1 == frac2)
    print('Frac1 equals Frac3:', frac1 == frac3)
    print('Frac1 less than Frac2:', frac1 < frac2)
    print('Frac1 greater than Frac2:', frac1 > frac2)
    print('Frac1 less than or equal to Frac3:', frac1 >= frac3)
    print('Frac1 greater than or equal to Frac3:', frac1 >= frac3)

if __name__ == "__main__":
    main()