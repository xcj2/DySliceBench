from collections import Counter,defaultdict,deque
from heapq import heapify,heappop,heappush
import sys,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

def conb(n,r): 
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n,p = inpl()
a = inpl()
res = 0
odd = 0
even = 0
for i in a:
    if i%2:
        odd += 1
    else:
        even += 1
# print(odd,even)
tmp = 0 if p == 0 else 1
for i in range(tmp,odd+1,2):
    for j in range(0,even+1):
        res += conb(odd,i) * conb(even,j)
print(res)