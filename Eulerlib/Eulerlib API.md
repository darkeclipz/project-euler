# Introduction

Eulerlib is a library that contains mathematical formulas or algorithms to help in solving problems for Project Euler. As more problems are completed, more methods are added to the library.

In this document all the current functions will be demonstrated, and some notes on their implementation.


```python
from eulerlib import *
```

# Functions

The library currently contains the following functions.

## `time_it`

Executes a function and prints the runtime in seconds. Arguments are passed in via a list of arguments.


```python
time_it(lambda x: prime_factorization(x), [67886])
```

    --- Timed execution for <lambda> ----------------
    Running...
    Solution is [2, 7, 13, 373]
    Executed in 0.022938 seconds
    

## `distinct`

Returns a list of unique elements.


```python
distinct([1, 1, 1, 2, 3])
```




    [1, 2, 3]



## `is_number`

Returns `true` if the number is an instance of an `int` or `float`.


```python
is_number(8)
```




    True




```python
is_number('c')
```




    False






## `divisors`
## `sum_of_proper_divisors_sieve`
## `prime_sieve`
## `sieve_to_list`
## `triangle_number`
## `is_triangle_number`
## `triangle_number_sieve`
## `hexagonal_number`
## `is_hexagonal_number`
## `pentagonal_number`
## `is_pentagonal_number`
## `proper_divisors`
## `restricted_divisors`
## `is_perfect_number`
## `is_abundant_number`
## `is_deficient_number`
## `digits`
## `digits_to_int`
## `is_fibonacci_number`
## `fibonacci_n`
## `fibonacci_n_inv`
## `gcd`
## `lcm`
## `lcm3`
## `primitive_pythagorean_triplet_generator`
## `prime_counting_function`
## `lambertw`
## `prime_counting_function_inv`
## `product`
## `factorial`
## `is_even`
## `is_odd`
## `permutations`
## `shift`
## `is_palindrome`
## `is_pandigital_to_n`
## `to_binary_string`
## `palindromes`
## `string_split_2d`
## `simplify_fraction`
## `intersect_sets`
## `quadratic.solve`
## `modpow`
## `is_prime`
## `next_permutation`
## `previous_permutation`
## `prime_factorization`
## `is_permutation`
## `is_permutation3`
## `equal_sets`
## `union_sets`


```python

```
