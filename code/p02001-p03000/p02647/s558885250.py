import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')
from itertools import accumulate


N, K = MI()
A = LMI()

for _ in range(min(50, K)):
    accum = [0] * (N + 1)
    for i, a in enumerate(A):
        l, r = max(0, i - a), min(N - 1, i + a)
        accum[l] += 1
        accum[r + 1] -= 1
    A = list(accumulate(accum))[:-1]
print(*A)

