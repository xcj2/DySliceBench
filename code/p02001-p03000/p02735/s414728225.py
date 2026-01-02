#!/usr/bin/env python3
import sys
# input = sys.stdin.r/eadline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    H,W = MAP()
    s = [input() for _ in range(H)]
    dp = [[0]*W for _ in range(H)]

    if s[0][0] == "#":
        dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if i == 0:
                if j == 0:
                    continue

                if s[i][j] == "#" and s[i][j-1] == ".":
                    dp[i][j] = dp[i][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1] 
            else:
                if j == 0:
                    if s[i-1][j] == "." and s[i][j] == "#":
                        up = dp[i-1][j]+1
                    else:
                        up = dp[i-1][j]
                    dp[i][j] = up
                    continue
                else:
                    if s[i-1][j] == "." and s[i][j] == "#":
                        up = dp[i-1][j]+1
                    else:
                        up = dp[i-1][j]
                    
                    if s[i][j-1] == "." and s[i][j] == "#":
                        left = dp[i][j-1]+1
                    else:
                        left = dp[i][j-1]
                    
                    dp[i][j] = min(left,up)

    print(dp[H-1][W-1])

if __name__ == '__main__':
    main()
