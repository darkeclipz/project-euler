import math
import eulerlib

"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

------------------------------------------------------

Notice that

    d1-d9     : 9 digits * 1 = 9
    d10-d99   : 90 digits * 2 = 180
    d100-d999 : 900 digits  * 3 = 2700

Or in general

    i = 0
    The range (10**i, 10**(i+1) - 1) has 9 * 10**i numbers of (i+1) digits. 
    
Let CR(i) be the number of digits that is in a range (10**i, 10**(i+1) - 1). So CR(0) is the range
of (1, 9) which contains 9 numbers of 1 digit, so a total of 9 digits.

For CR(1) we get the range of (10, 99) which contains 90 numbers of 2 digits, so a total of 180 digits.

Let CCR(k) be the cumulative sum of all i = 0, 1, ..., k for CR(i).

The algorithm CD(d) gives the digit at position d in Champernownes constant.

-----

Example: Let's work through the example for CD(1050).

If we look at the ranges

    d1-d9     : 9 digits * 1 = 9
    d10-d99   : 90 digits * 2 = 180
    d100-d999 : 900 digits  * 3 = 2700
    
we can see that 1050 falls between (10, 99) and (100, 999), this means that the digit
is in the range of (100, 999). This means that (the number of digits) k=3.

Now let's subtract all the digits we already had in the previous ranges, so we
know which n-th digit it is in the (100, 999) range.

    1050 - CCR(3 - 1) = 1050 - 189 = 861

the numbers have three digits in this range, so we divide by that
 
    861 / 3 = 287
    
we also need to add the amount of numbers we had so far, which is 

    10 ** (k - 1) - 1   
    
or in this case   

    10**(2) - 1 = 99

This means that we are looking at number 287 + 99 = 386.
Now we need to determine which digit it is of 386.

Let r = 386, then r_ceil is also 386.
The difference between them gives us the fractional index.
Let diff = r_ceil - r

The value (1 - diff) is the 1-based index for the sub-digit in r_ceil, to 
To get this index 0-based, we subtract 1/k, which results in:

    (1 - diff - 1/k)
    
To get the integer index, multiply this by k digits, which is:

    (1 - diff - 1/k) * k

So the algorithm for CD(x) is:

    1.  Let k be the highest possible integer such that x < CCR(k).
    2.  Let r = (x - CCR(k-1)) / k + 10**(k-1) - 1.
    3.  Let r_ceil = ceil{r}.
    4.  Let diff = r_ceil - r
    5.  Let sub_index = (1 - diff - 1/k) * k
    6.  Return str(r_ceil)[sub_index]

"""

def product(numbers):
    """
    Returns the product of a list of numbers.
    :param numbers:
    :return:
    """
    p = 1
    for x in numbers:
        p *= x
    return p


def ccr(x):
    return sum([9 * 10**i * (i+1) for i in range(x)])


def champernownes_digit(d):
    k = 0
    while ccr(k) < d:
        k += 1
    lower = ccr(k - 1)
    index = (d - lower) / k
    res = index + 10 ** (k - 1) - 1
    res_ceil = math.ceil(res)
    diff = res_ceil - res
    sub = int((1 - diff - 1/k) * k)
    return str(res_ceil)[sub]


eulerlib.time_it(lambda: product(map(int, [champernownes_digit(10**i) for i in range(7)])))
eulerlib.time_it(lambda: champernownes_digit(10**100))  # the googelth digit.