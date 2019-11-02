import eulerlib
import math


def prime_factorization(x, sieve=None):
    """
    Factorize a number into the prime factorization.
    Requires a sieve to be quick, if sieve is not specified
    it will generate one itself.
    :param x:
    :param sieve:
    :return:
    """
    if x == 0:
        return []
    if x in [1, 2]:
        return [x]
    if sieve is None:
        sieve = eulerlib.prime_sieve(x)
    factors = []
    if sieve[x]:
        return [x]
    for i in range(2, int(math.sqrt(x) + 1)):
        if sieve[x]:
            break
        if not sieve[i]:
            continue
        if x % i == 0:
            factors.append(i)
            x //= i
    factors += prime_factorization(x, sieve)
    return factors


def distinct_prime_factors_2(S):
    f1, f2 = [], []
    for i in range(2, 100, 1):
        f1 = f2
        f2 = prime_factorization(i + 1, S)
        if len(set(f1)) == 2 and len(set(f2)) == 2:
            print('f({}) = {}'.format(i, f1))
            print('f({}) = {}'.format(i + 1, f2))
            break


def distinct_prime_factors_3(S):
    f1, f2, f3 = [], [], []
    for i in range(3, 1000, 1):
        f1 = f2
        f2 = f3
        f3 = prime_factorization(i + 2, S)
        if len(set(f1)) == 3 and len(set(f2)) == 3 and len(set(f3)) == 3:
            print('f({}) = {}'.format(i, f1))
            print('f({}) = {}'.format(i + 1, f2))
            print('f({}) = {}'.format(i + 2, f3))
            break


def distinct_prime_factors_4(S):
    f1, f2, f3, f4 = [], [], [], []
    for i in range(4, 1000000, 1):
        f1 = f2
        f2 = f3
        f3 = f4
        f4 = prime_factorization(i + 3, S)
        if len(set(f1)) == 4 and len(set(f2)) == 4 and len(set(f3)) == 4 and len(set(f4)) == 4:
            print('f({}) = {}'.format(i, f1))
            print('f({}) = {}'.format(i + 1, f2))
            print('f({}) = {}'.format(i + 2, f3))
            print('f({}) = {}'.format(i + 3, f4))
            break


N = 200000
S = eulerlib.prime_sieve(N)
eulerlib.time_it(distinct_prime_factors_2, [S])
eulerlib.time_it(distinct_prime_factors_3, [S])
eulerlib.time_it(distinct_prime_factors_4, [S])
