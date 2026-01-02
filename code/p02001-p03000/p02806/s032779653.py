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
    N = ri()
    S = ["a"] * N
    T = [0] * N
    for i in range(N):
        ss = rsa()
        S[i] , T[i] = ss[0], int(ss[1])
    X = rs()

    ans = 0
    sleep = False
    for i in range(N):
        if S[i] == X:
            sleep = True
            continue
        if sleep:
            ans += T[i]
    
    print(ans)


if __name__ == "__main__":
    main()
