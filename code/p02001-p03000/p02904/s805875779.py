import sys
sys.setrecursionlimit(10**7) #再帰関数の上限,10**5以上の場合python
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
from functools import lru_cache#pypyでもうごく
#@lru_cache(maxsize = None)#maxsizeは保存するデータ数の最大値、2**nが最も高効率

def input(): return sys.stdin.readline()[:-1]
def printl(li): print(*li, sep="\n")
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

class BIT():#添字は1から始まることに注意
    def __init__(self, max_n):
        self.size = max_n + 1
        self.tree = [0] * self.size
        self.depth = self.size.bit_length()
        
    def initialize(self,seq):
        tree = self.tree
        size = self.size
        for i,x in enumerate(seq,1):
            tree[i] += x
            j = i+(i&(-i))
            if j < size:
                tree[j] += tree[i]
        
    def __repr__(self):
        return self.tree.__repr__()
        
    def get_sum(self,i):
        tree = self.tree
        s = 0
        while i:
            s += tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        tree = self.tree
        size = self.size
        while i < size:
            tree[i] += x
            i += i & -i
    
    def find_kth_element(self,k):#k番目（最小は１）の要素
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
    mod = 10**9+7
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    #N = int(input())
    N, K = map(int, input().split())
    Ps = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    bit=BIT(N+1)
    sc=1
    tot=0
    j=0
    cur=Ps[0]
    flag=1
    cur=Ps[0]
    it=0
    for i,p in enumerate(Ps[:K]):
        if cur>p:
            it=i
        bit.add(p+1,1)
        cur=p
    
    count=0
    if it ==0:
        count=1

    for i in range(N-K+1):
        j=i+K-1

        tot+=sc
        if i==N-K:
            break
        a=Ps[i]
        b=Ps[i+K]
        if bit.find_kth_element(1)==a+1 and bit.find_kth_element(K)<=b+1:
            sc=0
        else:
            sc=1
        bit.add(a+1,-1)
        bit.add(b+1,1)

        j=i+K
        if Ps[j-1]>Ps[j]:
            it=j
        elif j-it+1>=K:
            #print(it,j)
            if count>0:
                sc=0
            else:
                count=1
        cur=Ps[j]
    print(tot)


if __name__ == "__main__":
    main()