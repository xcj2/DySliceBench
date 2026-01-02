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
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = rip()

    for i in range(1000):
        s = str(i)
        if len(s) != N: continue
        chk = True
        for j in range(M):
            chk &= s[S[j] - 1] == str(C[j])
        if chk:
            print(i)
            sys.exit(0)
    
    print(-1)


if __name__ == "__main__":
    main()
