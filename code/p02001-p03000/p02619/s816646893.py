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


D = I()
C = LMI()
S = [LMI() for _ in range(D)]
T = [I() - 1 for _ in range(D)]

last = defaultdict(int)
ans = 0
for d in range(D):
    ans += S[d][T[d]]
    last[T[d]] = d + 1
    for i in range(26):
        ans -= C[i] * (d + 1 - last[i])
    print(ans)
