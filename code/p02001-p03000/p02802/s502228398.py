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
    N, M = rip()
    P = [0] * M
    S = [""] * M
    for i in range(M):
        ss = rsa()
        P[i] = int(ss[0]) - 1
        S[i] = ss[1]
    
    accept = [False] * N
    penalty = [0] * N
    for i in range(M):
        if S[i] == 'AC':
            accept[P[i]] = True
            continue
        if not accept[P[i]]:
            penalty[P[i]] += 1
    
    ac_count = 0
    penalty_count = 0
    for i in range(N):
        if accept[i]:
            ac_count += 1
            penalty_count += penalty[i]
    
    print("{0} {1}".format(ac_count, penalty_count))



if __name__ == "__main__":
    main()
