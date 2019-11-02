import eulerlib
import math
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
    
    (i)  each of the three terms are prime, and, 
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting 
this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

-------

There are three primes p1, p2, and p3 in the order p1 < p2 < p3.
Notice that the difference 

    p2 - p1 = d,     (1)
    p3 - p2 = d      (2)
    
So 
    p2 = p3 - d

Substituting into (2) gives
    
    p3 - d - p1 = d
    p3 - p1     = 2d       (3)
    
Let S be a sieve up to N = 10000
Let P denote the set of primes between 1000 < p <= 9999 from S

for p1 in P
    d = 1
    while p1 + 2 * d < N 
        let p2 = p1 + d
        let p3 = p1 + 2*d
        if p1, p2, p3 are all prime 
         and p1, p2, p3 are permutations of each other
            return p1, p2, p3, d
        
"""


def is_permutation(A, B):
    """
    Returns true if A and B are permutations of each other.
    :param A:
    :param B:
    :return:
    """
    return set(A) == set(B)

def is_permutation3(A, B, C):
    """
    Returns true if A, B and C are permutations of each other.
    :param A:
    :param B:
    :param C:
    :return:
    """
    return set(A) == set(B) == set(C)

def prime_permutations():
    N = 10000
    S = eulerlib.prime_sieve(N)
    P = [p for p in eulerlib.sieve_to_list(S) if 1000 < p < 9999]

    print('p1   p2   p3   d')
    print('------------------------')
    for p1 in P:
        d = 1
        while p1 + 2 * d < N:
            p2 = p1 + d
            p3 = p2 + d
            if S[p1] and S[p2] and S[p3] and is_permutation3(eulerlib.digits(p1), eulerlib.digits(p2), eulerlib.digits(p3)):
                print(p1, p2, p3, d)
                break
            d += 1

eulerlib.time_it(prime_permutations)
