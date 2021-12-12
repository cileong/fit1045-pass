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
