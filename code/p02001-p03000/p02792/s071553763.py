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


def cmd(n,r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n
 
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
 
    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
 
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
 
    return result

n = inp()
d = defaultdict(int)
for i in range(1,n+1):
    if i%10==0:
        continue
    if i<10:
        d[i*10+i] += 1
        continue
    tmp = str(i)
    d[int(tmp[0]+tmp[-1])] += 1
# print(d)
res = 0
fin = set()
for key in list(d):
    # print(key)
    if key%11==0:
        res += d[key]**2
    else:
        tmp = int(str(key)[-1] + str(key)[0])
        if tmp in fin:
            continue
        fin.add(key); fin.add(tmp)
        res += d[key] * d[tmp] * 2
print(res)