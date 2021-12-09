# FIT1045 PASS - Week 5


Topics covered:

* [Loop invariant](#loop-invariant)
* [Exercise](#exercise)


## Loop invariant

A condition that is always true before and immediately after each iteration of a loop.


## Exercise

Find the loop invariant.

```py
def sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total
```

```py
def get_min(lst):
    if len(lst) == 0:
        raise Exception("List is empty")
    else:
        smallest = lst[0]
        for i in range(len(lst)):
            if lst[i] < smallest:
                smallest = lst[i]
        return smallest
```

```py
def count(lst, target):
    occurrences = 0
    for i in range(len(lst)):
        if lst[i] == target:
            occurrences += 1
    return occurrences
```

```py
def mystery(n):
    i = 0
    total = 0
    while i < n:
        if i%2:
            total += i
            i += 1
    return total
```

```py
