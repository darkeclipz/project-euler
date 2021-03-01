"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is 
a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

import eulerlib as euler
import math

def powerful_digit_counts():
    count = 0
    for n in range(1, 100):
        lower = 10**(n - 1)
        upper = 10**n
        for k in range(1, 10):
            if lower <= k**n < upper:
                print('{}^{}={}'.format(k, n, k**n))
                count += 1
    return count

euler.time_it(powerful_digit_counts)

