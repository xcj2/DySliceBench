import sys
input = sys.stdin.readline

def gcd(a, b):
    while b: a, b = b, a % b
    return a
def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 7, 61] if n < 1<<32 else [2, 3, 5, 7, 11, 13, 17] if n < 1<<48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1: continue
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1: return 0
            t <<= 1
    return 1
def findFactorRho(n):
    m = 1 << n.bit_length() // 8 + 1
    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r-k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x-ys), n)
        if g < n:
            if isPrimeMR(g): return g
            elif isPrimeMR(n//g): return n//g
def primeFactor(N):
    i = 2
    ret = {}
    n = N
    mrFlg = 0
    while i*i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k: ret[i] = k
        i += 1 + i%2
        if i == 101 and n >= 2**20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    mrFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k

    if n > 1: ret[n] = 1
    if mrFlg > 0: ret = {x: ret[x] for x in sorted(ret)}
    return ret

N = int(input())
ans = 0
D = {}
for _ in range(N):
    pf = primeFactor(int(input()))
    a, b = 1, 1
    for p in pf:
        a *= p ** (pf[p] % 3)
        b *= p ** (-pf[p] % 3)
    if a not in D: D[a] = 0
    if a == b:
        if D[a] == 0: ans += 1
    else:
        if b not in D: D[b] = 0
        if D[b] <= D[a]: ans += 1
    D[a] += 1

print(ans)