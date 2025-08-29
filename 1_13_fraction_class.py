class Fraction:

    def __init__(self, numerator: int, denominator: int):
        if not (isinstance(numerator, int) and isinstance(denominator, int)):
            raise TypeError("Both numerator and denominator should be integer datatype.")
        if denominator < 0:
            denominator = -denominator
            numerator = -numerator
        
        gcd = self._gcd(numerator, denominator)

        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return f"Fraction(numerator={self.numerator}, denominator={self.denominator})"
    
    def __add__(self, other_frac):
        numerator = self.numerator * other_frac.denominator + self.denominator * other_frac.numerator
        denominator = self.denominator * other_frac.denominator
        # gcd = self._gcd(numerator, denominator)
        # return Fraction(numerator // gcd, denominator // gcd)
        return Fraction(numerator, denominator)
    
    def __radd__(self, other_frac):
        return self.__add__(other_frac)
    
    def __iadd__(self, other_frac):
        numerator = self.numerator * other_frac.denominator + self.denominator * other_frac.numerator
        denominator = self.denominator * other_frac.denominator
        gcd = self._gcd(numerator, denominator)

        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

        return self

    def __sub__(self, other_frac):
        numerator = self.numerator * other_frac.denominator - self.denominator * other_frac.numerator
        denominator = self.denominator * other_frac.denominator
        # gcd = self._gcd(numerator, denominator)
        # return Fraction(numerator // gcd, denominator // gcd)
        return Fraction(numerator, denominator)
    
    def __mul__(self, other_frac):
        numerator = self.numerator * other_frac.numerator
        denominator = self.denominator * other_frac.denominator
        # gcd = self._gcd(numerator, denominator)
        # return Fraction(numerator // gcd, denominator // gcd)
        return Fraction(numerator, denominator)
    
    def __truediv__(self, other_frac):
        numerator = self.numerator * other_frac.denominator
        denominator = self.denominator * other_frac.numerator
        # gcd = self._gcd(numerator, denominator)
        # return Fraction(numerator // gcd, denominator // gcd)
        return Fraction(numerator, denominator)

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

    def get_num(self):
        return self.numerator
    
    def get_den(self):
        return self.denominator
    
def main():
    frac1 = Fraction(1, 2)
    print('Frac1:', frac1)
    print('Represetation of Frac1:', repr(frac1))
    print('Numerator of Frac1:', frac1.get_num())
    print('Numerator of Frac2:', frac1.get_den())
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
    # frac4 = Fraction(1.0, 2)
    frac5 = Fraction(1, -2)
    frac6 = Fraction(-1, 4)
    print('Frac5 greater than Frac6:', frac5 > frac6)
    print('Adding integer to fraction:', frac1 + 1)
    print('Adding fraction to integer:', 1 + frac1)
    frac1 += 1
    print("Frac1 incremented by integer:", frac1)
    int_num = 1
    int_num += frac1
    print("Incrementing integer with Frac1:", int_num)

if __name__ == "__main__":
    main()