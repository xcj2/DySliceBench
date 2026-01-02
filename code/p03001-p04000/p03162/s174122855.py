import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**8) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n = ni()
abc = [list(li()) for _ in range(n)]

dp = [[0]*3 for _ in range(n+1)]

for day in range(n):
    ai,bi,ci = abc[day]
    dp[day+1][0] = max(dp[day][1], dp[day][2]) + ai
    dp[day+1][1] = max(dp[day][2], dp[day][0]) + bi
    dp[day+1][2] = max(dp[day][0], dp[day][1]) + ci
    
print(max(dp[n]))