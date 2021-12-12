# FIT1045 PASS - Week 7


Topics covered:

* [Divide and Conquer](#divide-and-conquer)
* [Recursion](#recursion)


## Recursion

* Another loop structure aside from the iterative method (while, for-loops).
* A recursive function is defined in terms of itself, see [here](#computing-n).
* Strategy: break a problem into smaller instances, find the solutions to these subproblems, then use them to build up to the solution to the entire problem.


Perhaps it is easier to illustrate with an example:


### Computing `n!`

By definition,

```
0! = 1              // Base case
1! = 1              // Base case
n! = n x (n-1)!
```

Let's convert it to a more math-y definition:

![equation](https://latex.codecogs.com/png.latex?%5Cbg_white%20n%21%20%3D%20%5Cbegin%7Bcases%7D%201%20%26%20%5Ctext%7B%2C%20if%20n%20%3D%200%20or%20n%20%3D%201%2C%7D%20%5C%5C%20n%20%5Ccdot%20%28n-1%29%21%20%26%20%5Ctext%7B%2C%20otherwise.%7D%20%5Cend%7Bcases%7D)


So, to compute `5!`, you'd do (recurse down until we reach the base case, `1!` in this case):
```
5! = 5x4!
4! = 4x3!
3! = 3x2!
2! = 2x1!
1! = 1      // Base case
```

Now we know the value of 1!, we can substitute `1! = 1` into the equation before:

```
2! = 2x1! = 2x1 = 2
```

Continue... (so we recurse back until we reach the solution to the original problem, `5!` in this case)

```
1! = 1
2! = 2x1! = 2x1 = 2
3! = 3x2! = 3x2 = 6
4! = 4x3! = 4x6 = 24
5! = 5x4! = 5x24 = 120
```

This is how the same recursive function looks like in Python:

```py
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
```


### Exercises

The `n`th term of the Fibonacci sequence is given as follows:

![equation](https://latex.codecogs.com/png.latex?%5Cbg_white%20F_n%20%3D%20%5Cbegin%7Bcases%7D%200%20%26%20%5Ctext%7B%2C%20if%20n%20%3D%201%2C%7D%20%5C%5C%201%20%26%20%5Ctext%7B%2C%20if%20n%20%3D%202%2C%7D%20%5C%5C%20F_%7Bn-1%7D%20&plus;%20F_%7Bn-2%7D%20%26%20%5Ctext%7B%2C%20otherwise.%7D%20%5Cend%7Bcases%7D)

<details>
<summary>Identify the base case.</summary>

When `n` is 1 or 2.

</details>

<details>
<summary>Implement the function recursively.
</summary>

```py
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

<details>
<summary>Identify the Big-O time complexity of the above implementation.</summary>

`O(2^N)`, where `N` is the input `n`.
</details>
</details>

<details>
<summary>Implement the function iteratively.</summary>

You see here, this function is easier to reason about **recursively**, isn't it?

There are functions better implemented iteratively. Conversely, there are also functions better implemented recursively. Know your tools!

```py
def fibonacci(n):
    a = 0, b = 1
    for _ in range(n-1):
        a, b = b, a+b
    return a
```

<details>
<summary>Identify the Big-O time complexity of this implementation.</summary>

`O(N)`, where `N` is the input `n`.
</details>
</details>

***

Implement a function `sum(lst)` that returns the sum of the numeric elements in the list `lst` **recursively**.

```
>>> sum([1, 2, 3, 4, 5])
15
>>> sum(list(range(1, 101)))
5050
```

Here is how the function would be implemented **iteratively**.

```py
def sum(lst):
    total = 0
    for element in lst:
        total += element
    return total
```

Can you do it **recursively**?

<details>
<summary>Solution</summary>

```py
def sum(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + sum(lst[1:])
```

Note that this solution does not compute the sum in `O(N)` time, where `N == len(lst)`.

Can you compute the time complexity of this solution?

<details>
<summary>Time complexity</summary>

`O(N^2)`, where `N == len(lst)`.

The function will be called `N` times, on each call, a slice of size `N-1` (`N` here refers to the `len(lst)` of the current call) will be created.

So, in total, the length of the slices created is `(N-1) + (N-2) + ... + 1`, which is an A.P. series. The steps taken is in `O(N^2)`.

Can you propose a `O(N)` time **recursive** solution?
</details>
</details>
