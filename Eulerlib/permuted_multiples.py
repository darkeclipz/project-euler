import eulerlib
import math
"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

----------------


for x in Z:



"""


def equal_sets(S):
    """
    Returns true if all the sets s in S are equal
    to each other.
    :param S:
    :return:
    """
    s0 = S[0]
    res = True
    for i in range(1, len(S)):
        res = res and s0 == S[i]
    return res


def permuted_multiples():
    x = 1
    while True:
        L = [x, 2 * x, 3 * x, 4 * x, 5 * x, 6 * x]
        if equal_sets(list(map(set, map(eulerlib.digits, L)))):
            return x
        x += 1


# eulerlib.time_it(permuted_multiples)




print(union_sets([set([1,2]), set([3,4]), set([4,5])]))
print(intersect_sets([set([1,2]), set([1,3,4]), set([1,4,5])]))
