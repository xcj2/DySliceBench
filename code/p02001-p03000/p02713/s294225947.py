def euclid(a, b):
    if a == b:
        return a
    elif b > a:
        return euclid(b, a)
    else:
        while b > 0:
            temp = a % b
            a = b
            b = temp
        return a


d = {}
def euclid_memo(a, b):
    if a > b:
        c = b
        b = a
        a = c
    if a in d:
        if not b in d[a]:
            d[a][b] = euclid(a, b)
    else:
        d[a] = {}
        d[a][b] = euclid(a, b)
    return d[a][b]

def calc(K):
    x = 0
    for i in range(1, K + 1):
        for j in range(1, K + 1):
            for k in range(1, K + 1):
                d = euclid_memo(i, j)
                e = euclid_memo(d, k)
                x += e
    return x


K = int(input())
print(calc(K))