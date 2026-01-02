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

n,k = li()

# すべてmod k == 0
mod0 = 0
modk2 = 0
for i in range(1,n+1):
    if i%k == 0:
        mod0 += 1
        
    if i%k == (k/2):
        modk2 += 1
        
ans = (modk2**3 + mod0**3)
print(ans)
