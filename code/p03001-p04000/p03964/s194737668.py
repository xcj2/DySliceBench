from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))
 
n = inp()
l = []
r = []
for i in range(n):
    q,w = inpl()
    l.append(q)
    r.append(w)
for i in range(n-1):
    if l[i+1] >= l[i] and r[i+1] >= r[i]:
        continue
    tmp = max(-(-l[i]//l[i+1]), -(-r[i]//r[i+1]))
    l[i+1] *= tmp
    r[i+1] *= tmp
print(l[n-1] + r[n-1])