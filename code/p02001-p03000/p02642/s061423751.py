import sys
sys.setrecursionlimit(300000)
from collections import Counter

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A = LMI()

div = set(A)
cnt = Counter(A)
M = max(A)
ng = [False] * (M + 1)
for a in A:
    n = a * 2
    while n <= M:
        ng[n] = True
        n += a
ans = 0
for a in A:
    if cnt[a] >= 2:
        continue
    if ng[a]:
        continue
    ans += 1

print(ans)