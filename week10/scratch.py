lst = [[1, 3], [4, -5], [-6, 2]]

def f(lst):
    return lst[1]

print(max(lst, key=f))