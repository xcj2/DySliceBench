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
works = [[] for _ in range(m+1)]
for _ in range(n):
    ai, bi = li()
    if m-ai >= 0:
        works[m-ai].append(bi)

pque = []
ans = 0
for mi in range(m, -1, -1):
    if works[mi]:
        for wi in works[mi]:
            heappush(pque, -wi)

    if pque:
        ans += -heappop(pque)

print(ans)