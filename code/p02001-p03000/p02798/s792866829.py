from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

def swap(l):
    cnt = 0
    for i in range(n):
        for j in range(i,n):
            if l[i]>l[j]:
                cnt += 1
    return cnt
n = inp()
a = inpl()
b = inpl()
card = []
res = INF
for i in range(n):
    card.append([a[i],b[i],i])
for flag in itertools.combinations(range(n),(n+1)//2):
    f = True
    odd_li = []
    odd_ind = [False] * n
    for i,bit in enumerate(flag):
        c = 1 if bit%2 else 0
        odd_li.append([card[bit][c],bit])
        odd_ind[bit] = True
    if not f:
        continue
    odd_li.sort()
    even_li = []
    for i in range(n):
        c = 0 if i%2 else 1
        if not odd_ind[i]:
            even_li.append([card[i][c],i])
    even_li.sort()
    if n%2:
        for i in range(n//2):
            if odd_li[i][0] <= even_li[i][0] <= odd_li[i+1][0]:
                continue
            else:
                f = False; break
    else:
        for i in range(n//2):
            if i != n//2-1:
                if odd_li[i][0] <= even_li[i][0] <= odd_li[i+1][0]:
                    continue
                else:
                    f = False; break
            else:
                if odd_li[-1][0] <= even_li[-1][0]:
                    continue
                else:
                    f = False; break
    if f:
        after_ind = []
        for i in range(n//2):
            after_ind.append(odd_li[i][1])
            after_ind.append(even_li[i][1])
        if n%2:
            after_ind.append(odd_li[-1][1])
        res = min(res,swap(after_ind))
print(-1 if res == INF else res)