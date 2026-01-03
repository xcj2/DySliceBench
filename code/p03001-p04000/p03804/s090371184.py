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


n,m = li()
a = []
b = []
for _ in range(n):
    a.append(ns())
for _ in range(m):
    b.append(ns())

# n-m+1行,列を探索
contain = False
for row in range(n-m+1):
    for col in range(n-m+1):
        match = True
        for r in range(m):
            if a[row+r][col:col+m] != b[r]:
                match = False
                
        if match:
            contain = True
            
if contain:
    print("Yes")
else:
    print("No")
            
        
