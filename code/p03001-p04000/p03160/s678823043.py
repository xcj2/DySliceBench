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
h = list(li())

cost = [float("inf")]*(n)
cost[0] = 0

for i in range(n-1):
    if i == n-2:
        cost[i+1] = min(cost[i+1],
                        cost[i] + abs(h[i+1]-h[i]))
        
    else:
        cost[i+1] = min(cost[i+1],
                        cost[i] + abs(h[i+1]-h[i]))
        cost[i+2] = min(cost[i+2],
                        cost[i] + abs(h[i+2]-h[i]))
        
print(cost[-1])
        