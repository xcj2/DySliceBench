from heapq import heappush, heappop
import re
from collections import deque
import sys
import math
input = sys.stdin.readline


def int_raw():
    return int(input())


def ss_raw():
    return input().split()


def ints_raw():
    return tuple(map(int, ss_raw()))


DIV = 10**9+7


def mod_inv_prime(a, mod=DIV):
    return pow(a, mod-2, mod)


def mod_inv(a, b):
    r = a
    w = b
    u = 1
    v = 0
    while w != 0:
        t = r//w
        r -= t*w
        r, w = w, r
        u -= t*v
        u, v = v, u
    return (u % b+b) % b


def ncr(n, r, mod=DIV):
	r = min(r, n-r)
	ret = 1
	for i in range(1, r+1):
		ret = ret * (n-i+1) % mod
		ret = ret * mod_inv(i, mod) % mod
	return ret


def main():
    S = input().rstrip("\n")
    dp = [[0 for i in range(13)] for i in range(len(S)+1)]
    dp [0][0] = 1
    modi = 1%13
    for i in range(1,len(S)+1):
        
        s = S[len(S)-i]
        if s!= '?':
            mod_q = (int(s)*modi)%13
            for k in range(13):
                dp[i][(k+mod_q) % 13] = (dp[i][(k+mod_q) % 13]+dp[i-1][k]) % DIV
        else:
            for j in range(10):
                mod_q = (j*modi) % 13
                for k in range(13):
                    dp[i][(k+mod_q) % 13] = (dp[i]
                                             [(k+mod_q) % 13]+dp[i-1][k]) % DIV
        modi = (modi*10)%13
    return dp[len(S)][5]
print(main())
