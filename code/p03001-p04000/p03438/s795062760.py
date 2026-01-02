from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def conb(n,r): return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n = inp()
a = inpl()
b = inpl()
pp = 0
qq = 0
for i in range(n):
    if a[i] > b[i]:
        pp += a[i] - b[i]
    elif a[i] < b[i]:
        qq += (b[i] - a[i]) // 2
if qq >= pp:
    print('Yes')
else:
    print('No')
