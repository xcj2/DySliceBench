from sys import stdin
import sys
import numpy as np
import collections
from functools import cmp_to_key
import heapq

##  input functions for me
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def rip(sep = ''):
    if sep == '' :
        return map(int, input().split()) 
    else: return map(int, input().split(sep))
def ria(sep = ''): 
    return list(rip(sep))
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##
def main():
    N = rs()
    K = ri()
    a = [int(c) for c in N]
    dp = [[0] * (K + 1) for i in range(2)]

    dp[1][0] = 1
    dp[1][1] = a[0] - 1
    dp[0][1] = 1

    for i in range(1,len(a)):
        ndp = [[0] * (K + 1) for i in range(2)]

        for k in range(K+1):
            if k + 1 <= K:
                ndp[1][k + 1] += 9 * dp[1][k] # 1 ~ 9
            ndp[1][k] += dp[1][k] # 0
        
        for k in range(K+1):
            if a[i] == 0:
                ndp[0][k] += dp[0][k] #0
            else:
                ndp[1][k] += dp[0][k] #0
                if k + 1 <= K:
                    ndp[1][k + 1] += (a[i] - 1) * dp[0][k] # 1 ~ (a[i]-1)
                    ndp[0][k + 1] += dp[0][k]
        
        dp = ndp
    print(dp[0][K] + dp[1][K])
    


if __name__ == "__main__":
    main()
