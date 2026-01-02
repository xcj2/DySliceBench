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

     
def main():
    N = I()

    h = LI()
    cnt = 0

    def dec_h(l, r):
        nonlocal cnt
        nonlocal h
        if l > r:
            return
        min_h = min(h[l:r+1])
        # print('l: {}, r: {}, min_h: {}'.format(l, r, min_h))
        for j in range(l, r+1):
            h[j] -= min_h
        cnt += min_h
        st = l
        en = r
        # print('h: {}'.format(h))
        for i in range(l, r+1):
            if h[i] == 0:
                en = i-1
                dec_h(st, en)
                st = i+1
            if i == r and st < r+1:
                dec_h(st, r)
    dec_h(0, N-1)
    print(cnt)

main()

