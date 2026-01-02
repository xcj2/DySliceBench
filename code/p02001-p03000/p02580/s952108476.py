import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

h,w,m=map(int,input().split())
hw=[list(map(int,input().split())) for i in range(m)]

hlst=[[0,i] for i in range(h)]    
wlst=[[0,i] for i in range(w)]
dic={}
for i in range(m):
    hh,ww=hw[i]
    hlst[hh-1][0]-=1
    wlst[ww-1][0]-=1
    dic[(hh-1,ww-1)]=1

hlst.sort()
wlst.sort()
hkouho=[]
wkouho=[]
mi=0
for i in range(h):
    if mi<hlst[i][0]:
        break
    hkouho.append(hlst[i][1])
    mi=hlst[i][0]
mi=0
for i in range(w):
    if mi<wlst[i][0]:
        break
    wkouho.append(wlst[i][1])
    mi=wlst[i][0]
# print(hkouho)
# print(wkouho)
# print(hlst)
for i in range(len(hkouho)):
    for j in range(len(wkouho)):
        if not (hkouho[i],wkouho[j]) in dic:
            print(-hlst[0][0]-wlst[0][0])
            exit()
print(-hlst[0][0]-wlst[0][0]-1)
# print(hkouho[0],wkouho[0])