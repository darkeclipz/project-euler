import eulerlib as lib


def is_lychrel(k):
    for _ in range(50):
        k = k + lib.digits_to_int(lib.digits(k)[::-1])
        if lib.is_palindrome(k):
            return False
    return True


def count_lychrel(n):
    count = 0
    for i in range(10, n):
        if is_lychrel(i):
            count += 1
    return count


lib.time_it(lambda: count_lychrel(10000))