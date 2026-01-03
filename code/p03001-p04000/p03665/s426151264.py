from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def conb(n,r): 
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n,m = inpl()
a = inpl()
odd = even = 0
for x in a:
    if x%2: odd += 1
    else: even += 1
res = pow(2,even)
ores = eres = 0
for i in range(odd+1):
    if i%2 == 0:
        eres += conb(odd,i)
    else:
        ores += conb(odd,i)
if m:
    print(ores*res)
else:
    print(eres*res)