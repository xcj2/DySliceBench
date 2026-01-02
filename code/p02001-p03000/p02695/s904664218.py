import bisect
import collections
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
ACMOD = 1000000007
INF = 1 << 62


def lmi():
    return list(map(int, input().split()))


def llmi(n):
    return [lmi() for _ in range(n)]


#
N, M, Q = lmi()
#
ABDC = llmi(Q)


def gen(arr=tuple()):
    score = 0
    if len(arr) == N:
        for a, b, c, d in ABDC:
            if arr[b - 1] - arr[a - 1] == c:
                score += d
        return score
    start = 0 if not arr else arr[-1]
    for i in range(start, M):
        score = max(score, gen(arr + (i,)))
    return score


print(gen())
#
# dp = [[-INF]*M for i in range(N+1)]
#
# for n in range(N):
#     for v in range(M):
#         # target: dp[n+1][v]
