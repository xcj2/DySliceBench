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
b = inpl()
x = 0
y = 0
for i in range(n):
    if b[i] - a[i] > 0:
        x += (b[i] - a[i])//2
    else:
        y += a[i] - b[i]
if x >= y:
    print('Yes')
else:
    print('No')