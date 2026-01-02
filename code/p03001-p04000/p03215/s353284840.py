import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from itertools import accumulate

n,k = li()
a = list(li())

acum = list(accumulate([0]+a))

cand = []
for i in range(n+1):
    for j in range(i+1,n+1):
        cand.append(acum[j] - acum[i])

ans = 0

for mask in range(40, -1, -1):
    satis = sum([bool(ci&(1<<mask)) for ci in cand])

    if satis >= k:
        ans += (1<<mask)
        nex = [ci for ci in cand if ci & (1<<mask)]
        cand = nex
        

print(ans)