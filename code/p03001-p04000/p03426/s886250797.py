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

from itertools import accumulate

h,w,d = li()
a = [list(li()) for _ in range(h)]

num2point = [(-1,-1)]*(h*w)
for r, ai in enumerate(a):
    for c, aij in enumerate(ai):
        num2point[aij-1] = (r, c)
    

dist = [[] for _ in range(d)]
for i in range(h*w):
    if i // d == 0:
        dist[i%d].append(0)
        
    else:
        dist[i%d].append(abs(num2point[i][0]-num2point[i-d][0]) + abs(num2point[i][1]-num2point[i-d][1]))
        
dist_cum = [list(accumulate(dist_row)) for dist_row in dist]


q = ni()
for _ in range(q):
    l,r = li_()
    print(dist_cum[l%d][r//d] - dist_cum[l%d][l//d])