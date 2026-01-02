from heapq import heappush, heappop
import re
from collections import deque
import sys
input = sys.stdin.readline


def int_raw():
    return int(input())


def ss_raw():
    return input().split()


def ints_raw():
    return tuple(map(int, ss_raw()))


DIV = 10**9+7


def mod_invs(n, mod=DIV):
    inv = [0]*(n+1)
    inv[0] = 1
    inv[1] = 1
    for i in range(2, n+1):
        inv[i] = (-(mod//i)*inv[mod % i]) % mod
    return inv


N,A,B,C,D = ints_raw()
S = input()
#N = int_raw()


def main():
    ans = 0
    if D==C:
        return "No"
    if S[D-1]=="#" or S[C-1]=="#":
        return "No"
    if "##" in S[A:max(B, D)]:
        return "No"
    if D>C:
        return "Yes"
    else:
        if "..." in S[B-2:min(min(D+1,N),C)]:
            #print(S[B-2:min(min(D+1, N), C)])
            return "Yes"
        return "No" 
    return ans


print(main())
