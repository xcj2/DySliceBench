import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from heapq import heappop, heappush

n = ni()
a = list(li())

first = []
second = []

for ai in a[:n]:
    heappush(first, ai)
    
for ai in a[2*n:]:
    heappush(second, -ai)
    
fsum = [sum(first)]
ssum = [sum(second)]
    
ans = fsum[0] + ssum[0]

for i in range(n,2*n):
    heappush(first, a[i])
    fmin = heappop(first)
    fsum.append(fsum[-1] - fmin + a[i])
    
    heappush(second, -a[3*n-i-1])
    smax = heappop(second)
    ssum.append(ssum[-1] - smax - a[3*n-i-1])
    
ssum = ssum[::-1]

for fs,ss in zip(fsum, ssum):
    ans = max(ans, fs+ss)
    
print(ans)