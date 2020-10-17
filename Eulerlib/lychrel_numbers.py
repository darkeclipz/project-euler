import eulerlib as lib

def count_lychrel(n):
    count = 0
    for k in range(n):
        for _ in range(50):
            k = k + int(str(k)[::-1])
            strk = str(k)
            if strk == strk[::-1]:
                break
        count += 1
    return count


lib.time_it(lambda: count_lychrel(10000))