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
    s, t = rsa()
    a, b = ria()
    u = rs()
    if s == u: a -= 1
    if t == u: b -= 1
    print("{0} {1}".format(a,b))


if __name__ == "__main__":
    main()
