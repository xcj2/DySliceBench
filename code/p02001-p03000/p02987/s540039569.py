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


def main():
    S = input().strip("\n")
    if len(set(S))==2 and S.count(S[0])==2:
        return "Yes"
    return "No"


print(main())
