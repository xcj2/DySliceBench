import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():


    n, w = LI()
    weight = [0 for _ in range(n+1)]
    value = [0 for _ in range(n+1)]

    for i in range(1,n+1):
        weight[i], value[i] = LI()


    dp = [[float("inf") for _ in range(sum(value)+1)]  for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(len(dp[0])):
            if j < value[i+1]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = min(dp[i][j], dp[i][j-value[i+1]] + weight[i+1])

    ans = 0
    for i in range(len(dp[n])):
        if dp[n][i] <= w:
            ans = i
    
    print(ans)
main()
