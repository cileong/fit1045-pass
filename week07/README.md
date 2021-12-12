# FIT1045 PASS - Week 7


Topics covered:

* [Divide and Conquer](#divide-and-conquer)
* [Recursion](#recursion)


## Recursion

* Another loop structure aside from the iterative method (while, for-loops).
* A recursive function is defined in terms of itself, see [here](#computing-n!).
* Strategy: break a problem into smaller instances, find the solutions to these subproblems, then use them to build up to the solution to the entire problem.


Perhaps it is easier to illustrate with an example:


### Computing `n!`

By definition,

```
0! = 1
1! = 1
n! = n x (n-1)!
```

Let's convert it to a more math-y definition:

![equation](https://latex.codecogs.com/svg.latex?%5Cbg_white%20n%21%20%3D%20%5Cbegin%7Bcases%7D%201%20%26%20%5Ctext%7B%2C%20if%20n%20%3D%200%20or%20n%20%3D%201%2C%7D%20%5C%5C%20n%20%5Ccdot%20%28n-1%29%21%20%26%20%5Ctext%7B%2C%20otherwise.%7D%20%5Cend%7Bcases%7D)
