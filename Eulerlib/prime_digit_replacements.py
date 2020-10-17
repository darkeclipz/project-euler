import eulerlib as lib


sieve = lib.prime_sieve(1000000)

def perm(k, n, res = [], memo = {}):
    if n == 1:
        return
    for i in range(len(k)):
        if k[i] == '*':
            continue
        temp = k[i]
        k[i] = '*'
        pstr = ''.join(map(str, k))
        if pstr not in memo.keys():
            res.append(pstr)
            memo[pstr] = True
        perm(k, n-1, res, memo)
        k[i] = temp
    if len(k) == n:
        return res


def pdr(max_n):
    result = {}
    memo = {}
    for i in range(13, max_n):
        if not sieve[i] and i % 11 != 0:
            continue
        print('Testing: {}'.format(i))
        istr = str(i)
        perms = perm(lib.digits(istr), len(istr))
        for p in perms:
            if p in memo.keys():
                continue
            memo[p] = True
            count = 0
            for j in range(0, 10):
                if j == 0 and p[0] == '*':
                    continue
                pnum = int(p.replace('*', str(j)))
                if sieve[pnum]:
                    count += 1
            result[p] = count
            if count == 8:
                print('Smallest prime with eight prime value family is {} with permutation {}'.format(i, p))
                exit(0)


lib.time_it(lambda: pdr(len(sieve)))
