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
def matmat(A,B):
    K,N,M=len(B),len(A),len(B[0])
    return [[sum([(A[i][k]*B[k][j]) for k in range(K)]) for j in range(M)] for i in range(N)]
def matvec(M,v):
    N=len(v)
    size=len(M)
    return [sum([M[i][j]*v[j] for j in range(N)]) for i in range(size)]
def main():
    mod = 10**9+7
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    N = int(input())
    #N, K = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    count=0

    ab=0
    a=0
    b=0
    for i in range(N):
        s=input()
        ls=len(s)
        for j in range(ls-1):
            if s[j:j+2]=='AB':
                count+=1
        if s[0]=='B' and s[-1]=='A':
            ab+=1
        elif s[-1]=='A':
            a+=1
        elif s[0]=='B':
            b+=1
    if a==0 and b==0:
        print(count+max(ab-1,0))
        exit()
    ans=min(a,b)+count
    ret=abs(a-b)
    if ret<=ab:
        ans+=ab
    else:
        ans+=ab
    print(ans)
    

    


if __name__ == "__main__":
    main()