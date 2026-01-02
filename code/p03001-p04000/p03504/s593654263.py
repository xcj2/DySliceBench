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

N,C = li()
MAX = 10**5

stc = []
for _ in range(N):
    stc.append(list(li()))
    
rec = [[0 for _ in range(MAX+1)] for _ in range(C)]
for s,t,c in stc:
    rec[c-1][s-1] += 1
    rec[c-1][t] -= 1
    
for i in range(C):
    rec[i] = list(accumulate(rec[i]))
    rec[i] = [min(1,reci) for reci in rec[i]]
    
rec_total = rec[0]
    
for i in range(1,C):
    for j in range(MAX+1):
        rec_total[j] = rec_total[j] + rec[i][j]

print(max(rec_total))