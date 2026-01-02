from sys import stdin
import sys
import numpy as np
import collections
from functools import cmp_to_key

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
    N, A, B = rip()
    if (B - A) % 2 == 0:
        print((B - A) // 2)
    else :
        a = A
        b = B
        l = 0
        l += a - 1
        b -= a - 1
        a -= a - 1
        l += 1
        b -= 1
        l += (b - a) // 2
        
        a = A
        b = B
        r = 0
        r += N - b
        a += N - b
        b += N - b
        r += 1
        a += 1
        r += (b - a) // 2
        print(min(l, r))




if __name__ == "__main__":
    main()
