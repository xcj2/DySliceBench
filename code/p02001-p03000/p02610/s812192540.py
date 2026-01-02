import sys
from heapq import heappush, heappop

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 19
MOD = 10 ** 9 + 7
EPS = 10 ** -10

for _ in range(INT()):
    N = INT()
    ans = 0
    adjli1 = [[] for i in range(N)]
    adjli2 = [[] for i in range(N+1)]
    for _ in range(N):
        k, l, r = MAP()
        k -= 1
        if l > r:
            adjli1[k].append(l - r)
        elif l < r:
            adjli2[k+1].append(r - l)
        ans += min(l, r)

    que = []
    for i in range(N):
        for a in adjli1[i]:
            heappush(que, a)
        while len(que) > i+1:
            heappop(que)
    ans += sum(que)
    que = []
    for i in range(N-1, -1, -1):
        for a in adjli2[i]:
            heappush(que, a)
        while len(que) > N-i:
            heappop(que)
    ans += sum(que)
    print(ans)
