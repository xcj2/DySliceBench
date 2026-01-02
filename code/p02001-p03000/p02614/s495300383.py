import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def gen_comb(n):
    c = []
    for i in range(n):
        for comb in itertools.combinations([j for j in range(n)], i):
            c.append(list(comb))
    return c

def count(C, arr1, arr2):
    n_row = len(C)
    n_col = len(C[0])
    s1 = set(arr1)
    s2 = set(arr2)
    cnt = 0
    for r in range(n_row):
        for c in range(n_col):
            if r in s1:
                continue
            if c in s2:
                continue
            if C[r][c] == '#':
                cnt += 1
    return cnt

def main():
    H, W, K = LI()
    C = []
    for i in range(H):
        C.append(S())

    h_comb = gen_comb(H)
    w_comb = gen_comb(W)
    cnt = 0
    for ixs in h_comb:
        for jxs in w_comb:
            if count(C, ixs, jxs) == K:
                cnt += 1
    print(cnt)


main()

