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

def primes(n):
    a = Counter()
    while n % 2 == 0:
        a[2]+=1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a[f]+=1
            n //= f
        else:
            f += 2
    if n != 1:
        a[n]+=1
    return a
def daccumulate(s):#二次元累積和
    n=len(s); m=len(s[0])
    acc=[[0]*m for _ in range(n)]
    for i in range(n):
        si=s[i]; ai=acc[i]
        for j in range(m):
            tot=si[j]
            if i>0: tot+=acc[i-1][j]
            if j>0:
                tot+=ai[j-1]
                if i>0: tot-=acc[i-1][j-1]
            ai[j]=tot
    return acc

def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reverse=True)  #二個目の要素で降順並び替え

    N = int(input())
    #N, K = map(int, input().split())
    #A = tuple(map(str, input().split())) #1行ベクトル
    A = tuple(input() for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    ans=0
    dp=[[0]*19 for _ in range(19)]
    t9=10**9
    bas=100

    for a in A:
        ta=0


        ta=round(float(a)*t9)

        n2=0
        n5=0
        while ta%2==0:
            n2+=1
            ta//=2
        while ta%5==0:
            n5+=1
            ta//=5


        n2=min(18,n2)
        n5=min(18,n5)
        dp[18-n2][18-n5]+=1
    ddp=daccumulate(dp)
    ans=0

    for i in range(19):
        for j in range(19):
            t2=18-i
            t5=18-j
            c=dp[t2][t5]
            ta=ddp[i][j] 
            if i*2>=18 and j*2>=18:
                ta-=c
                ans+=c*(c-1)
            ans+=ta*c

    print(ans//2)
               




if __name__ == "__main__":
    main()