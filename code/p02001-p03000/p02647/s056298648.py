import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(500000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]


def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    # if sum(a)==0:
    #     print(*a)
    #     quit()
    while k:
        lst=[1]*n
        dic={}
        cnt=0
        for i in range(n):
            lst[i]+=cnt
            if i in dic:
                cnt-=dic[i]
            if a[i]>0:
                if not i+a[i] in dic:
                    dic[i+a[i]]=1
                else:
                    dic[i+a[i]]+=1
                cnt+=1

        dic={}
        cnt=0
        for i in range(n)[::-1]:
            lst[i]+=cnt
            if i in dic:
                cnt-=dic[i]
            if a[i]>0:
                if not i-a[i] in dic:
                    dic[i-a[i]]=1
                else:
                    dic[i-a[i]]+=1
                cnt+=1
        k-=1
        if sum(lst)==n*n:
            break
        # print(k)
        a=lst[:]

    print(*lst)

main()