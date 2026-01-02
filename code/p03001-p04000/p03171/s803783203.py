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
a = list(li())

dp = [[0]*(n+1) for _ in range(n+1)]

for length in range(1,n+1):
    for stidx in range(n-length+1):
        # 次郎の手番
        if(n-length)%2:
            dp[stidx][stidx+length] = min(dp[stidx+1][stidx+length] - a[stidx],
                                          dp[stidx][stidx+length-1] - a[stidx+length-1])
        # 太郎の手番
        else:
            dp[stidx][stidx+length] = max(dp[stidx+1][stidx+length] + a[stidx],
                                          dp[stidx][stidx+length-1] + a[stidx+length-1])
            
print(dp[0][n])