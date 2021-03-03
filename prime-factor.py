from math import sqrt
from time import time

"""
The prime factorization sieve will create a sieve with all the 
prime factors up to n.

The number in the sieve indicates the smallest prime divisor
of the index number. If the prime divisor is zero, then the
provided index number is a prime number. *Note that this sieve
cannot be used to check if a number is prime, because the first
prime that is encountered has the prime number itself, and not
a 0*.

An example of the sieve for the first 100 numbers:

    [1, 1, 2, 3, 2, 5, 3, 7, 2, 3, 5, 0, 3, 0, 7, 5, 2, 0, 3, 0, 
    5, 7, 2, 0, 3, 5, 2, 3, 7, 0, 5, 0, 2, 3, 2, 7, 3, 0, 2, 3, 
    5, 0, 7, 0, 2, 5, 2, 0, 3, 7, 5, 3, 2, 0, 3, 5, 7, 3, 2, 0, 
    5, 0, 2, 7, 2, 5, 3, 0, 2, 3, 7, 0, 3, 0, 2, 5, 2, 7, 3, 0, 
    5, 3, 2, 0, 7, 5, 2, 3, 2, 0, 5, 7, 2, 3, 2, 5, 3, 0, 7, 3]

This method can be used to quickly find the prime factorization
of a composite number.

This method runs in 31 milliseconds with a sieve of n=10^6. The
initialization of the sieve takes the most time, so most efficient
usage is if multiple numbers have to be factorized.
"""
import math
import random

class PrimeFactorizationSieve():
    def __init__(self, n):
        # Every even index is divible by two, so we can
        # immediately initialize this to two.
        sieve = [2, math.inf] * ((n + 1) // 2 + 1)
        # The first two entries are not prime.
        sieve[0] = sieve[1] = 1
        # We only have to test up to sqrt(n) because of the identity
        # c = p1 * p2. If no prime p1 exists smaller than sqrt(n), then
        # a number p2 also doesn't exist, thus it is prime.
        limit = int(sqrt(n)) + 2
        # Here we iterate over every odd indexed entry in the sieve.
        for i in range(3, limit + 1, 2):
            # If the number has not yet been crossed out, we need to
            # cross out all the multiples of this number.
            if sieve[i] == math.inf:
                # Only iterate over the indices that are a multiple of
                # the number that we are crossing out.
                for j in range(i, n + 1, i):
                    # Set the number to the smallest prime divisor.
                    sieve[j] = min(sieve[j], i)

        self.sieve = sieve

    def factorize(self, x):
        factors = []
        # If x is still divisible
        while x > 1:
            # Fetch the smallest prime factor from the sieve
            factor = self.sieve[x]
            # If the factor is zero, then x is prime.
            if factor == math.inf:
                # Set the factor to x.
                factor = x
            # Append the factor to the result
            factors.append(factor)
            # Divide x by the factor to find the other factor
            x = x // factor
        # Return only the distinct set of factors of x.
        return set(factors)

class PrimeSieve():
    def __init__(self, n):
        print('sieve({})'.format(n))
        sieve = [False, True] * ((n + 1) // 2)
        sieve[0] = sieve[1] = False
        sieve[2] = True
        limit = int(sqrt(n)) + 1
        for i in range(3, limit + 1, 2):
            if sieve[i]:
                for j in range(2*i, n + 1, i):
                    print('{} cross out {}'.format(i, j))
                    sieve[j] = False
        print('sieve', sieve)
        self.sieve = sieve

    def isprime(self, x):
        return self.sieve[x]

    def iterator(self):
        for i in range(len(self.sieve)):
            if self.sieve[i]:
                yield i

"""
In this example we create a sieve where n = 1.000.000, and then use
it to factorize a large number.
"""
# start = time()
# pfs = PrimeFactorizationSieve(2767626)
# factors = pfs.factorize(2767626)
# end = time()
# print(factors, 'Runtime: {}'.format(end - start))

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if a == b:
        return a
    if b > a:
        a, b = b, a
    q = a // b
    r = a - b * q
    while r != 0:
        a = b
        b = r
        q = a // b
        r = a - b * q
    return b

def modpow(a, n, p):
    res = 1
    a = a % p
    while n > 0:
        # if n is odd
        if n & 1:
            res = (res * a) % p
        n = n >> 1  # n = n / 2
        a = (a*a) % p
    return res

def is_prime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    if not n & 1:
        return False
    while k > 0:
        a = random.randint(2, n-1)
        if gcd(n, a) != 1:
            return False
        if modpow(a, n-1, n) != 1:
            return False
        k -= 1
    return True

class PrimeFactorization():
    def __init__(self, n):
        limit = int(math.sqrt(n)) + 1
        self.sieve = PrimeSieve(limit)

    def factorize(self, x):
        factors = []
        for p in self.sieve.iterator():
            if x == 1:
                break
            if x % p == 0:
                factors.append(p)
                x = x // p
                if is_prime(x, 16):
                    factors.append(x)
                    break
        return factors




x = 45
primes = PrimeFactorization(x)
factors = primes.factorize(x)
print(factors)


print('sieve', primes.sieve.sieve)
print('sieve.primes', list(primes.sieve.iterator()))

print('is_prime(9): {}'.format(is_prime(9, 16)))