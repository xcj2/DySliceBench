import sys
from collections import defaultdict
input = sys.stdin.readline
mod = 998244353
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return [w[0],w[1]]
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return ( m + x%m ) % m
def main():
    n,s = map(int,input().split())
    a = list(map(int, input().split()))
    dp = [[0 for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = pow(2,n,mod)
    MODINV2 = mod_inv(2,mod)
    ans = 0
    for i in range(n):
        for j in range(s,-1,-1):
            if j-a[i] < 0:
                continue
            dp[i+1][j] += dp[i][j-a[i]]*MODINV2
            dp[i+1][j] %= mod
        for j in range(s,-1,-1):
            if j == s:
                ans += dp[i+1][j]
                ans %= mod
            else:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= mod
    print(ans)
if __name__ == "__main__":
    main()