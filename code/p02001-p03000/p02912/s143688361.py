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
a = list(li())

heap = []

for ai in a:
    heappush(heap, -ai)

for _ in range(m):
    bi = -heappop(heap)
    heappush(heap, -(bi//2))

print(-sum(heap))
