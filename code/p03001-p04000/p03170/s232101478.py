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
a = list(li())
dp = [-1]*(k+1)
dp[0] = 0

for m in range(1,k+1):
    for ai in a:
        if m - ai >= 0:
            if dp[m-ai] == 0:
                dp[m] = 1
                break
    
        dp[m] = 0
    
print("First") if dp[k] == 1 else print("Second")