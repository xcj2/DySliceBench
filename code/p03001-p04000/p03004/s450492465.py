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
#import fractions#古いatcoderコンテストの場合GCDなどはここからimportする
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
def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reverse=True)  #二個目の要素で降順並び替え

    N = int(input())
    #N, K = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    S=[]
    for i in range(N):
        x,y,d=input().split()
        x=int(x);y=int(y)
        S.append((x,y,d))
    sx=sorted(S,key=itemgetter(0))
    sy=sorted(S,key=itemgetter(1))
    ts=set([0])
    
    minx=sx[0][0]
    f1=0; f2=0
    for s in sx:
        if s[2]=="L" and not f1:
            if sx[0][2]=="R":
                ts.add((s[0]-minx)*0.5)
            else:
                ts.add(s[0]-minx)
            f1=1
        elif s[2] in ("U","D") and not f2:
            ts.add(s[0]-minx)
            f2=1
        
        if f1 and f2:
            break
        

    maxx=sx[-1][0]
    f1=0; f2=0
    for s in reversed(sx):
        if s[2]=="R" and not f1:
            if sx[0][2]=="L":
                ts.add(abs(s[0]-maxx)*0.5)
            else:
                ts.add(abs(s[0]-maxx))
            f1=1
        elif s[2] in ("U","D") and not f2:
            ts.add(abs(s[0]-maxx))
            f2=1
        
        if f1 and f2:
            break
    
    minx=sy[0][1]
    f1=0; f2=0
    for s in sy:
        if s[2]=="D" and not f1:
            if sy[1][2]=="U":
                ts.add((s[1]-minx)*0.5)
            else:
                ts.add(s[1]-minx)
            f1=1
        elif s[2] in ("L","R") and not f2:
            ts.add(s[1]-minx)
            f2=1
        
        if f1 and f2:
            break
        

    maxx=sy[-1][1]
    f1=0; f2=0
    for s in reversed(sy):
        if s[2]=="U" and not f1:
            if sx[1][2]=="D":
                ts.add(abs(s[1]-maxx)*0.5)
            else:
                ts.add(abs(s[1]-maxx))
            f1=1
        elif s[2] in ("L","R") and not f2:
            ts.add(abs(s[1]-maxx))
            f2=1
        
        if f1 and f2:
            break
    
    def calc(t):
        minx=10**9
        maxx=-10**9
        miny=10**9
        maxy=-10**9
        for s in S:
            x,y,d=s
            if d=="U":
                y+=t
            elif d=="D":y-=t
            elif d=="L":
                x-=t
            elif d=="R":
                x+=t
            minx=min(minx,x)
            miny=min(miny,y)
            maxx=max(maxx,x)
            maxy=max(maxy,y)
        return (maxx-minx)*(maxy-miny)
    ans=10**17
    for t in ts:
        ans=min(ans,calc(t))
    for t1,t2 in combinations(ts,2):
        mid=(t1+t2)*0.5
        ans=min(ans,calc(mid))
    print(ans)
    #print(ts)





if __name__ == "__main__":
    main()