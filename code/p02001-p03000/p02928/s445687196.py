import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, K = MI()
A = LMI()

# P[i] := i番目より後ろにA[i]より小さい数がいくつあるか
# U[i] := A全体でA[i]より小さい数がいくつあるか
P = [0] * N
U = [0] * N
d = defaultdict(int)
for i, a in enumerate(reversed(A)):
    i = N - 1 - i
    cnt = 0
    for j in range(a):
        cnt += d[j]
    P[i] = cnt
    d[a] += 1
for i, a in enumerate(A):
    cnt = 0
    for j in range(a):
        cnt += d[j]
    U[i] = cnt

ans = 0
for i in range(N):
    v = K * P[i] + U[i] * (K * (K - 1) // 2)
    ans += v
    ans %= MOD
print(ans)