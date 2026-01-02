import sys
sys.setrecursionlimit(10**6) #再帰関数の上限
import math
from copy import copy, deepcopy
from operator import itemgetter
from bisect import bisect_left, bisect, bisect_right#2分探索
#bisect_left(l,x), bisect(l,x)#aはソート済みである必要あり。aの中からx未満の要素数を返す。rightだと以下
from collections import deque 
#deque(l), pop(), append(x), popleft(), appendleft(x)
##listでqueの代用をするとO(N)の計算量がかかってしまうので注意
from collections import Counter#文字列を個数カウント辞書に、
#S=Counter(l),S.most_common(x),S.keys(),S.values(),S.items()
from itertools import accumulate#累積和
#list(accumulate(l))
from heapq import heapify,heappop,heappush
#heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone
#import fractions#古いatcoderコンテストの場合GCDなどはここからimportする

def input(): return sys.stdin.readline()[:-1]
def printl(li): print(*li, sep="\n")
def argsort(s, return_sorted=False): 
    inds=sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted: return inds, [s[i] for i in inds]
    return inds

class segtree():#seg=segtree(A),単位元とsegfuncを指定すること
    def __init__(self,A,ide=0):#単位元とsegfuncを指定すること
        n=len(A)
        num=2**(n-1).bit_length()#n以上の最小の2のべき乗
        seg=[ide]*(2*num-1)
        segfunc=self.segfunc
        self.ide,self.n,self.num,self.seg = ide, n, num, seg
        for i in range(n): seg[i+num-1]=A[i]#setvalue
        for i in range(num-2,-1,-1):seg[i]=segfunc(seg[2*i+1],seg[2*i+2])#build
    
    def segfunc(self,x,y):return x|y #seg木の基本関数
    
    def update(self,k,x):#Aのk番目の要素をxに置き換える,計算量log(N)
        k += self.num-1
        seg,segfunc=self.seg,self.segfunc
        seg[k] = x
        while k:
            k = (k-1)//2
            seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
    
    def query(self,p,q):#区間[p,q)の累積segfuncを求める,計算量log(N)
        if q<=p: return self.ide
        num,segfunc,seg=self.num,self.segfunc,self.seg
        p += num-1; q += num-2
        res=self.ide
        while q-p>1:
            if p&1 == 0: res = segfunc(res,seg[p])
            if q&1 == 1:
                res = segfunc(res,seg[q])
                q -= 1
            p,q = p//2, (q-1)//2
        if p == q: res = segfunc(res,seg[p])
        else: res = segfunc(segfunc(res,seg[p]),seg[q])
        return res 

def main():
    mod = 10**9+7
    alpha2num = lambda c: 2**(ord(c) - ord('a'))
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    N = int(input())
    S=input()
    #N, K = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    A=list(map(alpha2num, list(S)))
    #print(A)
    #exit()
    seg=segtree(A)
    #print(A)
    Q=int(input())
    for i in range(Q):
        t, a,b =input().split()
        if t=='1':
            a=int(a)
            seg.update(a-1,alpha2num(b))
        else:
            a,b=int(a),int(b)
            x=seg.query(a-1,b)
            count=0
            for i in range(26):
                count+= (x>>i & 1)
            print(count)






if __name__ == "__main__":
    main()