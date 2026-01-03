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

from itertools import permutations

n,m = li()
graph = [[False]*n for _ in range(n)]

for _ in range(m):
    a,b = li_()
    graph[a][b] = True
    graph[b][a] = True
    
cands = list(permutations([i for i in range(1,n)]))

ans = 0

for c in cands:
    cand = [0] + list(c)
    ok = True
    for i in range(n-1):
        if not graph[cand[i+1]][cand[i]]:
            ok = False
    
    if ok:   
        ans += 1
    
print(ans)