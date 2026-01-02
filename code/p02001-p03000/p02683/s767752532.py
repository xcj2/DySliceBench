import sys
sys.setrecursionlimit(300000)
from math import isinf
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M, X = MI()
C = [0] * N
A = [list() for _ in range(N)]
for i in range(N):
    C[i], *A[i] = MI()

ans = INF
for bits in range(2 ** N):
    rikai = [0] * M
    cost = 0
    for i in range(N):
        if (bits >> i) & 1:
            cost += C[i]
            for j, a in enumerate(A[i]):
                rikai[j] += a
    if all(r >= X for r in rikai):
        ans = min(ans, cost)
if isinf(ans):
    print(-1)
else:
    print(ans)