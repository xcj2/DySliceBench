import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
# from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,m,p=map(int,input().split())
abc=[list(map(int,input().split())) for i in range(m)]

#True : 負の経路が存在する
def find_negative_loop1(n,w,es):
    #負の経路の検出
    #n:頂点数, w:辺の数, es[i]: [辺の始点,辺の終点,辺のコスト]
    d = [float("inf")] * n
    d[0] = 0
    infdic=defaultdict(int)
    #この始点はどこでもよい
    for i in range(n):
        for j in range(w):
            e = es[j]
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                if i == n-1:
                    infdic[e[0]]=1
    return infdic

def find_negative_loop2(n,w,es,infd):
    #負の経路の検出
    #n:頂点数, w:辺の数, es[i]: [辺の始点,辺の終点,辺のコスト]
    d = [float("inf")] * n
    d[0] = 0
    for i in infd.keys():
        d[i]=-float('inf')
    #この始点はどこでもよい
    for i in range(n):
        for j in range(w):
            e = es[j]
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                # if i == n-1:
                #     return True
    return d


#############################
w = m
es = [[] for i in range(w)] #es[i]: [辺の始点,辺の終点,辺のコスト]
for i in range(w):
    x,y,z = abc[i]
    es[i] = [x-1,y-1,p-z]
# w = w*2
# print(es)

tmp=find_negative_loop1(n,w,es)
# print(tmp)
tmp2=find_negative_loop2(n,w,es,tmp)
# print(tmp2)
if tmp2[-1]==-float('inf'):
    print(-1)
else:
    print(-min(tmp2[-1],0))