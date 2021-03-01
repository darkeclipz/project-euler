"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two 
primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of 
these four primes, 792, represents the lowest sum for a set of four primes 
with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

import eulerlib as euler

def prime_pair_sets():
    sieve = euler.prime_sieve(10000000)
    primes = euler.sieve_to_list(sieve)
    for prime in primes:
        n = len(str(prime))
        if 4 <= n <= 5:
            groups_that_are_prime = 0
            sub_primes = []
            for i in range(1, n):
                left = int(str(prime)[:i])
                right = int(str(prime)[i:])
                if sieve[left]:
                    groups_that_are_prime += 1
                    sub_primes.append(left)
                if sieve[right]:
                    groups_that_are_prime += 1
                    sub_primes.append(right)
            sub_primes = list(set(sub_primes))
            m = len(sub_primes)
            if m >= n:
                all_orders_are_prime = True
                print(sub_primes)
                for i in range(m):
                    for j in range(m):
                        if i == j:
                            continue
                        test_prime = int(str(sub_primes[i]) + str(sub_primes[j]))
                        if test_prime >= 1000000 and not euler.is_prime(test_prime, 32) or test_prime < 1000000 and not sieve[test_prime]:
                            all_orders_are_prime = False
                            print('  {} is not prime.'.format(test_prime))
                            break
                    if not all_orders_are_prime:
                        break
                if all_orders_are_prime:
                    print(sub_primes)
                    return sum(sub_primes)

                    """
                    doesn't find anything... fuck this problem in particular
                    """

euler.time_it(prime_pair_sets)