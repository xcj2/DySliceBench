from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpl()
sum_a = sum(a)
acc = list(itertools.accumulate(a))
ans = mod
if n == 2:
    print(abs(a[0] - a[1]))
else:
    for i in range(n-1):
        tmp = abs(acc[i] - (acc[-1]-acc[i]))
        ans = min(ans, tmp)
    print(ans)