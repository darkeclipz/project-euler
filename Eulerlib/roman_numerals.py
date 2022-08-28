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



class RomanNumeral:

    char_lookup = {
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

    inv_char_lookup = {v:k for k,v in char_lookup.items()}
    roman_numeral_chars = list(inv_char_lookup.keys())
    roman_numeral_chars.sort(reverse = True)

    def __init__(self, roman_numeral):
        self.value = self.decode(roman_numeral)

    def decode(self, roman_numeral):
        roman_numeral = roman_numeral.strip()
        value = 0
        i = 0
        while i < len(roman_numeral):
            if roman_numeral[i:i+2] in RomanNumeral.char_lookup:
                value += RomanNumeral.char_lookup[roman_numeral[i:i+2]]
                i += 2
            elif roman_numeral[i] in RomanNumeral.char_lookup:
                value += RomanNumeral.char_lookup[roman_numeral[i]]
                i += 1
        return value

    def encode(self, decimal_number):
        roman_numeral = ""
        while decimal_number > 0:
            for char in RomanNumeral.roman_numeral_chars:
                if char <= decimal_number:
                    decimal_number -= char
                    roman_numeral += RomanNumeral.inv_char_lookup[char]
                    break
        return roman_numeral

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
