from heapq import heappush,heappop
import queue
import re
import math
import functools

def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int, ss_raw()))

INF = 1<<29

def make1d_arr(n,val=INF):
    return [val for i in range(n)]

def make2d_arr(h,w,val =INF):
    return [[val for i in range(w)]for i in range(h)]


N = int_raw()
A = ints_raw()


def main():
    numNega = len([a for a in A if a<0])
    numZero = len([a for a in A if a==0])
    absA = list(map(abs,A))
    if numZero >1 or numNega%2 == 0:
        return sum(absA)
    else:
        minAbs = min(absA)
        return sum(absA)-minAbs*2

print(main())
