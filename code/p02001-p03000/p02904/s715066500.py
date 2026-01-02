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
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,k=map(int,input().split())
p=list(map(int,input().split()))

class SegminTree:
    # init_valはseg木にしたいlist、ide_eleは単位元
    # """
    # 単位元の説明
    # 最小値のセグ木 → 10**9　(最小値の更新に影響しないため)
    # 　　和のセグ木 → 0　(上の単位元の説明を参照)
    # 　　積のセグ木 → 1　(上の単位元の説明を参照)
    # 　　gcdのセグ木 → 0　(gcdを更新しない値は0)
    # """
    def __init__(self, init_val, ide_ele):
        self.ide_ele=ide_ele
        self.num=2**(len(init_val)-1).bit_length()
        self.seg=[self.ide_ele]*2*self.num

        #set_val
        for i in range(len(init_val)):
            self.seg[i+self.num-1]=init_val[i]
        #built
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2])

    # 書け
    def segfunc(self, x, y):
        return min(x,y)
    
    def update(self, k, x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])

    def query(self, p, q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfunc(res,self.seg[p])
            if q&1 == 1:
                res = self.segfunc(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res,self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
        return res

class SegmaxTree:
    # init_valはseg木にしたいlist、ide_eleは単位元
    # """
    # 単位元の説明
    # 最小値のセグ木 → 10**9　(最小値の更新に影響しないため)
    # 　　和のセグ木 → 0　(上の単位元の説明を参照)
    # 　　積のセグ木 → 1　(上の単位元の説明を参照)
    # 　　gcdのセグ木 → 0　(gcdを更新しない値は0)
    # """
    def __init__(self, init_val, ide_ele, func):
        self.ide_ele=ide_ele
        self.num=2**(len(init_val)-1).bit_length()
        self.seg=[self.ide_ele]*2*self.num
        self.func=func

        #set_val
        for i in range(len(init_val)):
            self.seg[i+self.num-1]=init_val[i]
        #built
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2])

    # 書け
    def segfunc(self, x, y):
        return self.func(x,y)
    
    def update(self, k, x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])

    def query(self, p, q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfunc(res,self.seg[p])
            if q&1 == 1:
                res = self.segfunc(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res,self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
        return res

segmin=SegminTree(p,10**9)
segmax=SegmaxTree(p,0,max)

lst=[]
for i in range(n-k+1):
    tmp1=segmin.query(i,k+i)
    tmp2=segmax.query(i,k+i)
    lst.append((tmp1,tmp2))
# print(lst)

ans=1
for i in range(n-k):
    # print(lst[i][0],p[i])
    # print(lst[i+1][1],p[i+k])
    if lst[i][0]==p[i] and lst[i+1][1]==p[i+k]:
        continue
    else:
        ans+=1
# print(ans)

cnt=1
cnt2=0
flag=0
for i in range(n-1):
    if p[i]<p[i+1]:
        if flag==1:
            continue
        else:
            cnt+=1
    else:
        cnt=1
        flag=0
    if cnt>=k:
        cnt2+=1
        flag=1
# print(cnt2)
if cnt2>=2:
    print(ans-cnt2+1)
else:
    print(ans)