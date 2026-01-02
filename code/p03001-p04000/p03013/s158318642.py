#create date: 2020-07-25 09:13

import sys
stdin = sys.stdin
mod = 10**9+7

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n, m = na()
    a = [0] * (10**5+1)
    for i in range(m):
        st = ni()
        a[st] = 1

    dp = [0] * (10**5+1)
    dp[0] = 1
    if a[1] == 0: dp[1] = 1
    for i in range(2, n+1):
        if a[i] == 1:
            dp[i] = 0
        else:
            dp[i] = (dp[i-2] + dp[i-1]) % mod
    print(dp[n])

if __name__ == "__main__":
    main()