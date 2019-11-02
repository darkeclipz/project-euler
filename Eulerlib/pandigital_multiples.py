import eulerlib as el


def pandigital_multiples():
    pandigitals = []

    for i in range(1, 10000):
        digits = el.digits(i)
        j = 2
        while len(digits) < 9:
            digits += el.digits(i * j)
            j += 1
        if len(digits) == 9 and el.is_pandigital_to_n(digits, 9):
            print('Pandigital: {}'.format(digits))
            pandigitals.append(el.digits_to_int(digits))

    return max(pandigitals)


el.time_it(pandigital_multiples)
