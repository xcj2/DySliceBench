from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

a = inpl()
cnt = 0
for i in a:
    if i%2:
        print(cnt)
        quit()
if a[0] == a[1] == a[2]:
    print(-1)
else:
    while True:
        for i in a:
            if i%2:
                print(cnt)
                quit()
        b = [0] * 3
        b[0] = (a[1] + a[2]) // 2
        b[1] = (a[0] + a[2]) // 2
        b[2] = (a[1] + a[0]) // 2
        cnt += 1
        a[::] = b[::]

