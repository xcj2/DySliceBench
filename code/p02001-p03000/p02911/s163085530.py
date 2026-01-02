from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,k,q = inpl()
a = inpln(q)
d = defaultdict(int)
for i in range(q):
    d[a[i]] += 1
for i in range(1,n+1):
    # print(d[i])
    if q - d[i] < k:
        print('Yes')
    else:
        print('No')