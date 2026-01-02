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

last = defaultdict(int)
ans = 0
for d in range(D):
    m = -INF
    ans = -1
    for i in range(26):
        lans = S[d][i]
        for j in range(26):
            if i == j:
                lans -= C[j] * (d + 1 - d - 1)
            else:
                lans -= C[j] * (d + 1 - last[j])
        if lans > m:
            m = lans
            ans = i
    print(ans + 1)
