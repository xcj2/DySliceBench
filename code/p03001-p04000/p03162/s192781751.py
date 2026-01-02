import sys
import math
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":
    n = I()
    a = [Intl() for _ in range(n)]
    dp = [[0,0,0] for _ in range(n+1)]
    for i in range(n):
        for j in range(3):
            for k in range(3):
                if j == k:pass
                else:
                    dp[i+1][k] = max(dp[i+1][k],dp[i][j] + a[i][k])
    print(max(dp[-1]))