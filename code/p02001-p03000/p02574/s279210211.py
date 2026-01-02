import sys
from math import gcd

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 19
MOD = 10 ** 9 + 7
EPS = 10 ** -10

def eratosthenes_sieve(n):

    table = [0] * (n+1)
    table[1] = 1
    for i in range(2, n+1):
        if table[i] == 0:
            for j in range(i, n+1, i):
                table[j] = i
    return table

def factorize(table, num: int) -> dict:
    """ 素因数分解 """
    from math import sqrt
    from collections import Counter

    d = Counter()
    while num != table[num]:
        d[table[num]] += 1
        num = num // table[num]
    if num != 1:
        d[num] += 1
    return d

N = INT()
A = LIST()

def check(se, fact):
    for k in fact:
        if k not in se:
            se.add(k)
        else:
            return False
    return True

table = eratosthenes_sieve(10**6)

is_pc = 1
se = set()
for a in A:
    fact = factorize(table, a)
    if not check(se, fact):
        is_pc = 0
        break

is_sc = 1
g = 0
for a in A:
    g = gcd(g, a)
if g != 1:
    is_sc = 0

if is_pc:
    print('pairwise coprime')
elif is_sc:
    print('setwise coprime')
else:
    print('not coprime')
