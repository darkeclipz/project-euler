# Rules:
#
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
#
# Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
# I can only be placed before V and X.
# X can only be placed before L and C.
# C can only be placed before D and M.

lookup = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}

inv_lookup = {v:k for k,v in lookup.items()}

class RomanNumeral:

    def __init__(self, x):
        self.value = self.decode(x)

    def decode(self, x):
        x = x.strip()
        value = 0
        i = 0
        while i < len(x):
            if x[i:i+2] in lookup:
                value += lookup[x[i:i+2]]
                i += 2
            elif x[i] in lookup:
                value += lookup[x[i]]
                i += 1
        return value

    def encode(self, x):
        rn = ""
        values = [k for k,v in inv_lookup.items()]
        values.sort(reverse = True)
        while x > 0:
            for i in values:
                if i <= x:
                    x -= i
                    rn += inv_lookup[i]
                    break
        return rn

    def __repr__(self):
        return self.encode(self.value)


# print(RomanNumeral('IIIIIIIIIIIIIIII'))
# print(RomanNumeral('VIIIIIIIIIII'))
# print(RomanNumeral('VVIIIIII'))
# print(RomanNumeral('XIIIIII'))
# print(RomanNumeral('VVVI'))
# print(RomanNumeral('XVI'))


solution = 0

with open('roman_numerals.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        current_size = len(line)
        rn = RomanNumeral(line)
        optimal_size = len(str(rn))
        solution += (current_size - optimal_size)
        print("Reduced {} to {} saving {} characters.".format(line, str(rn), current_size - optimal_size))
    
print(solution)
        