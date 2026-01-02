import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():

    mod = 998244353
    n, k = LI()
    l = [0 for _ in range(k)]
    r = [0 for _ in range(k)]

    for i in range(k):
        l[i], r[i] = LI()

    dp = [0 for _ in range(n+1)]      
    dpsum = [0 for _ in range(n+1)]
    dp[1], dpsum[1] = 1, 1

    for i in range(2,n+1):
        for el, er in zip(l, r):
            dp[i] += dpsum[max(i-el, 0)] - dpsum[max(i-er-1, 0)]
        dp[i] %= mod
        dpsum[i] = (dpsum[i-1] + dp[i])%mod

    print(dp[n])

main()
