import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from heapq import heappop, heappush

n, m = li()
works = []
heap = []
ans = 0

for i in range(n):
    ai, bi = li()
    heappush(works, (ai, bi))

for i in range(1, m+1):
    while works:
        ai, bi = heappop(works)
        if ai > i:
            heappush(works, (ai, bi))
            break
        else:
            heappush(heap, -bi)

    if heap:
        ans += -heappop(heap)

print(ans)


