# FIT1045 PASS - Week 4

Topics covered:
* [Mutability](#mutability)


## Mutability
Contrary to mutable objects, immutable objects' values cannot be changed (state mutation) once created.

### Mutable objects
* `list`
* `dict`

### Immutable objects
* `int`
* `float`
* `bool`
* `str`
* `tuple`
* `NoneType`

There is only one copy of `True`, `False` and `None` each.
```py
x = True
y = True

# A Boolean expression that evaluates to True
z = x == y

# Print their addresses on separate lines
print(id(x), id(y), id(z), sep='\n')
```

**Output:**
```
140708208564048
140708208564048
140708208564048
```

Notice all three `True`s have the same address, and all `x`, `y`, `z` are referencing the same `True`. The same applies to `False` and `None` (of `NoneType`) as well.
