import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

# 繰り返し二乗法
def pow_r_mod(x:int, n:int, mod=10**9+7)->int:
    # 計算量 : log N
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        x %= mod
        n //= 2
    return (K * x) % mod

def table(n:int, p=10**9+7):
    global fact, factinv, inv
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, n+1):
        #fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        #factinv.append((factinv[-1] * inv[-1]) % p)

m, a, b = mi()

P = 10**9+7
N = 2*(10**5)
table(N)

mca = 1
for i in range(1, a+1):
    mca *= (m-i+1) * inv[i]
    mca %= P

mcb = mca
for i in range(a+1, b+1):
    mcb *= (m-i+1) * inv[i]
    mcb %= P

#print((pow_r_mod(2, m)-1-mca-mcb) % P)
print((pow(2, m, P)-1-mca-mcb) % P)