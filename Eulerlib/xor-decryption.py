from math import inf

ciphertext = [36,22,80,0,0,4,23,25,19,17,88,4,4,19,21,11,88,22,23,23,29,69,12,24,0,88,25,11,12,2,10,28,5,6,12,25,10,22,80,10,30,80,10,22,21,69,23,22,69,61,5,9,29,2,66,11,80,8,23,3,17,88,19,0,20,21,7,10,17,17,29,20,69,8,17,21,29,2,22,84,80,71,60,21,69,11,5,8,21,25,22,88,3,0,10,25,0,10,5,8,88,2,0,27,25,21,10,31,6,25,2,16,21,82,69,35,63,11,88,4,13,29,80,22,13,29,22,88,31,3,88,3,0,10,25,0,11,80,10,30,80,23,29,19,12,8,2,10,27,17,9,11,45,95,88,57,69,16,17,19,29,80,23,29,19,0,22,4,9,1,80,3,23,5,11,28,92,69,9,5,12,12,21,69,13,30,0,0,0,0,27,4,0,28,28,28,84,80,4,22,80,0,20,21,2,25,30,17,88,21,29,8,2,0,11,3,12,23,30,69,30,31,23,88,4,13,29,80,0,22,4,12,10,21,69,11,5,8,88,31,3,88,4,13,17,3,69,11,21,23,17,21,22,88,65,69,83,80,84,87,68,69,83,80,84,87,73,69,83,80,84,87,65,83,88,91,69,29,4,6,86,92,69,15,24,12,27,24,69,28,21,21,29,30,1,11,80,10,22,80,17,16,21,69,9,5,4,28,2,4,12,5,23,29,80,10,30,80,17,16,21,69,27,25,23,27,28,0,84,80,22,23,80,17,16,17,17,88,25,3,88,4,13,29,80,17,10,5,0,88,3,16,21,80,10,30,80,17,16,25,22,88,3,0,10,25,0,11,80,12,11,80,10,26,4,4,17,30,0,28,92,69,30,2,10,21,80,12,12,80,4,12,80,10,22,19,0,88,4,13,29,80,20,13,17,1,10,17,17,13,2,0,88,31,3,88,4,13,29,80,6,17,2,6,20,21,69,30,31,9,20,31,18,11,94,69,54,17,8,29,28,28,84,80,44,88,24,4,14,21,69,30,31,16,22,20,69,12,24,4,12,80,17,16,21,69,11,5,8,88,31,3,88,4,13,17,3,69,11,21,23,17,21,22,88,25,22,88,17,69,11,25,29,12,24,69,8,17,23,12,80,10,30,80,17,16,21,69,11,1,16,25,2,0,88,31,3,88,4,13,29,80,21,29,2,12,21,21,17,29,2,69,23,22,69,12,24,0,88,19,12,10,19,9,29,80,18,16,31,22,29,80,1,17,17,8,29,4,0,10,80,12,11,80,84,67,80,10,10,80,7,1,80,21,13,4,17,17,30,2,88,4,13,29,80,22,13,29,69,23,22,69,12,24,12,11,80,22,29,2,12,29,3,69,29,1,16,25,28,69,12,31,69,11,92,69,17,4,69,16,17,22,88,4,13,29,80,23,25,4,12,23,80,22,9,2,17,80,70,76,88,29,16,20,4,12,8,28,12,29,20,69,26,9,69,11,80,17,23,80,84,88,31,3,88,4,13,29,80,21,29,2,12,21,21,17,29,2,69,12,31,69,12,24,0,88,20,12,25,29,0,12,21,23,86,80,44,88,7,12,20,28,69,11,31,10,22,80,22,16,31,18,88,4,13,25,4,69,12,24,0,88,3,16,21,80,10,30,80,17,16,25,22,88,3,0,10,25,0,11,80,17,23,80,7,29,80,4,8,0,23,23,8,12,21,17,17,29,28,28,88,65,75,78,68,81,65,67,81,72,70,83,64,68,87,74,70,81,75,70,81,67,80,4,22,20,69,30,2,10,21,80,8,13,28,17,17,0,9,1,25,11,31,80,17,16,25,22,88,30,16,21,18,0,10,80,7,1,80,22,17,8,73,88,17,11,28,80,17,16,21,11,88,4,4,19,25,11,31,80,17,16,21,69,11,1,16,25,2,0,88,2,10,23,4,73,88,4,13,29,80,11,13,29,7,29,2,69,75,94,84,76,65,80,65,66,83,77,67,80,64,73,82,65,67,87,75,72,69,17,3,69,17,30,1,29,21,1,88,0,23,23,20,16,27,21,1,84,80,18,16,25,6,16,80,0,0,0,23,29,3,22,29,3,69,12,24,0,88,0,0,10,25,8,29,4,0,10,80,10,30,80,4,88,19,12,10,19,9,29,80,18,16,31,22,29,80,1,17,17,8,29,4,0,10,80,12,11,80,84,86,80,35,23,28,9,23,7,12,22,23,69,25,23,4,17,30,69,12,24,0,88,3,4,21,21,69,11,4,0,8,3,69,26,9,69,15,24,12,27,24,69,49,80,13,25,20,69,25,2,23,17,6,0,28,80,4,12,80,17,16,25,22,88,3,16,21,92,69,49,80,13,25,6,0,88,20,12,11,19,10,14,21,23,29,20,69,12,24,4,12,80,17,16,21,69,11,5,8,88,31,3,88,4,13,29,80,22,29,2,12,29,3,69,73,80,78,88,65,74,73,70,69,83,80,84,87,72,84,88,91,69,73,95,87,77,70,69,83,80,84,87,70,87,77,80,78,88,21,17,27,94,69,25,28,22,23,80,1,29,0,0,22,20,22,88,31,11,88,4,13,29,80,20,13,17,1,10,17,17,13,2,0,88,31,3,88,4,13,29,80,6,17,2,6,20,21,75,88,62,4,21,21,9,1,92,69,12,24,0,88,3,16,21,80,10,30,80,17,16,25,22,88,29,16,20,4,12,8,28,12,29,20,69,26,9,69,65,64,69,31,25,19,29,3,69,12,24,0,88,18,12,9,5,4,28,2,4,12,21,69,80,22,10,13,2,17,16,80,21,23,7,0,10,89,69,23,22,69,12,24,0,88,19,12,10,19,16,21,22,0,10,21,11,27,21,69,23,22,69,12,24,0,88,0,0,10,25,8,29,4,0,10,80,10,30,80,4,88,19,12,10,19,9,29,80,18,16,31,22,29,80,1,17,17,8,29,4,0,10,80,12,11,80,84,86,80,36,22,20,69,26,9,69,11,25,8,17,28,4,10,80,23,29,17,22,23,30,12,22,23,69,49,80,13,25,6,0,88,28,12,19,21,18,17,3,0,88,18,0,29,30,69,25,18,9,29,80,17,23,80,1,29,4,0,10,29,12,22,21,69,12,24,0,88,3,16,21,3,69,23,22,69,12,24,0,88,3,16,26,3,0,9,5,0,22,4,69,11,21,23,17,21,22,88,25,11,88,7,13,17,19,13,88,4,13,29,80,0,0,0,10,22,21,11,12,3,69,25,2,0,88,21,19,29,30,69,22,5,8,26,21,23,11,94]

alphabet_frequency = [0.082, 0.015, 0.028, 0.043, 0.13, 0.022, 
                      0.02, 0.061, 0.07, 0.0015, 0.0077, 0.04, 
                      0.024, 0.067, 0.075, 0.019, 0.00095, 0.06, 
                      0.063, 0.091, 0.028, 0.0098, 0.024, 0.0015, 
                      0.02, 0.00074]


def chi_squared(f, e):
    """
    Using chi_squared and checking for the min error results in
    the shortest pad.
    """
    return sum([(f[i] - e[i])**2 / e[i] for i in range(len(f))])


def dot(u, v):
    """
    Using dot and checking for the max error results in the 
    longest possible pad, which could be a repeated shorter
    pad.

    A dot product can be used because the result will be larger if
    the vectors are more identical to each other. For perfectly identical
    vectors, each term produces a square.

    This might be a faster method than chi_squared because, with the
    use of numpy, the calculations can be vectorized.
    """
    return sum([u[i] * v[i] for i in range(len(u))])


def count_frequency(text):
    """
    Returns a list with the percentage of the frequency
    that a-z occur in the given text.
    """
    alphabet = "".join(map(chr, range(97, 97 + 26)))
    n = len(text) - text.count(' ')
    frequencies = [text.count(letter) / n for letter in alphabet]
    return frequencies


def decipher_xor_pad(cipher, pad_length):
    """
    Cracks an xor'ed text for a certain path length. It creates
    a frequency table for all the letters for a certain pad, and
    compares it with the Chi-squared test to a frequency table
    for English letters. The lowest error is chosen as the pad.
    """
    ciphers = [cipher[i::pad_length] for i in range(pad_length)]
    pad = [0] * pad_length
    for i in range(pad_length):
        min_error = inf
        min_pad = 0
        for p in range(256):
            decoded_cipher = [c^p for c in ciphers[i]]
            decoded_text = "".join(map(chr, decoded_cipher))
            frequencies = count_frequency(decoded_text)
            error = chi_squared(frequencies, alphabet_frequency)
            if error < min_error:
                min_error, min_pad = error, p
        pad[i] = min_pad
    for i in range(len(cipher)):
        cipher[i] ^= pad[i % pad_length]
    return pad, cipher


def guess_pad_length(cipher, max_length):
    """
    Guesses the pad length by using the same technique as cracking
    the text. But now only for a single pad.
    """
    min_error = inf
    min_i = 0
    for i in range(1, max_length + 1):
        for j in range(256):
            decoded_cipher = [c^j for c in cipher[i::i]]
            decoded_cipher_text = "".join(map(chr, decoded_cipher))
            frequencies = count_frequency(decoded_cipher_text)
            error = chi_squared(frequencies, alphabet_frequency)
            if error < min_error:
                min_error, min_i = error, i
    return min_i


def crack_xor_pad(cipher):
    """
    Cracks any xor-encrypted text with an unknown pad, and pad length.
    Max pad length is 20, but can be modified.
    """
    pad_length = guess_pad_length(cipher, 20)
    pad, decoded_cipher = decipher_xor_pad(cipher, pad_length)
    return pad, decoded_cipher


password = "code"
message = """Although life was hard, these people lived on Greenland for many 
years and it became their home. They built houses that were snug and strong 
from stone, wood and turf."""
#message = "secret message"

pad = [ord(c) for c in password]
n = len(pad)
plaintext = [ord(c) for c in message]
ciphertext = [0] * len(plaintext)

for i in range(len(plaintext)):
    ciphertext[i] = plaintext[i] ^ pad[i % n]
    print('{} ^ {} = {}'.format(
        str(plaintext[i]).rjust(3, ' '),
        str(pad[i % n]).rjust(3, ' '),
        str(ciphertext[i]).rjust(3, ' ')
    ))

print(ciphertext)

print('Pad length = {}'.format(guess_pad_length(ciphertext, 8)))
pad, text = decipher_xor_pad(ciphertext, 4)
print("".join(list(map(chr, text))))

# pad, decoded_cipher = crack_xor_pad(ciphertext)
# print("Pad: {}\nText:\n{}".format(
#     ", ".join(map(str, pad)), 
#     "".join(map(chr, decoded_cipher)))
# )

# print('Solution: {}'.format(sum(decoded_cipher)))

"""
    TODO:
        - Create a write-up for the following
        - Compare speeds for different text size, logarithmically increasing.
            - Text sizes: 100, 1000, 10000, 1000000
            - Pad sizes: 3, 4, 5, 6, 7, 8
        - Create a vectorized version with numpy
            - Might be easier to just xor the array again, instead of creating a new one
        - Compare speeds with vectorized version
        - Finish write-up
"""
