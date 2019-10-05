from eulerlib import *


def substring_divisibility():
    primes = [2, 3, 5, 7, 11, 13, 17]
    pandigitals = []
    for d in permutations(list(range(10))):
        has_property = True
        for i in range(7):
            substring = digits_to_int([d[i + 1],  d[i + 2],  d[i + 3]])
            if substring % primes[i] != 0:
                has_property = False
                break
        if has_property:
            pandigitals.append(digits_to_int(d))
            print('{} ⟶ {}'.format(d, pandigitals[-1]))

    return sum(pandigitals)


def substring_divisibility2():
    div_17 = [17 * x for x in range(100 // 17 + 1, 1000 // 17 + 1)]
    set_of_9 = set(range(10))
    primes = [2, 3, 5, 7, 11, 13]

    for d17 in div_17:
        i = 6
        while i > 0:
            digs = digits(d17)
            is_divisible = True
            for d in set_of_9 - set(digs):
                if digits_to_int([d] + digs[:2]) % primes[i]:
                    d17.append(d)
                    d17 = shift(d17, -1)
                    i -= 1
                    break



    return div_17


time_it(substring_divisibility2)
#time_it(substring_divisibility)
#time_it(lambda: len(list(permutations(list(range(10))))))
