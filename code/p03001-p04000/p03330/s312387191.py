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

from collections import Counter

n,c = li()
diff = [list(li()) for _ in range(c)]
init = [list(li_()) for _ in range(n)]

group = [Counter() for _ in range(3)]

for row in range(n):
    for col in range(n):
        group[(row+col)%3][init[row][col]] += 1
        
ans = 10**18

for c0 in range(c):
    cost = [0,0,0]
    for k,v in group[0].items():
        cost[0] += v*diff[k][c0]

        
    for c1 in range(c):
        if c0 == c1:
            continue
        
        cost[1] = 0
        
        for k,v in group[1].items():
            cost[1] += v*diff[k][c1]
            
        for c2 in range(c):
            if c2 == c0 or c2 == c1:
                continue
            
            cost[2] = 0
            
            for k,v in group[2].items():
                cost[2] += v*diff[k][c2]
                
            ans = min(ans, sum(cost))
            
print(ans)