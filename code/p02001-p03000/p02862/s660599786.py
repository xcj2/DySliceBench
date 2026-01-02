import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    x,y=map(int, input().split())
    if (2*y-x)%3!=0 or (2*x-y)%3!=0:
        print(0)
    else:
        a=(2*y-x)//3
        b=(2*x-y)//3
        c=a+b

        def cmb(n, r, p):
            if (r < 0) or (n < r):
                return 0
            r = min(r, n - r)
            return fact[n] * factinv[r] * factinv[n - r] % p

        p = 10 ** 9 + 7
        N = c
        fact = [1, 1]  # fact[n] = (n! mod p)
        factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
        inv = [0, 1]  # factinv 計算用

        for i in range(2, N + 1):
            fact.append((fact[-1] * i) % p)
            inv.append((-inv[p % i] * (p // i)) % p)
            factinv.append((factinv[-1] * inv[-1]) % p)

        print(cmb(c, min(a,b), p))
resolve()