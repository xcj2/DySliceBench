def binarev(x):
    ans = []
    while x:
        ans.append(x%2)
        x = x//2
    return ans

def power(a, b, *c):
    if c:
        c = c[0]
        bb = binarev(b)
        n = len(bb)
        pool = [a%c] * n
        for i in range(1, n):
            pool[i] = (pool[i-1]**2)%c
        ans = 1
        for i in range(n):
            if bb[i]: ans = (pool[i]*ans)%c
        return ans
    else:
        bb = binarev(b)
        n = len(bb)
        pool = [a] * n
        for i in range(1, n):
            pool[i] = pool[i-1]**2
        ans = 1
        for i in range(n):
            if bb[i]: ans *= pool[i]
        return ans

def root(x, n):
    a = x
    left = 0
    right = x
    while left+1 < right:
        x = (left + right)//2
        if power(x, n) <= a:
            left = x
        else:
            right = x
    return left

def log(x, n):
    a = x
    left = 0
    right = x
    while left+1 < right:
        x = (left + right)//2
        if power(n, x) <= a:
            left = x
        else:
            right = x
    return left

def permod(MOD, N, R=-1):
    from functools import reduce
    if R==-1: R=N
    return reduce(lambda x,y: x*y%MOD, range(N, N-R, -1))


def combod(MOD, N, R):
    return permod(MOD, N, R) * power(permod(MOD, R), MOD-2, MOD) % MOD


n,a,b = map(int, input().split())
p = 7 + 10**9
print((power(2,n,p) - combod(p,n,a) - combod(p,n,b) - 1) % p)