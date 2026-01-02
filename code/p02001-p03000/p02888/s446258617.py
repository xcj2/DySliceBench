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
ans = 0
a.sort()
for i in range(n-2):
    for j in range(i+1,n-1):
        b = a[j+1:]
        tmp = a[i] + a[j] - 1
        tt = bisect.bisect_right(b,tmp)
        if tt > 0 :
            ans += tt
print(ans)