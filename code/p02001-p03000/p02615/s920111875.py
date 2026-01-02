import sys
sys.setrecursionlimit(300000)
from heapq import heappush, heappop

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A = LMI()
A.sort(reverse=True)

ans = 0
q = []
for i, a in enumerate(A):
    if i == 0:
        heappush(q, -a)
    else:
        m = -heappop(q)
        ans += m
        heappush(q, -a)
        heappush(q, -a)
print(ans)