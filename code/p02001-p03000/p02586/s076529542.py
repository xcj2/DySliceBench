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
INF = 10 ** 18
MOD = 10 ** 19 + 7
EPS = 10 ** -10

H, W, K = MAP()
grid = list2d(H+1, W+1, 0)
for i in range(K):
    h, w, v = MAP()
    grid[h][w] = v

dp0 = list2d(H+1, W+1, -INF)
dp1 = list2d(H+1, W+1, -INF)
dp2 = list2d(H+1, W+1, -INF)
dp3 = list2d(H+1, W+1, -INF)
dp0[0][1] = dp0[1][0] = 0
for h in range(1, H+1):
    for w in range(1, W+1):
        dp0[h][w] = max(dp0[h][w-1], dp0[h-1][w], dp0[h-1][w], dp1[h-1][w],  dp2[h-1][w], dp3[h-1][w])
        dp1[h][w] = dp1[h][w-1]
        dp2[h][w] = dp2[h][w-1]
        dp3[h][w] = dp3[h][w-1]
        if grid[h][w]:
            dp1[h][w] = max(dp1[h][w], max(dp0[h][w-1], dp0[h-1][w], dp1[h-1][w], dp2[h-1][w], dp3[h-1][w]) + grid[h][w])
            dp2[h][w] = max(dp2[h][w], dp1[h][w-1] + grid[h][w])
            dp3[h][w] = max(dp3[h][w], dp2[h][w-1] + grid[h][w])
ans = max(dp0[H][W], dp1[H][W], dp2[H][W], dp3[H][W])
print(ans)
