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

n = inp()
a = inpl()
a.sort()
ln = len(bin(a[-1])) - 2
bit = [defaultdict(int) for i in range(ln)]
res = 0
for i in a:
    tmp = bin(i)
    for _,j in enumerate(tmp[:1:-1]):
        # print(_,j)
        bit[_][j] += 1
# pprint.pprint(bit)
for i,j in enumerate(bit):
    x = j['0']
    y = j['1']
    if x+y < n:
        x = n - y
    # print(i,x,y)
    c = pow(2,i)
    res += x * y * c
    res %= mod
print(res)