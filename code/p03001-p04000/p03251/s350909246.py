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

n,m,x,y = li()
xs = list(li()) + [x]
ys = list(li()) + [y]

xmax = max(xs)
ymin = min(ys)

if xmax < ymin:
    print("No War")
else:
    print("War")