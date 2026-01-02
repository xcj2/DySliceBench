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

from heapq import heappush, heappop
from collections import defaultdict

x, y, z, k = li()
a = list(li())
b = list(li())
c = list(li())

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

amax = a[0]
bmax = b[0]
cmax = c[0]

acnt = 0
bcnt = 0
ccnt = 0

heap = [(-amax - bmax - cmax, acnt, bcnt, ccnt)]
ans = []

visited = defaultdict(int)
visited[(0,0,0)] = 1

for _ in range(k):
    cur, acnt, bcnt, ccnt = heappop(heap)

    if acnt < len(a)-1:
        if not visited[(acnt+1, bcnt, ccnt)]:
            heappush(heap, (-a[acnt+1]-b[bcnt]-c[ccnt], acnt+1, bcnt, ccnt))
            visited[(acnt+1, bcnt, ccnt)] = 1

    if bcnt < len(b)-1:
        if not visited[(acnt, bcnt+1, ccnt)]:
            heappush(heap, (-a[acnt]-b[bcnt+1]-c[ccnt], acnt, bcnt+1, ccnt))
            visited[(acnt, bcnt+1, ccnt)] = 1

    if ccnt < len(c)-1:
        if not visited[(acnt, bcnt, ccnt+1)]:
            heappush(heap, (-a[acnt]-b[bcnt]-c[ccnt+1], acnt, bcnt, ccnt+1))
            visited[(acnt, bcnt, ccnt+1)] = 1

    ans.append(-cur)

for ansi in ans:
    print(ansi)
