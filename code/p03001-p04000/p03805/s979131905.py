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

from itertools import permutations

# 全探索をするのです
n,m = li()
edges = set()
for _ in range(m):
    a,b = li()
    edges.add((a,b))
    edges.add((b,a))
    
paths = permutations([str(i) for i in range(2,n+1)],n-1)
cnt = 0
for path in paths:
    path = [1] + [int(i) for i in path]
    
    exist = True
    for i in range(n-1):
        if not (path[i], path[i+1]) in edges:
            exist = False

    if exist:
        cnt += 1
        
print(cnt)