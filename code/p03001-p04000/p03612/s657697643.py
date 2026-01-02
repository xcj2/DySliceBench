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
cnt = 0
for i in range(n):
    if i == n-1 and a[i] == i+1:
        cnt += 1
        continue
    if a[i] == i+1:
        a[i], a[i+1] = a[i+1], a[i]
        cnt += 1
print(cnt)