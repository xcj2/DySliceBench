from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

def conb(n,r): return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n = inp()
a = inpl()
cntsum = list(itertools.accumulate(a)) + [0]
cntcol = Counter(cntsum)
res = 0
for key in cntcol.keys():
    if cntcol[key] >= 2:
        res += conb(cntcol[key],2)
print(res)
