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
    h = Intl()
    dp = [10000]*n
    dp[0] = 0
    dp[1] = abs(h[1]-h[0])
    for i in range(2,n):
        dp[i] = min(dp[i-1] + abs(h[i]-h[i-1]),\
        dp[i-2] + abs(h[i]-h[i-2]))
    print(dp[-1])