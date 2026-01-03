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
if n%2:
    for i in range(n)[::-2]:
        print(a[i],end=' ')
    for i in range(1,n)[::2]:
        print(a[i],end=' ')
    print()
else:
    for i in range(n)[::-2]:
        print(a[i],end=' ')
    for i in range(n)[::2]:
        print(a[i],end=' ')
    print()
    