import sys
sys.setrecursionlimit(300000)
from itertools import combinations_with_replacement
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M, Q = MI()
ABCD = [tuple(MI()) for i in range(Q)]

ans = 0
for arr in combinations_with_replacement(range(1, M + 1), N):
    A = list(arr)
    score = 0
    for a, b, c, d in ABCD:
        if A[b - 1] - A[a - 1] == c:
            score += d
    ans = max(ans, score)
print(ans)
