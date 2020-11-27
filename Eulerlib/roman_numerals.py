table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
         'C': 100, 'D': 500, 'M': 1000}

rtable = sorted((v, k) for k, v in table.items())[::-1]


def decimal(numeral):
    result = 0
    n = len(numeral)
    skip = False
    for i in range(n):
        if skip:
            skip = False
            continue
        if i < n-1 and table[numeral[i]] < table[numeral[i+1]]:
            result += table[numeral[i+1]] - table[numeral[i]]
            skip = True
        else:
            result += table[numeral[i]]
    return result



def roman_numeral(decimal):
    result = ""
    i = 0
    while decimal > 0:
        if decimal > 10 and decimal >= rtable[i][0] - rtable[i+2][0] and decimal < rtable[i][0]:
            result += rtable[i+2][1] + rtable[i][1]
            decimal -= rtable[i+2][0] + rtable[i][0]
        elif decimal >= rtable[i][0]:
            result += rtable[i][1]
            decimal -= rtable[i][0]
        elif decimal >= rtable[i][0] - rtable[i+1][0] and decimal < rtable[i][0]:
            result += rtable[i+1][1] + rtable[i][1]
            decimal -= rtable[i+1][0] + rtable[i][0]

        print('{} | {}'.format(result.ljust(14, ' '), decimal))

        # if decimal > 10 and decimal >= rtable[i][0] - rtable[i+2][0] and decimal < rtable[i][0]:
        #     result += rtable[i+2][1] + rtable[i][1]
        #     decimal -= rtable[i][0] + rtable[i+2][0]
        # elif decimal > 5 and decimal >= rtable[i][0] - rtable[i+1][0] and decimal < rtable[i][0]:
        #     result += rtable[i+1][1] + rtable[i][1]
        #     decimal -= rtable[i][0] + rtable[i+1][0]
        # if decimal >= rtable[i][0]:
        #     result += rtable[i][1]
        #     decimal -= rtable[i][0]

        if not decimal >= rtable[i][0]:
            i += 1
    return result


def test(numeral):
    dec = decimal(numeral)
    result = roman_numeral(dec)
    return numeral, dec, result


print('{} = {} = {}'.format(*test('IIIIIIIIIIIIII')))
print('{} = {} = {}'.format(*test('MMMMCCCXIV')))
print('{} = {} = {}'.format(*test('MMDCCXXXXIIII')))  #XLIV