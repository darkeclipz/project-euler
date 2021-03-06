Help on module eulerlib:

NAME
    eulerlib

FUNCTIONS
    digits(x, base=10)
        Returns the the digits of a number.
        Reference: https://en.wikipedia.org/wiki/Digit_sum
        :param x: The number to sum the digits of.
        :param base: The base of the number system.
        :return: Sum of the number x.
    
    digits_to_int(x)
        Concatenate a list of digits to an integer.
        :param x:
        :return:
    
    distinct(x)
        Returns a list of unique elements.
        :param x: List of elements.
        :return: List of unique elements.
    
    divisors(x)
        Returns all the divisors for a number x, including x.
        e.g divisors(1001) = [1, 7, 11, 13, 77, 91, 143, 1001]
        :param x: number >= 1.
        :return: the divisors including 1 and x.
    
    equal_sets(S)
        Returns true if all the sets s in S are equal
        to each other.
        :param S:
        :return:
    
    factorial(n)
        Returns the factorial n! of a number.
        :param n:
        :return:
    
    fibonacci_n(n)
        Calculate the nth Fibonacci number (Fn).
        :param n: which number to calculate.
        :return: The nth Fibonacci number.
    
    fibonacci_n_inv(x)
        Calculate the n for Fn for a Fibonacci number.
        :param x: Fibonacci number.
        :return: The position of the Fibonacci number (Fn)
    
    gcd(a, b)
        Determines the greatest common divisor for a and b
        with the Euclidean Algorithm.
        :param a: First number.
        :param b: Second number.
        :return: Greatest common divisor for a and b.
    
    hexagonal_number(n)
        Calculate the nth hexagonal number.
        :param n: Hn
        :return: Hexagonal number
    
    intersect_sets(S)
        Intersection of a list of sets.
        :param S:
        :return:
    
    is_abundant_number(x)
        Test if a number is an abundant number. A number is abundant
        if the sum of the proper divisors is greater than the number
        itself.
        :param x: number to test.
        :return: True if it is an abundant number.
    
    is_deficient_number(x)
        Test if a number is a deficient number. A number is deficient
        if the sum of the proper divisors is less than the number
        itself.
        :param x: number to test.
        :return: True if it is a deficient number.
    
    is_even(n)
        Returns true if a number is even.
        :param n:
        :return:
    
    is_fibonacci_number(x)
        Test if x is a Fibonacci number.
        :param x: Number to test.
        :return: True if it is a Fibonacci number.
    
    is_hexagonal_number(n)
        Determines if n is a hexagonal number.
        :param n: Hn
        :return: Hexagonal number
    
    is_number(n)
        Returns true if the number is an instance of an int.
        or a float.
        :param n: The number n to be tested.
        :return: True if n is int or float.
    
    is_odd(n)
        Returns true if a number is odd.
        :param n:
        :return:
    
    is_palindrome(x)
        Returns true if a number or a string is a palindrome.
        :param x:
        :return:
    
    is_pandigital_to_n(x, n, zero_based=False)
    
    is_pentagonal_number(n)
        Determines if n is a pentagonal number.
        :param n:
        :return: True if pentagonal.
    
    is_perfect_number(x)
        Test if a number is a perfect number. A number is perfect
        if the sum of the proper divisors is equal to itself.
        :param x: number to test.
        :return: True if it is a perfect number.
    
    is_permutation(A, B)
        Returns true if A and B are permutations of each other.
        :param A:
        :param B:
        :return:
    
    is_permutation3(A, B, C)
        Returns true if A, B and C are permutations of each other.
        :param A:
        :param B:
        :param C:
        :return:
    
    is_prime(n, k)
        Test if a number n is prime k-times.
        :param n: The prime number to be tested.
        :param k: The number of tests.
        :return:
    
    is_triangle_number(n)
        Tests if a number is a triangle number. Solved with the
        inverse of n(n+1)/2, and testing if that solution
        is integer.
        :param n: Number to test.
        :return: True if it is a triangle number.
    
    is_unique_string(s)
        Determines if a given string only consists of unique
        characters.
        :param s: The string to test.
        :return: True if the string only contains unique characters.
    
    lambertw(x)
        Lambert W function with Newton's Method.
        :param x:
        :return:
    
    lcm(a, b)
        Calculate the least common multiple (LCM) with the GCD
        algorithm using: LCM(a,b) = (a*b)/GCD(a,b).
        :param a:
        :param b:
        :return:
    
    lcm3(a, b, c)
        Calculating the LCM for multiple digits is done with
        LCM(a,b,c) = LCM(LCM(a,b),c)
        :param a:
        :param b:
        :param c:
        :return:
    
    modpow(a, n, p)
        Use Fermat's little theorem to calculate a^n mod p, which
        can handle very large exponents. Calculates in O(log n) time.
        :param a: base
        :param n: exponent
        :param p: mod
        :return: (a^n) mod p
    
    next_permutation(P)
        For any given permutation P, give the next permutation.
        If there is no next permutation, P will be returned.
        :param P:
        :return:
    
    palindromes(lower, upper)
        Generates all palindromes between [lower, upper].
        https://stackoverflow.com/a/16344628
        :param lower:
        :param upper:
        :return:
    
    pentagonal_number(n)
    
    permutations(a)
        Generates all the permutations for a set.
        :param a:
        :return:
    
    previous_permutation(P)
        For any given permutation P, give the previous permutation.
        If there is no pervious permutation, P will be returned.
        :param P:
        :return:
    
    prime_counting_function(n)
        Return the number of primes below a given number.
        This is calculated with the proportionality which
        states that \u03c0(n) ~ n / log(n).
        :param n: Upper bound.
        :return: Estimate of the number of primes below the
                 bound.
    
    prime_counting_function_inv(y)
        Returns the upper bound for a given number of primes.
        :param y: How many primes you want.
        :return: Upper bound.
    
    prime_factorization(x, sieve=None)
        Factorizes a number into the prime factorization.
        Requires a sieve to be quick, if sieve is not specified
        it will generate one itself.
        :param x:
        :param sieve:
        :return:
    
    prime_sieve(n)
        Generates an array which determines if the index
        of the array is a prime number. To see if 997 is
        a prime number: sieve[997] == True.
        :param n: Upper limit of numbers.
        :return: List with boolean values.
    
    primitive_pythagorean_triplet_generator(n=inf)
        Generates n primitive pythagorean triplets.
        :param n:
        :return:
    
    product(numbers)
        Returns the product of a list of numbers.
        :param numbers:
        :return:
    
    proper_divisors(x)
        Returns all the proper divisors for a number x, excluding x.
        e.g divisors(1001) = [1, 7, 11, 13, 77, 91, 143]
        :param x: number >= 1.
        :return: the divisors excluding itself.
    
    restricted_divisors(x)
        Returns all the restricted divisors for a number x, excluding 1 and x.
        e.g divisors(1001) = [7, 11, 13, 77, 91, 143]
        :param x: number >= 1.
        :return: the divisors excluding 1 and itself.
    
    shift(a, n=1)
        Shift all the elements in the list by n.
        :param a:
        :param n:
        :return:
    
    sieve_to_list(sieve)
        Returns the sieve as a list where the index is the number
        where it was True.
        :param sieve:
        :return:
    
    simplify_fraction(a, b)
        Simplifies a fraction to the lowest common form.
        :param a:
        :param b:
        :return:
    
    string_split_2d(data, field_delimiter=',', line_delimiter='\n')
        Split a string of 2D data into lists. Example of the data
        1,2
        3,4
        5,6
        to:
        [[1,2],[3,4],[5,6]]
        :param data:
        :param field_delimiter: delimiter used between seperate fields, default: ,
        :param line_delimiter: delimiter used between lines, default: 
        
        :return: 2D list
    
    sum_of_proper_divisors_sieve(n)
        Generates an array with the sum of the divisors
        for that index of the array. To find the sum of
        divisors for 12: sieve[12].
        :param n: Upper limit of numbers.
        :return: List with sum of divisors.
    
    time_it(f, args=None)
    
    to_binary_string(x)
        Useful to convert a number into a binary number.
        :param x:
        :return:
    
    triangle_number(n)
        Calculate the nth triangle number.
        :param n: Fn
        :return: Triangle number for n.
    
    triangle_number_sieve(n)
        Generates a sieve which can be used to tell if a number
        is a triangle number.
        :param n: Up to which n.
        :return: Sieve with boolean values, sieve[3] = True.
    
    union_sets(S)
        Union of a list of sets.
        :param S:
        :return:

FILE
    c:\users\isomorphism\documents\repos\project-euler\eulerlib\eulerlib.py


