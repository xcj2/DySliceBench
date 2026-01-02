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

def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reverse=True)  #二個目の要素で降順並び替え

    #N = int(input())
    H,W = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    S = tuple(input() for i in range(H)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    
    n=H*W
    inf=10000000

    def warshall_floyd():#n^3, 処理が軽いので多少ギリギリでも通る
        #d[i][j]: iからjへの最短距離
        #初期化
        d = [[inf]*n for i in range(n)] 
        for i in range(H):
            for j in range(W):
                if S[i][j]!=".":
                    continue
                for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if 0<=ni<H and 0<=nj<W and S[ni][nj]==".":
                        d[i*W+j][ni*W+nj]=1
                        
        for i in range(n):
            d[i][i] = 0 #自身のところに行くコストは０
        for k in range(n):
            for i in range(n):
                for j in range(i+1,n):#無向グラフ,有向グラフの場合はrange(0,n)
                    x = min(d[i][j],d[i][k] + d[k][j])
                    d[i][j]=x
                    d[j][i]=x#無向グラフの場合
                # if i==j and d[i][i]<0: #負閉路がある場合
                #     return -1
        return d

    d=warshall_floyd()
    ans=0
    for i in range(H):
        for j in range(W):
            if S[i][j]!=".":
                continue
            for ni in range(H):
                for nj in range(W):
                    if d[i*W+j][ni*W+nj]<inf:
                        ans=max(ans,d[i*W+j][ni*W+nj])
    print(ans)
if __name__ == "__main__":
    main()