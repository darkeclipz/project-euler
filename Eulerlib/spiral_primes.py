import eulerlib as pe
import random


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


def is_even(n):
    return not n & 1


def is_prime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    if is_even(n):
        return False
    while k > 0:

        # Take random int in [2, n-2]
        a = random.randint(2, n-1)

        # Check if a and n are co-prime.
        if gcd(n, a) != 1:
            return False

        # Fermat's little theorem
        if modpow(a, n-1, n) != 1:
            return False

        k -= 1

    return True


def sp():
    k = 1
    primes = 0
    while(True):
        p = 4*k*k + 4*k + 1 
        for j in range(4):
            q = p - 2*j*k
            if is_prime(q, 20):
                primes += 1
        rat = primes / (4*k + 1)
        if rat <= 0.1:
            return 2*k + 1
        k += 1


pe.time_it(lambda: sp())
# Solution is 26241
# Executed in 6.178759 seconds