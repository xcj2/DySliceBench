import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 6 + 3
def POW(x, y): return pow(x, y, MOD)
def INV(x, m=MOD): return pow(x, m - 2, m)
def DIV(x, y, m=MOD): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

def main():
    Q = II()
    query = []
    for _ in range(Q):
        query.append(LI())
    fact = [1] * MOD
    for i in range(1, MOD):
        fact[i] = fact[i - 1] * i % MOD
    ifact = [1] * MOD
    ifact[MOD - 1] = pow(fact[MOD - 1], MOD - 2, MOD)
    for i in range(MOD - 1, 0, -1):
        ifact[i - 1] = ifact[i] * i % MOD
    for x, d, n in query:
        if d == 0:
            ans = pow(x, n, MOD)
        else:
            x = x * pow(d, MOD - 2, MOD) % MOD
            if x + n > MOD or x == 0:
                ans = 0
            else:
                factor = pow(d, n, MOD)
                perm = fact[x + n - 1] * ifact[x - 1] % MOD
                ans = perm * factor % MOD
        print(ans)
    return

main()