from collections import *
from itertools import *
from bisect import *
from heapq import *
import copy
import math


#N,K=map(int,input().split())
N=int(input())
S=input()
Q=int(input())
Query=[input().split() for i in range(Q)]

def segfunc(x,y):
    return (x|y)

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=seg[2*i+1]|seg[2*i+2]

def update(k,b):
    k += num-1
    if seg[k]=={b}:
        return ()
    seg[k] = {b}
    while k:
        k = (k-1)>>1
        seg[k] = seg[k*2+1]|seg[k*2+2]

def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=set()
    while q-p>1:
        if p&1 == 0:
            res = res|seg[p]
        if q&1 == 1:
            res = res|seg[q]
            q -= 1
        p = p>>1
        q = (q-1)>>1
    if p == q:
        res = res|seg[p]
    else:
        res = res|seg[p]|seg[q]
    return res

#num:n以上の最小の2のべき乗
n=N
num =2**(n-1).bit_length()
seg=[set()] * (2*num)

for i in range(N):
    seg[i+num-1]={ord(S[i])}
for k in range(num-2,-1,-1):
    seg[k] = seg[k*2+1]|seg[k*2+2]
for type, i, c in Query:
    if type=="1":
        update(int(i)-1,ord(c))
    else:
        print(len(query(int(i)-1,int(c))))
    #print(seg)
