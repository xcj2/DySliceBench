from heapq import heappush,heappop
import queue
import re
import math
import functools


def i_raw():
    return int(input())

def ss_raw():
    return input().split()

def is_raw():
    return list(map(int, ss_raw()))

INF = 1<<29

def make1d_arr(n,val=INF):
    return [val for i in range(n)]

def make2d_arr(h,w,val =INF):
    return [[val for i in range(w)]for i in range(h)]

def gcd (a,b):
    if(b==0):
        return a
    return gcd(b,a%b)


def main():
    S,T = ss_raw()
    A,B = is_raw()
    U = input().strip()
    if U==S:
        return " ".join(map(str,[A-1,B]))
    else:
        return " ".join(map(str,[A,B-1]))  


print(main())
