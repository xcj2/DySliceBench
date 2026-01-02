def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def sieve(n):
    res = [True for _ in range(n + 1)]
    res[0] = False
    res[1] = False
    i = 2
    while i * i <= n:
        if res[i]:
            for j in range(i * 2, n + 1, i):
                res[j] = False
        i += 1
    return res

def factorize(n):
    if n == 1: return []
    res = []
    x, y = n, 2
    while y * y <= x:
        while x % y == 0:
            res.append(y)
            x //= y
        y += 1
    if x > 1:
        res.append(x)
    return res

from collections import Counter, defaultdict

N = int(input())
A = list(map(int, input().split()))

S = sieve(10**6 + 1)

flag = True

for i in range(N):
    if S[A[i]]:
        S[A[i]] = 0
    else:
        F = set(factorize(A[i]))
        for f in F:
            if S[f]:
                S[f] = 0
            else:
                flag = False
                break
        else:
            continue
        break

if flag:
    print('pairwise coprime')

else:
    res = 0
    for i in range(N):
        res = gcd(res, A[i])
    if res == 1:
        print('setwise coprime')
    else:
        print('not coprime')