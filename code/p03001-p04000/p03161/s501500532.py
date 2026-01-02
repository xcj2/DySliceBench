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

n,k = li()
h = list(li())

cost = [float("inf")]*(n)
cost[0] = 0

for i in range(n-1):
    cnt = 1
    while i+cnt < n and cnt <= k:
        cost[i+cnt] = min(cost[i+cnt],
                          cost[i] + abs(h[i+cnt]-h[i]))
        
        cnt += 1
             
print(cost[-1])