from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def f(x):
    cnt = 0
    while x%2 == 0:
        cnt += 1
        x //= 2
    return cnt
def lcm(x,y):
    return x*y//math.gcd(x,y)

n,m = inpl()
a = inpl()
a = list(set(a))
c = list(set([f(x) for x in a]))
if len(c) != 1:
    print(0)
    quit()
c = c[0]
x = 1
for i in range(len(a)):
    x = lcm(a[i]//2, x)
# print(x)
print((m+x)//(2*x))