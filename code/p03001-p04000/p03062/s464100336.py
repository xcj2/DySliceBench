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
a = list(li())

absmin = float('inf')
minusnum = 0
ans = 0
for ai in a:
    absmin = min(absmin, abs(ai))
    
    if ai < 0:
        minusnum += 1
        
    ans += ai if ai > 0 else -ai
        
if minusnum % 2 == 0:
    print(ans)

else:
    print(ans - 2*absmin)