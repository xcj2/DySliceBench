from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

h,w,d = inpl()
a = [inpl() for i in range(h)]
de = defaultdict(int)
for i in range(h):
    for j in range(w):
        de[a[i][j]] = (i,j)
li = dict()
for i in range(d):
    c = 0
    tmp = 0
    while True:
        if de[i+d*c] == 0:
            c += 1
            continue
        tmp = de[i+d*c]
        break
    li[i+d*c] = 0
    while True:
        c += 1
        if de[i+d*c] == 0:
            break
        now = de[i+d*c]
        kyori = abs(now[0]-tmp[0]) + abs(now[1]-tmp[1])
        li[i+d*c] = li[i+d*(c-1)] + kyori
        tmp = now
# print(li)
q = inp()
lr = [inpl() for i in range(q)]
for l,r in lr:
    print(li[r] - li[l])
