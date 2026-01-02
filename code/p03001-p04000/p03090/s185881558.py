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

n = ni()

a = [i for i in range(1,101)]
acc = list(accumulate(a))

if n%2:
    groups = [[i, n-i] for i in range(1,(n+1)//2)]
    groups.append([n])
else:
    groups = [[i, n-i+1] for i in range(1,n//2 + 1)]
    
edges = []

for i in range(len(groups)):
    for j in range(len(groups[i])):
        for k in range(1,n+1):
            if k in groups[i] or groups[i][j] > k:
                continue
            
            else:
                edges.append([groups[i][j], k])
                
print(len(edges))
for ei in edges:
    print(*ei)