import eulerlib
import random
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

---------------

The largest n-digit pandigital is when n=9 and is 987654321.
Let p be the largest prime that is n-digit pandigital.

We know that

    p < 987654321

Let L be the largest n-digit pandigital, which is L = 987654321.

If we generate the permutations of L from high to low
and call this the set P.

Then the algorithm becomes simple:

Algorithm PandigitalPrime(n):

    1.  Let L be the largest n-digit pandigital.
    2.  Let P be the set of permutations from L from high to low.
    3.  for p in P
    4.      if p is prime
    5.          return p

Except that it requires a generator the returns the permutations of L
in reversed order. And it also needs a primality test for big primes.
"""


def modpow(a, n, p):
    """
    Use Fermat's little theorem to calculate a^n mod p, which
    can handle very large exponents. Calculates in O(log n) time.
    :param a: base
    :param n: exponent
    :param p: mod
    :return: (a^n) mod p
    """
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
    """
    Test if a number n is prime k-times.
    :param n: The prime number to be tested.
    :param k: The number of tests.
    :return:
    """
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    if eulerlib.is_even(n):
        return False
    while k > 0:

        # Take random int in [2, n-2]
        a = random.randint(2, n-1)

        # Check if a and n are co-prime.
        if eulerlib.gcd(n, a) != 1:
            return False

        # Fermat's little theorem
        if modpow(a, n-1, n) != 1:
            return False

        k -= 1

    return True


def first_index_with_bigger_neighbour(P):
    """
    Find the first index from the right whose element is larger
    than his neighbour.
    :param P:
    :return:
    """
    i = len(P) - 1
    while i > 0 and P[i-1] >= P[i]:
        i -= 1
    return i


def first_index_with_smaller_neighbour(P):
    """
    Find the first index from the right whose element is smaller
    than his neighbour.
    :param P:
    :return:
    """
    i = len(P) - 1
    while i > 0 and P[i-1] <= P[i]:
        i -= 1
    return i


def next_permutation(P):
    """
    For any given permutation P, give the next permutation.
    If there is no next permutation, P will be returned.
    :param P:
    :return:
    """
    n = len(P)

    # Find the first index with the bigger neighbour.
    i = first_index_with_bigger_neighbour(P)

    # If this is the first, where i=0, then there is no next permutation.
    if i == 0:
        return P

    # From the right, find a value in P that is smaller than
    # the previous found value.
    j = n - 1
    while P[j] <= P[i-1]:
        j -= 1

    # Swap the values
    P[i-1], P[j] = P[j], P[i-1]

    # Restore the tail of the permutation.
    j = n - 1
    while i < j:
        P[i], P[j] = P[j], P[i]
        i += 1
        j -= 1

    return P


def previous_permutation(P):
    """
    For any given permutation P, give the previous permutation.
    If there is no pervious permutation, P will be returned.
    :param P:
    :return:
    """
    n = len(P)

    # Find the first index with the bigger neighbour.
    i = first_index_with_smaller_neighbour(P)

    # If this is the first, where i=0, then there is no next permutation.
    if i == 0:
        return P

    # From the right, find a value in P that is bigger than
    # the previous found value.
    j = n - 1
    while P[j] >= P[i-1]:
        j -= 1

    # Swap the values
    P[i-1], P[j] = P[j], P[i-1]

    # Restore the tail of the permutation.
    j = n - 1
    while i < j:
        P[i], P[j] = P[j], P[i]
        i += 1
        j -= 1

    return P


"""
Soo, let's return to implement the following algorithm:

Algorithm LargestPandigitalPrime(n):

    1.  Let L be the largest n-digit pandigital.
    2.  Let P be the set of permutations from L from high to low.
    3.  for p in P
    4.      if p is prime
    5.          return p
    
"""

def largest_pandigital_prime(n):
    L = list(range(1, n + 1))[::-1]
    prev_L = None
    while L != prev_L:
        prev_L = list(L)
        if is_prime(eulerlib.digits_to_int(L), 10):
            return L
        L = previous_permutation(L)
    return None


"""
The solution is 

    max { LargestPandigitalPrime(n) | 1 <= n <= 9 }
    
which gives
"""


def search_pandigital_primes():
    P = []
    for n in range(1, 9 + 1):
        p = largest_pandigital_prime(n)
        if p is not None:
            P.append(eulerlib.digits_to_int(p))
            print('N={}  =>  PD({}) = {}'.format(n, n, eulerlib.digits_to_int(p)))
    return max(P)


eulerlib.time_it(search_pandigital_primes)
