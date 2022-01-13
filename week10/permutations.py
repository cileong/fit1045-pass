def permutations(a, b):
    first = list(range(a, b))
    last = list(reversed(first))
    res = [first]
    while res[-1] != last:
        _next = lex_suc(res[-1])
        res.append(_next)
    return res

def lex_suc(perm):
    n = len(perm)
    res = perm.copy()

    # Find the index of the first number,
    # that is smaller than the next.
    # Let i be the index.
    for i in range(n-2, -1, -1):
        if perm[i] < perm[i+1]:
            break
    
    # Find the index of the first number
    # to the right of perm[i],
    # that is larger than perm[i].
    # Let j be the index.
    for j in range(n-1, i, -1):
        if perm[j] > perm[i]:
            break
    
    # Swap the two numbers
    res[i], res[j] = res[j], res[i]

    # Reset everything after res[i] to lexicographic min
    return res[:i+1] + list(reversed(res[i+1:]))


if __name__ == '__main__':
    print(*permutations(1, 6), sep='\n')