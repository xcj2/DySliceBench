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

a = ni()
b = ni()
c = ni()
x = ni()

ans = 0

for ai in range(a+1):
    for bi in range(b+1):
        for ci in range(c+1):
            if 500*ai + 100*bi + 50*ci == x:
                ans += 1
                
print(ans)