import sys

def input(): return sys.stdin.readline()[:-1]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def MATINT(h): return [list(map(int, input().split())) for _ in range(h)]
def MATSTR(h): return [input() for _ in range(h)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
inf = float('inf')
mod = 10 ** 9 + 7

N, M = MAP()
A = []
B = []
C = []
for mm in range(M):
    tmpa, tmpb = MAP()
    A.append(tmpa)
    B.append(tmpb)
    tmpc = LIST()
    c = 0
    for cc in tmpc:
        c += 2**(cc-1)
    C.append(c)

dp = [[inf] * (2**N) for _ in range(M+1)]
dp[0][0] = 0
for i in range(M):
    for j in range(2**N):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i+1][j | C[i]] = min(dp[i+1][j | C[i]], dp[i][j] + A[i])
if dp[M][2**N-1] == inf:
    print(-1)
else:
    print(dp[M][2**N-1])
