```python
from eulerlib import *
```

# General

## `product(L)`

Returns the product of a `list` of numbers.


```python
product([1, 2, 3, 4, 5, 6])
```




    720



## `factorial(n)`

Returns the factorial n! of a number.


```python
factorial(6)
```




    720



## `is_even(x)`

Returns `true` if a number is even.


```python
is_even(2)
```




    True



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



## `distinct(x)`

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



## `is_pandigital_to_n`

# Sets


## `equal_sets`
## `union_sets`
## `intersect_sets`

# Primes

## `is_prime`
## `prime_counting_function`
## `prime_counting_function_inv`
## `prime_factorization`

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

## `permutations`
## `next_permutation`
## `previous_permutation`
## `is_permutation`
## `is_permutation3`

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



## `palindromes`

# Strings

## `string_split_2d`
## `to_binary_string`

## `is_palindrome`

# Utility

## `time_it(f, [args])`

Executes a function and prints the runtime in seconds. Arguments are passed in via a list of arguments.


```python
time_it(lambda x: prime_factorization(x), [67886])
```

    --- Timed execution for <lambda> ----------------
    Running...
    Solution is [2, 7, 13, 373]
    Executed in 0.022966 seconds
    

## `sieve_to_list(S)`

Returns the sieve as a list where the index is the number where it was `true`.


```python
S = prime_sieve(20)
sieve_to_list(S)
```




    [2, 3, 5, 7, 11, 13, 17, 19, 20]



# Other

## `lambertw`


```python

```
