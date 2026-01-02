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

def extgcd1(a0,b0):
    u=1
    v=0
    a=a0
    b=b0
    while b:
        t=a//b
        a-=t*b
        a,b=b,a
        u-=t*v
        u,v=v,u
    if a!=1: 
        #print("not 素")
        return -1
    return u%b0 #a0*u=1(mod b0)

def main():
    mod =998244353
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    #N = int(input())
    N, M, K = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列

    # dp=[0]*2
    # ndp=copy(dp)
    # dp[0]=0
    # dp[1]=M
    # for i in range(2,N+1):
    #     if i<=K+1:
    #         ndp[0]=((M-1)*(dp[0]+dp[1])+dp[0])%mod
    #         ndp[1]=dp[1]
    #     else:
    #         ndp[0]=(M*dp[0]+(M-1)*dp[1])%mod
    #         ndp[1]=0

    #     dp=copy(ndp)
    # ans=(dp[0]+dp[1])%mod
    # #print(ans)

    #n0=math.factorial(N-1)
    #ks=[1]*(N-1+1)
    #for k in range(2,N-1+1):
    #    ks[k]=ks[k-1]*k
    ans=0
    c0=1
    c1=pow(M-1,N-1,mod)
    inv=[1,1]+[extgcd1(i,mod) for i in range(2,N)]
    #print("ok1")
    ifac=[1]*(N)
    nfac=1
    for i in range(1,N):
        nfac=(i*nfac)%mod
        ifac[i]=(ifac[i-1]*inv[i])%mod
    #print("ok2")
    #print(ifac)
    
    
    mp=[1]*(N)
    for i in range(1,N):
        mp[i]=(mp[i-1]*(M-1))%mod
    #print("ok3")
    ans=0
    #print(nfac)
    #print(mp)
    
    for k in range(0,K+1):
        #print((n0//ks[k]//ks[N-1-k]))
        ans=ans+(mp[N-1-k]*nfac*ifac[k]*ifac[N-1-k])%mod
        ans%=mod
        #print(ans)
    #print(ks)
    ans=(ans*M)%mod
    print(ans)
if __name__ == "__main__":
    main()