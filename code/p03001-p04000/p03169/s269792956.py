#!/usr/bin/env python3
#dp9 #Sushi

import sys
import bisect
input = sys.stdin.readline
def LI(): return list(map(int,input().split()))
def LIR(n): return [LI() for _ in range(n)]

def J():
    n = int(input())
    a = LI()
    a.sort()
    one = bisect.bisect_right(a,1)
    two = bisect.bisect_right(a,2) - one
    three = n - one - two

    #dp[i][j][k] := 残り1個の皿がi枚、2個の皿がj枚、3個の皿がk枚の状態から
    #               寿司をすべてなくすのに必要な操作回数の期待値
    dp = [[[0.0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
    for k in range(three+1):
        for j in range(two+three+1 - k):
            for i in range(one+two+three+1-k-j):
                if i == 0 and j == 0 and k == 0:
                    continue
                tmp = n*1.0
                if i > 0:
                    tmp += i*dp[i-1][j][k]
                if j > 0:
                    tmp += j*dp[i+1][j-1][k]
                if k > 0:
                    tmp += k*dp[i][j+1][k-1]
                dp[i][j][k] = tmp/(i+j+k)
    print(dp[one][two][three])
if __name__ == '__main__':
    J()
