import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from itertools import accumulate

n,k = li()
xs = []
ys = []
points = []
for _ in range(n):
    x,y = li()
    xs.append(x)
    ys.append(y)
    points.append((x,y))
    
xs.sort()
ys.sort()

rank_x = {}
rank_y = {}
for i, x in enumerate(xs):
    rank_x.update({x:i+1})
for i, y in enumerate(ys):
    rank_y.update({y:i+1})

field = [[0 for _ in range(n+1)] for _ in range(n+1)]
for px,py in points:
    field[rank_y[py]][rank_x[px]] = 1
    
for row in range(n+1):
    field[row] = list(accumulate(field[row]))
    
for col in range(n+1):
    for row in range(n):
        field[row+1][col] += field[row][col]

ans = float("inf")
for xst in range(n):
    for xed in range(xst+1,n):
        for yst in range(n):
            for yed in range(yst+1,n):
                if field[yed+1][xed+1] + field[yst][xst] \
                    -field[yed+1][xst] - field[yst][xed+1]>= k:
                    ans = min(ans, (xs[xed]-xs[xst])*(ys[yed]-ys[yst]))

print(ans)