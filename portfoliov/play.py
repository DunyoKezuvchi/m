def m(a, b):
    b = sorted(b)
    bi = [i for i in b]
    ai = [i for i in a]
    n = len(a)
    m = len(b)
    j = m - 1
    for i in range(n):
        if (j < 0):
            break
        if (bi[j] > ai[i]):
            ai[i] = bi[j]
            j -= 1
    x = "" . join(ai)
    return x
a,b = map(str, input().split())
print(m(a, b))