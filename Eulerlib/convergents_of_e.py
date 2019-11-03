"""

    Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

"""
from fractions import ContinuedFraction
import math
from eulerlib import digits, time_it


def convergents_of_e():
    an = [2]
    for k in range(1, 34):
        an += [1, 2 * k, 1]
    cf = ContinuedFraction(an)
    return sum(digits(cf.pn(99)))


time_it(convergents_of_e)
