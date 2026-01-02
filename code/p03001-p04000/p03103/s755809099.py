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

n,m = li()
ab = []
for _ in range(n):
    ab.append(tuple(li()))
    
ab.sort()

rest = m
ans = 0
for a,b in ab:
    if rest > b:
        ans += a*b
        rest -= b
        
    elif rest == b:
        ans += a*b
        rest = 0
        
    else:
        ans += a*rest
        rest = 0
        
    if rest == 0:
        break
    
print(ans)