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
def alp2num(c,cap=False): return ord(c)-97 if not cap else ord(c)-65
def num2alp(i,cap=False): return chr(i+97) if not cap else chr(i+65)

class modint():#add:和,mul:積,pow:累乗,div:商(modと互いに素であること)
    def __init__(self,x,mod=1000000007): self.x, self.mod=x, mod
    def add(self,a): self.x=(self.x+a%self.mod)%self.mod
    def mul(self,c): self.x=(self.x*(c%self.mod))%self.mod
    def pow(self,p): self.x=pow(self.x,p,self.mod)
    def div(self,d):
        u,v,a,b=1,0,d,self.mod
        while b:
            t=a//b
            a-=t*b
            a,b,u,v=b,a,v,u-t*v
        if a!=1: print("not 素")
        self.x=(self.x*(u%self.mod))%self.mod

def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    N = int(input())
    #N, K = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列

    d=dict()
    m=10**18+100
    for i in range(N):
        A, B = map(int, input().split())
        if A==0 and B==0:
            d[-m]=d.get(-m,0)+1
        elif B==0:
            d[m]=d.get(m,0)+1
        elif A==0:
            d[0]=d.get(0,0)+1
        else:
            sa=sb=1
            if A<0:
                sa=-1
                A*=-1
            if B<0:
                sb=-1
                B*=-1

            g=math.gcd(A,B)
            A=A//g
            B=B//g
            if sa==-1 and sb==-1:
                t=(A,B)
            elif sb==-1:
                t=(-A,B)
            else:
                t=(sa*A,sb*B)
            d[t]=d.get(t,0)+1
    
        
    #print(d)
    ks=set(d.keys())
    alis=[]
    tot=modint(1)
    for i, k in enumerate(ks):
        if d[k]==-1.0:
            continue
        if k==-m:
            continue
        if k==m:
            ik=0
        elif k==0:    
            ik=m
        elif k[0]<0:
            ik=(k[1],-k[0])
        else:
            ik=(-k[1],k[0])
        #print(ik)
        if ik in ks:
            d1,d2=d[k],d[ik]
            tot.mul((pow(2,d1,mod)-1)+(pow(2,d2,mod)-1)+1)
            d[ik]=-1

        else:
            tot.mul(pow(2,d[k],mod))

    tot.add(-1)
    tot.add(d.get(-m,0))
    
    print(tot.x)




if __name__ == "__main__":
    main()