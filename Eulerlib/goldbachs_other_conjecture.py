import eulerlib
import math

"""
Find the smallest composite odd number that cannot be written in the form of

    x = p + 2a^2

    where x is an odd composite number, x > 3
    and p is a prime
    and a >= 1.

Notice that we can rewrite this as
    
    x - 2a^2 = p
        
which means that we must find some a, for which x - 2a^2 is prime.

We can use a prime number sieve to check for primality and to generate
a list of odd composite numbers.

To factor the number into p + 2a^2:

Algorithm FactorGoldbach(c):

1.  for a in [1, sqrt(c/2) + 1]
2.      if c - 2*a^2 is prime
3.          return true
4.  return false

Now we can search for the first odd composite number that cannot
be factored by FactorGoldbach:

Algorithm FindContradiction(N):

1.  Let S be a prime number sieve up to N.
2.  Let C be the set of odd composite numbers.
3.  for i from 3 to N skip 2
4.       if i is prime
5.           continue
6.       if not FactorGoldbach(i, S)
7.           return i
    
"""

def factor_goldbach(c, sieve):
    """
    Gives an odd composite number c, rewrite the
    number in the form of   p + 2a^2   (a prime plus two times a square).

    Return False if this is not possible.
    :param p:
    :return:
    """
    for a in range(1, int(math.sqrt(c / 2)) + 1):
        if sieve[c - 2*a**2]:
            return c - 2*a**2, a
    return False, False


def find_contradiction():
    N = 10000
    primes = eulerlib.prime_sieve(N)
    # For all odd composite numbers
    for i in range(3, N, 2):
        if primes[i]:
            continue
        # Factor into a prime plus a square
        p, a = factor_goldbach(i, primes)
        # Not factorized?
        if not p:
            # Return solution
            return i
        print('{} = {} + 2^{}'.format(i, p, a))


eulerlib.time_it(find_contradiction)
