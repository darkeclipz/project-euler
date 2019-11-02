# Introduction

Eulerlib is a library that contains mathematical formulas or algorithms to help in solving problems for Project Euler. As more problems are completed, more methods are added to the library.

In this document all the current functions will be demonstrated, and some notes on their implementation.


```python
from eulerlib import *
```

# Functions

## `distinct(x)`


```python
help(distinct)
```

    Help on function distinct in module eulerlib:
    
    distinct(x)
        Returns a list of unique elements.
        :param x: List of elements.
        :return: List of unique elements.
    
    


```python
distinct([1, 1, 1, 2, 3])
```




    [1, 2, 3]



## `is_number(n)`


```python
help(is_number)
```

    Help on function is_number in module eulerlib:
    
    is_number(n)
        Returns true if the number is an instance of an int.
        or a float.
        :param n: The number n to be tested.
        :return: True if n is int or float.
    
    


```python
is_number(1)
```




    True




```python
is_number('c')
```




    False




```python

```
