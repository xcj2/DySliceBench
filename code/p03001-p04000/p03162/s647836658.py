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

n = ni()
abc = []
for _ in range(n):
    abc.append(tuple(li()))
    
happiness = [[0]*(n+1) for _ in range(3)]

for i in range(n):
    a,b,c = abc[i]
    
    happiness[0][i+1] = max(happiness[1][i],
                            happiness[2][i]) + a
             
    happiness[1][i+1] = max(happiness[0][i],
                            happiness[2][i]) + b
             
    happiness[2][i+1] = max(happiness[0][i],
                            happiness[1][i]) + c
             
print(max(happiness[0][-1],
          happiness[1][-1],
          happiness[2][-1]))