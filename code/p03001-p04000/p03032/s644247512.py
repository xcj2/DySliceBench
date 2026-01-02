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

from heapq import heappop

n, k = li()
v = list(li())

ans = 0

for x in range(-(-k//2)):
    if 2*x > k:
        continue

    get = k - x
    if get >= n:
        cnt = 0
        heap = sorted(v)

        while heap[0] < 0 and cnt < x:
            _ = heappop(heap)
            cnt += 1

        ans = max(ans, sum(heap))

    else:
        for i in range(get+1):
            cnt = 0
            heap = sorted(v[:i] + v[n-(get-i):])
            while heap[0] < 0 and cnt < x:
                _ = heappop(heap)
                cnt += 1

            ans = max(ans, sum(heap))

print(ans)