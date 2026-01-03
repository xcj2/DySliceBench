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

n,c,k = li()
t = [ni() for _ in range(n)]

t.sort()

ans = 0
people = 0
isfirst = True
for ti in t:
    if isfirst:
        first = ti
        people = 1
        isfirst = False
        
    else:
        if ti <= first + k and people < c:
            people += 1
            
        else:
            ans += 1
            
            people = 1
            first = ti

print(ans+1)