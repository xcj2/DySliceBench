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

k,t = li()
a = list(li())

ans = 0

for ai in a:
    if  k%2 == 1 and ai > k//2 + 1:
        ans = (ai - (k//2+1)) * 2
            
    elif k%2 == 0  and ai > k//2:
        ans = 1 + (ai - (k//2+1)) * 2
        
print(ans)