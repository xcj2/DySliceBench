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

from collections import Counter

def factorize(n: int):
    d = Counter()
    m= 2
    
    while m*m <= n:
        while n%m == 0:
            n //= m
            d[m] += 1
            
        m += 1
        
    if n > 1:
        d[n] += 1
        
    return d

n,p = li()

facs = factorize(p)

ans = 1
for k in sorted(facs.keys()):
    if facs[k] >= n:
        ans = ans * k**(facs[k]//n)
        
print(ans)