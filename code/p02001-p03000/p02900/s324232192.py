def primeFactor(N):
    i = 2
    ret = {}
    n = N
    mrFlg = 0
    while i**2 <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
            ret[i] = k
        i += 1
        if i == 101 and n >= (2**20):
            def findFactorRho(N):
                def gcd(a, b):
                    while b: a, b = b, a % b
                    return abs(a)
                def f(x, c):
                    return ((x ** 2) + c) % N
                semi = [N]
                for c in range(1, 99):
                    x, y, d = 2, 2, 1
                    while d == 1:
                        x = f(x, c)
                        y = f(f(y, c), c)
                        d = gcd(abs(x-y), N)
                    if d != N:
                        if isPrimeMR(d): return d
                        elif isPrimeMR(N//d):
                            return N//d
                        else:
                            semi.append(d)
            while True:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                    break
                else:
                    mrFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                        ret[j] = k
                if n == 1: break

    if n > 1: ret[n] = 1
    if mrFlg > 0:
        def dict_sort(X):
            Y={}
            for x in sorted(X.keys()):
                Y[x] = X[x]
            return Y
        ret = dict_sort(ret)
    return ret

def isPrimeMR(n):
    if n == 2:
        return True
    if n == 1 or n & 1 == 0:
        return False
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            return False
        return True

def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)

A, B = map(int, input().split())
N = gcd(A, B)
pf = primeFactor(N)

print(len(pf)+1)
