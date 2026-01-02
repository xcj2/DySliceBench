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

n,m,q = li()
train = []
query = []

field = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    train.append(tuple(li()))
    
for _ in range(q):
    query.append(tuple(li()))
    
for ts, tt in train:
    field[ts][tt] += 1
    
for r in range(n+1):
    for c in range(n):
        field[r][c+1] += field[r][c]
        
for c in range(n+1):
    for r in range(n):
        field[r+1][c] += field[r][c]
        
for qs,qt in query:
    print(field[qt][qt] - field[qt][qs-1] - field[qs-1][qt] + field[qs-1][qs-1])
    