import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

def main():
    a = inpll(3)
    n = inp()
    b = inplm(n)
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                a[i][j] = 0
    for i in range(3):
        flag = True
        for j in range(3):
            if a[i][j] != 0:
                flag = False
        if flag:
            print('Yes')
            return
    for i in range(3):
        flag = True
        for j in range(3):
            if a[j][i] != 0:
                flag = False
        if flag:
            print('Yes')
            return
    flag = True
    for i in range(3):
        if a[i][i] != 0:
            flag = False
    if flag:
        print('Yes')
        return
    flag = True
    for i in range(3):
        if a[i][2-i] != 0:
            flag = False
    if flag:
        print('Yes')
        return
    print('No')
    
if __name__ == "__main__":
    main()