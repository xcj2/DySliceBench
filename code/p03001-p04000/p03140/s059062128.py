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

n = ni()
a = ns()
b = ns()
c = ns()

ans = 0
for ai, bi, ci in zip(a,b,c):
    if ai == bi == ci:
        continue
    
    elif ai == bi or bi == ci or ci == ai:
        ans += 1
    
    else:
        ans += 2
        
print(ans)