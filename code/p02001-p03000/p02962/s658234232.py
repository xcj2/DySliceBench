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
import random

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
    #N, K = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列


    class rh:#base,max_n,convertを指定すること
        def __init__(self,base=26,max_n=5*10**5):#baseとmaxnを指定すること。baseは偶数(modが奇数)
            self.mod=random.randrange(1<<54-1,1<<55-1,2)#奇数、衝突させられないよう乱数で生成
            self.base=int(base*0.5+0.5)*2#偶数,英小文字なら26とか
            self.max_n=max_n
            self.pows1=[1]*(max_n+1)
            cur1=1
            for i in range(1,max_n+1):
                cur1=cur1*base%self.mod
                self.pows1[i]=cur1
    
        def convert(self,c): return alp2num(c,False)#大文字の場合Trueにする
        
        def get(self, s):#特定の文字のhash. O(|s|)
            n=len(s)
            mod=self.mod
            si=[self.convert(ss) for ss in s]
            h1=0
            for i in range(n):h1=(h1+si[i]*self.pows1[n-1-i])%mod
            return h1
        
        def get_roll(self, s, k):#ローリングハッシュ,特定の文字の中から長さkのhashをすべて得る,O(|s|)
            n=len(s)
            si=[self.convert(ss) for ss in s]
            mod=self.mod
            h1=0
            for i in range(k):h1=(h1+si[i%n]*self.pows1[k-1-i])%mod
            hs=[0]*n
            hs[0]=h1
            mbase1=self.pows1[k]
            base=self.base
            for i in range(1,n): 
                front=si[i-1];back=si[(i+k-1)%n]
                h1=(h1*base-front*mbase1+back)%mod
                hs[i]=h1
            return hs
    
    s=input()
    t=input()
    n=len(s)
    nt=len(t)
    rhs=rh()
    has=rhs.get(t)
    hass=rhs.get_roll(s,nt)
    l=[hass[i]==has for i in range(n)]
    ds=[0]*n
    for i in range(n):
        ci=i
        q=deque()
        while l[ci] and ds[ci]==0:
            q.append(ci)
            ci=(ci+nt)%n
            if ci==i:
                print(-1)
                return
        tot=ds[ci]
        while q:
            tot+=1
            ci=q.pop()
            ds[ci]=tot
    print(max(ds))
        




if __name__ == "__main__":
    
    main()