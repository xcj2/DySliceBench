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

def input(): 
    x=sys.stdin.readline()
    return x[:-1] if x[-1]=="\n" else x
def printe(*x):print("## ",*x,file=sys.stderr)
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
    mod = 998244353
    #w.sort(key=itemgetter(1),reverse=True)  #二個目の要素で降順並び替え

    N = int(input())
    #N, K = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    xs=[]
    ys=[]
    for x,y in S:
        xs.append(x)
        ys.append(y)

    ixsort=argsort(xs)
    iysort=argsort(ys)
    s=[[0,0] for _ in range(N)]

    for i in range(N):
        s[ixsort[i]][0]=i
        s[iysort[i]][1]=i
    
    s.sort()

    xsmall=BIT(N)
    xlarge=BIT(N)
    for i in range(0,N):
        xlarge.add(s[i][1]+1,1)
    
    p2=[0]*(N+1)
    p2[0]=1
    for i in range(1,N+1):
        p2[i]=p2[i-1]*2%mod
    ans=0
    p2n=p2[N]
    for i,(x,y) in enumerate(s):
        xlarge.add(y+1,-1)
        
        lxsy=xlarge.sum(y+1)
        lxly=xlarge.tot-lxsy
        sxsy=xsmall.sum(y+1)
        sxly=xsmall.tot-sxsy

        xsmall.add(y+1,1)
        
        t=1
        t+=p2[lxsy]+p2[lxly]+p2[sxly]+p2[sxsy]-4
        t%=mod
        t+=(p2[lxly+lxsy]-p2[lxly]-p2[lxsy]+1)
        t+=(p2[lxly+sxly]-p2[sxly]-p2[lxly]+1)
        t+=(p2[sxsy+lxsy]-p2[sxsy]-p2[lxsy]+1)
        t+=(p2[sxsy+sxly]-p2[sxsy]-p2[sxly]+1)
        t%=mod
        ans+=p2n-t
        ans%=mod
    print(ans)


        
        



if __name__ == "__main__":
    main()