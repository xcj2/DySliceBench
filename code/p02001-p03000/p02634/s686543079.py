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
MOD = 998244353

a, b, c, d = MAP()
dp0 = list2d(c+1, d+1, 0)
dp1 = list2d(c+1, d+1, 0)

dp1[a][b] = 1
for i in range(a, c+1):
    for j in range(b, d+1):
        dp0[i][j] += dp0[i-1][j] * j
        dp0[i][j] += dp1[i-1][j] * j
        dp1[i][j] += dp1[i][j-1] * i
        dp1[i][j] += dp0[i][j-1]
        dp0[i][j] %= MOD
        dp1[i][j] %= MOD
ans = (dp0[c][d] + dp1[c][d]) % MOD
print(ans)
