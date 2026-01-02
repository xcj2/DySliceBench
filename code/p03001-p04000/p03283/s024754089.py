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

from itertools import accumulate

n,m,q = li()
grid = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    l,r = li()
    grid[0][r] += 1
    if l+1 <= n:
        grid[l+1][r] -= 1
    
imos = [list(accumulate(grid[row])) for row in range(n+1)]
for row in range(n):
    for col in range(n+1):
        imos[row+1][col] += imos[row][col]
        
for _ in range(q):
    p,q = li()
    print(imos[p][q])