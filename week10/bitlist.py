def bitlist(length):
    current = [0] * length
    res = [current]
    for _ in range(2**length-1):
        next_bitlist = lex_suc(current)
        res.append(next_bitlist)
        current = next_bitlist
    return res

def lex_suc(lst):
    lst = lst.copy()
    n = len(lst)
    for i in range(n-1, -1, -1):
        if lst[i] == 0:
            lst[i] = 1
            break
    for j in range(i+1, n):
        lst[j] = 0
    return lst

if __name__ == '__main__':
    print(*bitlist(6), sep='\n')
