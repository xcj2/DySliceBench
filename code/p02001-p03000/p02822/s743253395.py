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

class rerooting:#全方位木
    def __init__(self,N,edge):#単位元self.unitとモノイドdef func,および親の追加処理def addnode設定すること
        #tot[親]:すべての子の値の累計
        #dics[親][根（親の隣接点)]=その部分木での値
        self.unit=0
        self.edge=edge
        self.par=[-1]*N
        self.N=N
        self.visited=[0]*N
        self.dics=[dict() for _ in range(N)]
        self.ikigake=[]
        self.tot=[self.unit]*N
        self._forward(0)
        

    def func(self,x,y):
        return x+y

    def addnode(self,x):#辺(距離)に関するdpのとき必要
        return x+1

    def _dfs(self,start):
        edge=self.edge
        N=self.N
        par=self.par
        q=deque([(start,start)])
        while len(q):
            e,pa=q.pop()#ここをpopleftにすると幅優先探索BFSになる
            if par[e]!=-1:continue
            par[e]=pa
            self.ikigake.append(e)
            for ne in edge[e]:q.append((ne,e))
        
        for e in reversed(self.ikigake[1:]):
            pa=par[e]
            ans=self.unit
            de=self.dics[e]
            for val in de.values():
                ans=self.func(ans,val)
            self.dics[pa][e]=self.addnode(ans)
    
    def _forward(self,start):
        self._dfs(start)
        for e in self.ikigake:
            pa=self.par[e]
            nes=list(self.dics[e].keys())
            nvals=list(self.dics[e].values())
            l=len(nes)
            aleft=[self.unit]
            aright=[self.unit]
            for i in range(l-1):
                aleft.append(self.func(aleft[-1],nvals[i]))
                aright.append(self.func(aright[-1],nvals[-i-1]))
            
            for i,ne in enumerate(nes):
                if ne==pa:
                    continue
                self.dics[ne][e]=self.addnode(self.func(aleft[i],aright[-1-i]))

            self.tot[e]=self.func(aright[-1],nvals[0])
        return self.dics

def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reverse=True)  #二個目の要素で降順並び替え

    N = int(input())
    #N, K = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列

    edge = [[] for i in range(N)]
    for i in range(N-1):#木の場合M=N-1
        a,b= map(int,input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1) #有向のばあいコメントアウト

    rt=rerooting(N,edge)
    d=rt.dics
    tot=rt.tot
    
    i2=pow(2,mod-2,mod)
    i2n=pow(i2,N,mod)
    i2n1=pow(i2,N-1,mod)
    ans=0
    cur0=(i2-i2n)%mod
    p2=[1]*(N+1)
    for i in range(1,N+1):
        p2[i]=p2[i-1]*2%mod


    for i in range(N):
        if len(edge[i])<2:
            continue
        cur=cur0
        
        for ne in d[i].values():
            cur-=(p2[ne]-1)*i2n
        
        ans+=cur
        ans%=mod
    
    print(ans)

if __name__ == "__main__":
    main()