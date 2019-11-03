```python
from eulerlib import *
```

# Eulerlib

This is an overview of the most used functions from Eulerlib. 

 * **General**
   * `product(L)`
   * `factorial(n)`
   * `is_even(x)`
   * `is_odd(x)`
   * `shift(L, n)`
   * `modpow(a, n, p)`
   * `simplify_fraction(a, b)`
   * `quadratic.solve(a, b, c)`
   * `gcd(a, b)`
   * `lcm(a, b)`
   * `lcm3(a, b, c)`
   * `distinct(L)`
 * **Numbers**
   * `is_number(x)`
   * `divisors(x)`
   * `proper_divisors(x)`
   * `restricted_divisors(x)`
   * `is_pandigital_to_n(L, n)`
 * **Fractions**
   * ...
 * **Sets**
   * `equal_sets(L[S])`
   * `union_sets(L[S])`
   * `intersect_sets(L[S])`
 * **Primes**
   * `is_prime(x, k)`
   * `prime_counting_function(n)`
   * `prime_counting_function_inv(x)`
   * `prime_factorization(x)`
   * `prime_sieve(n)`
 * **Permutations**
   * `permutations(L)`
   * `next_permutation(L)`
   * `previous_permutation(L)`
   * `is_permutation(A, B)`
   * `is_permutation3(A, B, C)`
 * **Fibonacci**
   * `is_fibonacci_number(x)`
   * `fibonacci_n(n)`
   * `fibonacci_n_inv(Fn)`
 * **Generators**
   * `primitive_pythagorean_triplet_generator(n)`
   * `palindrome_generator(lower, upper)`
 * **Strings**
   * `string_split_2d(x)`
   * `to_binary_string(x)`
   * `is_palindrome(x)`
 * **Utility**
   * `time_it(f, [args])`
   * `sieve_to_list(L)`
 * **Other**
   * `lambertw(x)`

# General

## `product(L)`

Returns the product of a `list` of numbers.


```python
product([1, 2, 3, 4, 5, 6])
```

## `factorial(n)`

Returns the factorial n! of a number.


```python
factorial(6)
```

## `is_even(x)`

Returns `true` if a number is even.


```python
is_even(2)
```

## `is_odd(X)`

Returns `true` if a number is odd.


```python
is_odd(17)
```




    1



## `shift(L, n)`

Shift all the elements in the list by n.


```python
shift(['A', 'B', 'C', 'D'], 2)
```




    ['C', 'D', 'A', 'B']



## `modpow(a, n, p)`

Use Fermat's little theorem to calculate `a^n mod p`, which can handle very large exponents. Calculates in O(log n) time.


```python
modpow(397, 2603, 10)
```




    3



## `simplify_fraction(a, b)`

Simplifies a fraction a / b to the lowest common form.


```python
simplify_fraction(22, 6)
```




    (11, 3)



## `quadratic.solve`

Solves a polynomial of the form: `ax^2 + bx + c = 0`.


```python
quadratic.solve(2, -2, -10)
```




    (-1.79128784747792, 2.79128784747792)



## `gcd(a, b)`

Determines the greatest common divisor for a and b with the Euclidean Algorithm.


```python
gcd(273, 14)
```




    7



## `lcm(a, b)`

Calculate the least common multiple (LCM) with the GCD algorithm using: LCM(a,b) = (a*b)/GCD(a,b).


```python
lcm(22, 3)
```




    66.0



## `lcm3(a, b, c)`

Calculating the LCM for multiple digits is done with LCM(a,b,c) = LCM(LCM(a,b),c)


```python
lcm3(22, 3, 13)
```




    858.0



## `distinct(L)`

Returns a `list` of unique elements.


```python
distinct([1, 1, 1, 2, 3])
```




    [1, 2, 3]



## `digits(x)`

Returns the digits of a number in a `list`.


```python
digits(34587)
```




    [3, 4, 5, 8, 7]



## `digits_to_int(L)`

Concatenate a list of digits to an `int`.


```python
digits_to_int([1, 2, 3])
```




    123



# Numbers

## `is_number(x)`

Returns `true` if the number is an instance of an `int` or `float`.


```python
is_number(8)
```




    True




```python
is_number('c')
```




    False



## `divisors(x)`

Returns all the divisors for a number x, including x.


```python
divisors(1001)
```




    [1, 7, 11, 13, 77, 91, 143, 1001]



## `proper_divisors(x)`

Returns all the proper divisors for a number x, excluding x.


```python
proper_divisors(1001)
```




    [1, 7, 11, 13, 77, 91, 143]



## `restricted_divisors(x)`

Returns all the restricted divisors for a number x, excluding 1 and x.


```python
restricted_divisors(1001)
```




    [7, 11, 13, 77, 91, 143]



## `is_pandigital_to_n(L, n)`

Returns `true` if a list of numbers is pandigital from 1 up to n.


```python
is_pandigital_to_n([3, 1, 4, 2], 4)
```




    True



# Sets

## `equal_sets(L[S])`

Returns `true` if all the sets s in S are equal.


```python
S1 = set([1, 2, 3])
S2 = set([1, 2, 3])
S3 = set([1, 2, 3])
equal_sets([S1, S2, S3])
```




    True



## `union_sets(L[S])`

Returns the union of all sets in S.


```python
S1 = set([1, 2, 3])
S2 = set([4, 5, 6])
S3 = set([7, 8, 9])
union_sets([S1, S2, S3])
```




    {1, 2, 3, 4, 5, 6, 7, 8, 9}



## `intersect_sets`

Returns the intersection of all sets in S.


```python
S1 = set([1, 2, 3])
S2 = set([1, 3, 4])
S3 = set([1, 5, 6])
intersect_sets([S1, S2, S3])
```




    {1}



# Primes

## `is_prime(x, k)`

Test if a number n is prime k-times.


```python
is_prime(17, 1)
```




    True



## `prime_counting_function(n)`

Return the number of primes below a given number.


```python
prime_counting_function(100)
```




    21.71472409516259



## `prime_counting_function_inv(x)`

Returns the upper bound for a given number of primes.


```python
prime_counting_function_inv(22)
```




    102



## `prime_factorization(x, S?)`

actorizes a number into the prime factorization. Requires a sieve to be quick, if sieve is not specified it will generate one itself.


```python
prime_factorization(1001)
```




    [7, 11, 13]



## `prime_sieve(n)`

Generates an array up to n, which determines if the index of the array is a prime number. Used for prime testing.


```python
S = prime_sieve(10)
S
```




    [False, False, True, True, False, True, False, True, False, False, True]



To test if 7 is prime:


```python
S[7]
```




    True



# Permutations

## `permutations(L)`

Generates all the permutations for a `list`.


```python
list(permutations(['A', 'B', 'C']))
```




    [['A', 'B', 'C'],
     ['B', 'A', 'C'],
     ['C', 'A', 'B'],
     ['A', 'C', 'B'],
     ['B', 'C', 'A'],
     ['C', 'B', 'A']]



## `next_permutation(L)`

For any given permutation P, give the next permutation. If there is no next permutation, P will be returned.


```python
next_permutation(['A', 'B', 'C'])
```




    ['A', 'C', 'B']



## `previous_permutation(L)`

For any given permutation P, give the previous permutation. If there is no pervious permutation, P will be returned.


```python
previous_permutation(['A', 'C', 'B'])
```




    ['A', 'B', 'C']



## `is_permutation(A, B)`

Returns true if A and B are permutations of each other.


```python
is_permutation(['A', 'B'], ['B', 'A'])
```




    True



## `is_permutation3(A, B, C)`

Returns true if A, B and C are permutations of each other.


```python
A = [1, 2, 3]
B = shift(A, 1)
C = shift(B, 1)
print(A, B, C)
is_permutation3(A, B, C)
```

    [1, 2, 3] [2, 3, 1] [3, 1, 2]
    




    True



# Fibonacci

## `is_fibonacci_number(x)`

Test if x is a Fibonacci number.


```python
is_fibonacci_number(21)
```




    True



## `fibonacci_n(n)`

Calculate the nth Fibonacci number (Fn).


```python
fibonacci_n(7)
```




    13.0



## `fibonacci_n_inv(Fn)`

Calculate the n for Fn for a Fibonacci number.


```python
fibonacci_n_inv(13)
```




    7



# Generators

## `primitive_pythagorean_triplet_generator(n)`

Generates n primitive pythagorean triplets.


```python
list(primitive_pythagorean_triplet_generator(6))
```




    [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41)]



## `palindrome_generator(lower, upper)`

Generates all palindromes between [lower, upper].


```python
palindrome_generator(1, 120)
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111]




```python

```

# Strings

## `string_split_2d(x)`

Split a string of 2D data into lists.


```python
string_split_2d("1,2\n3,4")
```




    [['1', '2'], ['3', '4']]



## `to_binary_string(x)`

Useful to convert a number into a binary number.


```python
to_binary_string(42)
```




    '101010'



## `is_palindrome(x)`

Returns true if a number or a string is a palindrome.


```python
is_palindrome(10001)
```




    True




```python
is_palindrome("alula")
```




    True



# Utility

## `time_it(f, [args])`

Executes a function and prints the runtime in seconds. Arguments are passed in via a list of arguments.


```python
time_it(lambda x: prime_factorization(x), [67886])
```

    --- Timed execution for <lambda> ----------------
    Running...
    Solution is [2, 7, 13, 373]
    Executed in 0.022939 seconds
    

## `sieve_to_list(L)`

Returns the sieve as a list where the index is the number where it was `true`.


```python
S = prime_sieve(20)
sieve_to_list(S)
```




    [2, 3, 5, 7, 11, 13, 17, 19, 20]



# Other

## `lambertw(x)`

Lambert W function with Newton's Method.


```python
lambertw(2)
```




    0.852605502013737


