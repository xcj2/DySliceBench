import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c for j in range(b)] for i in range(a)]
def list3d(a, b, c, d): return [[[d for k in range(c)] for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e for l in range(d)] for k in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10**9)
INF = 10**19
MOD = 10**9 + 7
EPS = 10**-10

def factorize(num: int) -> dict:
    """ 素因数分解 """
    from math import sqrt
    from collections import Counter

    d = Counter()
    for i in range(2, int(sqrt(num))+1):
        while num % i == 0:
            num //= i
            d[i] += 1
        if num == 1:
            break
    if num != 1:
        d[num] += 1
    return d

def extgcd(a, b, x, y):
    """ 拡張ユークリッドの互除法(ax+by=gcd(a, b)の解を求める) """

    if b == 0:
        x = 1
        y = 0
        return (y, x)
    else:
        x, y = extgcd(b, a%b, y, x)
        y -= a // b * x
        return (y, x)

N = INT()

fact = list(factorize(N*2).items())
M = len(fact)

ans = N
for bit in range(1<<M):
    a = b = 1
    for i in range(M):
        if (bit>>i) & 1:
            a *= fact[i][0] ** fact[i][1]
        else:
            b *= fact[i][0] ** fact[i][1]
    y, x = extgcd(a, b, 0, 0)
    if x == 0 or y == 0:
        continue
    res = min(a*abs(x), b*abs(y))
    ans = min(ans, res)
print(ans)
