# FIT1045 PASS - Week 4

Topics covered:
* [Mutability](#mutability)
* [Slicing](#slicing)


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


***

## Slicing

Slicing a list gives a sublist of that list, as a **shallow copy** of the original list.

To obtain a slice of `lst` from `start` (inclusive), to `stop` (exclusive).

```py
lst[start:stop]
```

Let `lst = [0, 1, 2, 3, 4]`.

| Operation | Evaluates to | Remarks |
|-----------|---------|---------|
| `lst[:]` | `[0, 1, 2, 3, 4]` | By default, `start=0`, `stop=len(lst)`. |
| `lst[0:5]` | `[0, 1, 2, 3, 4]` | Same as doing `lst[:]`. |
| `lst[3:5]` | `[3, 4]` | `4` is not included, as `stop` is exclusive. |
| `lst[:3]` | `[0, 1, 2]` | Similar to `lst[:]`, if `start` is not defined, defaults to `0`. |
| `lst[3:]` | `[3, 4]` | Similar to the above, `stop` defaults to `len(lst)`. |

What if you want every `k` items in `lst` from `start` to `stop`? Define `step`.

```py
lst[start:stop:step]
```

| Operation | Evaluates to | Remarks |
|-----------|---------|---------|
| `lst[3:5:1]` | `[3, 4]` | Equivalent to `lst[3:5]`, `step` defaults to `1` when not defined. |
| `lst[0:4:2]` | `[0, 2, 4]` | Start from index `0`, take every `2` items, stop at index `4` (exclusive). |

If `step` is negative, and `start` or `stop` is not defined, `start` will default to the index of the last item, `-1`; `stop` will default to the index of the 1st item, `-len(lst)`. Recall how negative indexing behaves in Python.

Think of slicing with negative indices this way:

```
                   P  y  t  h  o  n
Positive index:    0  1  2  3  4  5
Negative index:   -6 -5 -4 -3 -2 -1
```

Let `s = 'Python'`,

| Operation | Evaluates to | Remarks |
|-----------|---------|---------|
| `s[::-1]` | `nohtyP` | Traverse from last to first, decrementing the index by `1` each time. |
| `s[::-2]` | `nhy` | Same as above, take every `2`. |
| `s[-3:-6:-1]` | `hty` | Remember the exclusivity of `stop`. |
| `s[-6:-3:1]` | `Pyt` | |

Slicing works on strings (`str`) as well. After all, they are just *strings* of characters. In some languages, a string is, in fact, an immutable array of characters, `char[]`.

Remember, slicing returns a **shallow copy** of the original *sequence*.
