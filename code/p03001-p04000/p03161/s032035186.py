import sys
import math
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":
    n ,k = I2()
    h = Intl()
    dp = [float("inf")]*n
    dp[0] = 0
    for i in range(1,n):
        for j in range(max(0,i-k),i):
            dp[i] = min(dp[i],dp[j]+abs(h[i]-h[j]))
    print(dp[-1])