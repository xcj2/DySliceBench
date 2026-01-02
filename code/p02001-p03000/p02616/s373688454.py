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


N, K = MI()
A = LMI()

if all(a < 0 for a in A) and K % 2 == 1:
    A.sort(reverse=True)
    ans = 1
    for a in A[:K]:
        ans = ans * a % MOD
    print(ans)
    exit(0)

p = []
n = []
for a in A:
    if a < 0:
        heappush(n, a)
    else:
        heappush(p, -a)

ans = 1
cnt = 0
while cnt < K:
    if cnt == K - 1:
        if len(p) > 0:
            ans = ans * -heappop(p) % MOD
        else:
            ans = ans * max(n) % MOD
        cnt += 1
        break
    if len(p) < 1:
        ans = ans * heappop(n) * heappop(n) % MOD
        cnt += 2
    elif len(n) < 2:
        ans = ans * -heappop(p) % MOD
        cnt += 1
    else:
        p0, p1 = -p[0], -p[1] if len(p) > 1 else 1
        if p0 * p1 > n[0] * n[1]:
            ans = ans * -heappop(p) % MOD
            cnt += 1
        else:
            ans = ans * heappop(n) * heappop(n) % MOD
            cnt += 2
print(ans)