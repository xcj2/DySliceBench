from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,pprint,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,a,b,c = inpl()
l = inpln(n)
x = [a,b,c]
res = INF

for flag in itertools.product(range(4), repeat=n):
    cnt = 0
    xx = [[]for i in range(4)]
    for i,bit in enumerate(flag):
        xx[bit].append(i)
    for i in range(3):
        if xx[i] == []:
            break
        cnt += (len(xx[i]) - 1)*10
        sum = 0
        for j in xx[i]:
            sum += l[j]
        cnt += abs(sum-x[i])
    else:
        res = min(res,cnt)
print(res)