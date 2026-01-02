import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
def main():
    # from math import gcd
    def input():
        return sys.stdin.readline()[:-1]
    def ruiseki(lst):
        return [0]+list(accumulate(lst))
    mod=pow(10,9)+7
    al=[chr(ord('a') + i) for i in range(26)]
    direction=[[1,0],[0,1],[-1,0],[0,-1]]

    h,w=map(int,input().split())
    a=[input() for i in range(h)]

    cnt=0

    itta=[[10**9]*w for i in range(h)]

    d=deque()
    # aaa=d.append
    for i in range(h):
        for j in range(w):
            if a[i][j]=="#":
                d.append((i,j))
                itta[i][j]=0

    # print(d)
    # print(itta)

    while d:
        cnt+=1
        for l in range(len(d)):
            nh,nw=d.popleft()
            for i in range(4):
                d1,d2=direction[i]
                if 0<=nh+d1<h and 0<=nw+d2<w:
                    if itta[nh+d1][nw+d2]==10**9:
                        itta[nh+d1][nw+d2]=cnt
                        d.append((nh+d1,nw+d2))
        # print(d)

    # print(itta)
    print(cnt-1)

if __name__ == '__main__':
    main()