import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A = LMI()
d = defaultdict(int)
ans = sum(A)
for a in A:
    d[a] += 1

Q = I()
for q in range(Q):
    B, C = MI()
    ans -= B * d[B]
    ans += C * d[B]
    d[C] += d[B]
    d[B] = 0
    print(ans)