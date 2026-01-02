import sys

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

def popcount(i):
    return bin(i).count('1')

N = INT()
S = list(map(int, input()))[::-1]

pcnt1 = S.count(1) - 1
pcnt2 = S.count(1) + 1
base1 = base2 = 0
for i in range(N):
    if S[i]:
        if pcnt1 != 0:
            base1 += pow(2, i, pcnt1)
        base2 += pow(2, i, pcnt2)

ans = [0] * N
for i in range(N):
    if S[i] and pcnt1 == 0:
        ans[i] = 0
        continue
    cur = 0
    if S[i]:
        cur += (base1 - pow(2, i, pcnt1)) % pcnt1
    else:
        cur += (base2 + pow(2, i, pcnt2)) % pcnt2
    cnt = 1
    while cur:
        cur %= popcount(cur)
        cnt += 1
    ans[i] = cnt
for a in ans[::-1]:
    print(a)
