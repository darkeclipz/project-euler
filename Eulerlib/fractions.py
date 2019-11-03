import eulerlib


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        if isinstance(other, Fraction):
            c = eulerlib.lcm(self.den, other.den)
            a = c * self
            b = c * other
            return Fraction(a.num + b.num, a.den).simplify()
        elif isinstance(other, int):
            return Fraction(other, 1) + self
        elif isinstance(other, float):
            raise Exception("Can't add float to fraction.")
        else:
            raise Exception("Addition operator not defined.")

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.den * other.den).simplify()
        if isinstance(other, (int, float)):
            return Fraction(self.num * other, self.den * other).simplify()
        else:
            raise Exception("Multiplication operator not defined.")

    def __rmul__(self, other):
        return self * other

    def simplify(self):
        c = eulerlib.gcd(self.num, self.den)
        return Fraction(self.num // c, self.den // c)

    def __repr__(self):
        return '{}/{}'.format(self.num, self.den)

    def value(self):
        return self.num / self.den


class ContinuedFraction:

    def __init__(self, an):
        if isinstance(an, float):
            self.an = self.float_to_continued_fraction(an)
        elif isinstance(an, int):
            self.an = self.int_to_continued_fraction(an)
        elif isinstance(an, Fraction):
            self.an = self.fraction_to_continued_fraction(an)
        elif isinstance(an, list):
            self.an = an
        else:
            raise Exception('Cannot parse input to continued fraction.')

    def float_to_continued_fraction(self, x, max_convergents=16):
        a = x // 1
        r = x - a
        an = [int(a)]
        while r != 0 and len(an) < max_convergents:
            a = 1 / r // 1
            r = 1 / r - a
            an.append(int(a))
        return an

    def int_to_continued_fraction(self, x):
        return [x]

    def fraction_to_continued_fraction(self, x, max_convergents=16):
        x = x.simplify()  # assume gcd(a, b) = 1
        a = x.num
        b = x.den
        an = []
        while b != 0 and len(an) < max_convergents:
            p = a // b
            an.append(p)
            r = a - p * b
            a, b = b, r
        return an

    def pn(self, n):
        n += 1
        P = [0, 1, self.an[0]]
        for i in range(1, n):
            P.append(self.an[i] * P[-1] + P[-2])
        return P[-1]

    def qn(self, n):
        n += 1
        Q = [1, 0, 1]
        for i in range(1, n):
            Q.append(self.an[i] * Q[-1] + Q[-2])
        return Q[-1]

    def convergents(self):
        P = [0, 1, self.an[0]]
        Q = [1, 0, 1]
        C = [self.an[0]]
        for i in range(1, len(self.an)):
            P.append(self.an[i] * P[-1] + P[-2])
            Q.append(self.an[i] * Q[-1] + Q[-2])
            C.append(Fraction(P[-1], Q[-1]))
        return C

    def value(self):
        return self.convergents()[-1].value()

    def __repr__(self):
        return str(self.an)

