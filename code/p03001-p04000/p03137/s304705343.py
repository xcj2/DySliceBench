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
x = list(li())
if n >= m:
    print(0)

else:
    diffs = []
    
    x.sort()
    
    for idx in range(m-1):
        diffs.append(x[idx+1]-x[idx])
        
    diffs.sort()
    
    for _ in range(n-1):
        diffs.pop()
        
    print(sum(diffs))