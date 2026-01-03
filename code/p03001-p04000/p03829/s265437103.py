# 入力
import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

n,a,b = li()
x = li()

ans = 0
for i in range(n-1):
    if a*(x[i+1]-x[i]) > b:
        ans += b
        
    else:
        ans += a*(x[i+1]-x[i])
        
print(ans)