import sys
sys.setrecursionlimit(10**7) #再帰関数の上限,10**5以上の場合python
import math
from copy import copy, deepcopy
from copy import deepcopy as dcp
from operator import itemgetter
from bisect import bisect_left, bisect, bisect_right#2分探索
#bisect_left(l,x), bisect(l,x)#aはソート済みである必要あり。aの中からx未満の要素数を返す。rightだと以下
from collections import deque, defaultdict
#deque(l), pop(), append(x), popleft(), appendleft(x)
#q.rotate(n)で → にn回ローテート
from collections import Counter#文字列を個数カウント辞書に、
#S=Counter(l),S.most_common(x),S.keys(),S.values(),S.items()
from itertools import accumulate,combinations,permutations,product#累積和
#list(accumulate(l))
from heapq import heapify,heappop,heappush
#heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone
from functools import reduce,lru_cache#pypyでもうごく
#@lru_cache(maxsize = None)#maxsizeは保存するデータ数の最大値、2**nが最も高効率
from decimal import Decimal
from argparse import ArgumentParser

args=ArgumentParser()
args.add_argument('-loc', '--local', type=bool,default=False)
LOCAL=args.parse_args().local

def input(): 
    x=sys.stdin.readline(); 
    if x[-1]=="\n": 
        return x.rstrip() 
    return x
    
def printe(*x):_=print("## ",*x,file=sys.stderr) if LOCAL else 0
def printl(li): _=print(*li, sep="\n") if li else None
def argsort(s, return_sorted=False): 
    inds=sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted: return inds, [s[i] for i in inds]
    return inds
def alp2num(c,cap=False): return ord(c)-97 if not cap else ord(c)-65
def num2alp(i,cap=False): return chr(i+97) if not cap else chr(i+65)
def matmat(A,B):
    K,N,M=len(B),len(A),len(B[0])
    return [[sum([(A[i][k]*B[k][j]) for k in range(K)]) for j in range(M)] for i in range(N)]
def matvec(M,v):
    N,size=len(v),len(M)
    return [sum([M[i][j]*v[j] for j in range(N)]) for i in range(size)]
def T(M):
    n,m=len(M),len(M[0])
    return [[M[j][i] for j in range(n)] for i in range(m)]
def binr(x): return bin(x)[2:]
def bitcount(x): #xは64bit整数
    x= x - ((x >> 1) & 0x5555555555555555)
    x= (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x= (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f 
    x+= (x >> 8); x+= (x >> 16); x+= (x >> 32) 
    return x & 0x7f
INF=10**18

class segtree():#seg=segtree(A),単位元とsegfuncを指定すること
    def __init__(self,A,ide=INF):#単位元とsegfuncを指定すること
        n=len(A)
        num=2**(n-1).bit_length()#n以上の最小の2のべき乗
        seg=[ide]*(2*num-1)
        segfunc=self.segfunc
        self.ide,self.n,self.num,self.seg = ide, n, num, seg
        for i in range(n): seg[i+num-1]=A[i]#setvalue
        for i in range(num-2,-1,-1):seg[i]=segfunc(seg[2*i+1],seg[2*i+2])#build
    
    def segfunc(self,x,y):return min(x,y) #seg木の基本関数
    
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

class BIT():#添字は1から始まることに注意
    def __init__(self, max_n):
        self.size = max_n + 1
        self.tree = [0] * self.size
        self.depth = self.size.bit_length()
        self.tot=0
        
    def initialize(self,seq):
        tree = self.tree
        size = self.size
        self.tot=0
        for i,x in enumerate(seq,1):
            self.tot+=x
            tree[i] += x
            j = i+(i&(-i))
            if j < size:
                tree[j] += tree[i]
        
    def __repr__(self):
        return self.tree.__repr__()
        
    def sum(self,i):
        tree = self.tree
        s = 0
        while i:
            s += tree[i]
            i -= i & -i
        return s
 
    def add(self, i, val):
        tree = self.tree
        size = self.size
        while i < size:
            tree[i] += val
            i += i & -i
        self.tot+=val
    
    def find(self,k):#k番目（最小は１）の要素,使うときは数列のサイズとbitのサイズを合わせること
        if k>self.tot: return self.size
        tree = self.tree; size = self.size
        x,sx = 0,0
        dx = 1 << (self.depth)
        for i in range(self.depth - 1, -1, -1):
            dx = (1 << i)
            if x + dx >= size:
                continue
            y = x + dx
            sy = sx + tree[y]
            if sy < k:
                x,sx = y,sy
        return x + 1

def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reverse=True)  #二個目の要素で降順並び替え

    #N = int(input())
    H,W = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    S = tuple(tuple(map(int, input().split())) for i in range(H)) #改行行列
    seg=segtree([0]*W)
    bit=BIT(W)
    bit.initialize([1]*W)

    for i in range(H):
        a,b=S[i]
        a-=1;b-=1
        if a==0 and b==W-1:
            for _ in range(i-H):
                print(-1)
                return
        
        if b==W-1:
            l=bit.sum(a)
            r=bit.sum(b+1)
            #printe(l,r)
            aset=[]
            for j in range(l+1,r+1):
            
                ind=bit.find(j)-1
                aset.append(ind)
            for j in aset:
                seg.update(j,INF)
                bit.add(j+1,-1)
        else:
            cur0=seg.query(b+1,b+2)
            cur=cur0
            l=bit.sum(a)
            r=bit.sum(b+1)
            aset=[]
            #printe(a,b,l,r)
            for j in range(l+1,r+1):
                ind=bit.find(j)-1
                aset.append(ind)
                #printe(ind)
                cur=min(cur,seg.query(ind,ind+1)+(b+1-ind))
            #printe(l,r)
            for j in aset:
                bit.add(j+1,-1)
                seg.update(j,INF)
            
            seg.update(b+1,cur)
            if cur<INF and cur0>=INF:
                bit.add(b+2,1)
        ans=INF
        if a>0:
            ans=min(ans,seg.query(0,a))
        if b<W-1:
            ans=min(ans,seg.query(b+1,W))
        if ans>=INF:
            print(-1)
        else:
            print(ans+i+1)


if __name__ == "__main__":
    main()