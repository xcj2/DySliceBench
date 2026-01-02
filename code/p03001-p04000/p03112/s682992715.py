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

a,b,c = inpl()
x = [-INF] + inpln(a) + [INF]
y = [-INF] + inpln(b) + [INF]
z = inpln(c)

def f(x,y,q):
    res = INF
    qq = []
    cs = bisect.bisect_left(x,q)
    qq.append((x[cs],abs(q - x[cs])))
    qq.append((x[cs-1],abs(q - x[cs-1])))
    while qq:
        now, dist = qq.pop()
        cs = bisect.bisect_left(y,now)
        res = min(res,dist+abs(now - y[cs]))
        res = min(res,dist+abs(now - y[cs-1]))
    return res

for q in z:
    print(min(f(x,y,q),f(y,x,q)))

