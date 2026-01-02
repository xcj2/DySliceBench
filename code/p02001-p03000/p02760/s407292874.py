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
    A = [ria() for _ in range(3)]
    N = ri()
    B = [ri() for _ in range(N)]
    d = set()
    for n in B: d.add(n)

    for i in range(3):
        cnt = 0
        for j in range(3):
            if A[i][j] in d: cnt += 1
        if cnt == 3:
            print("Yes")
            sys.exit(0)
    for j in range(3):
        cnt = 0
        for i in range(3):
            if A[i][j] in d: cnt += 1
        if cnt == 3:
            print("Yes")
            sys.exit(0)

    if A[0][0] in d and A[1][1] in d and A[2][2] in d:    
            print("Yes")
            sys.exit(0)
    if A[0][2] in d and A[1][1] in d and A[2][0] in d:    
            print("Yes")
            sys.exit(0)

    print("No")

if __name__ == "__main__":
    main()
    
