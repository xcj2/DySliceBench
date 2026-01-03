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

from collections import defaultdict, Counter

dic = defaultdict(int)

h,w,n = li()

dhs = [-1,-1,-1, 0, 0, 0, 1, 1, 1]
dws = [-1, 0, 1,-1, 0, 1,-1, 0, 1]

for _ in range(n):
    r,c = li()
    for dh, dw in zip(dhs, dws):
        if 1 < r+dh < h and 1 < c+dw < w:
            dic[(r+dh, c+dw)] += 1
            
vals = Counter(dic.values())

for i in range(10):
    if i == 0:
        print((h-2)*(w-2) - sum(vals.values()))
    else:
        print(vals[i])