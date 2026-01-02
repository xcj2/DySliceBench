import sys
sys.setrecursionlimit(300000)
from bisect import bisect_right, bisect_left

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


X, N = MI()
if N == 0:
    print(X)
    exit()
else:
    P = LMI()
P.sort()
ng = set(P)
m = INF
ans = -1
l, r = min(X - 1, P[0]), max(X + 1, P[-1] + 1)
for i in range(l - 100, r + 100):
    if i in ng:
        continue
    if abs(X - i) < m:
        m = abs(X - i)
        ans = i
print(ans)


