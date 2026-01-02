from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpl()
a.sort()
ma = a.pop()
mi = -1
dif = mod
for i in range(n-1):
    if abs(ma/2-a[i]) < dif:
        mi = i
        dif = abs(ma/2-a[i])
print(ma,a[mi])