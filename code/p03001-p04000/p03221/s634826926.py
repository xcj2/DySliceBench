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

def main():
    mod = 10**9+7
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    #N = int(input())
    N, M = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    tot=[[] for _ in range(N+1)]
    ys=[0]*M
    for i in range(N):
        heapify(tot[i])
    for i in range(M):
        P, Y = map(int, input().split())
        heappush(tot[P],[Y,i])
        ys[i]=Y
    tset=[]
    ans=['']*M
    for i in range(N+1):
        t1=tot[i]
        if len(t1)<1:continue
        p=str(i).zfill(6)
        j=0
        while len(t1):
            t, i1=heappop(t1)
            tx=str(j+1).zfill(6)
            ans[i1]=''.join((p,tx))
            j+=1
    print('\n'.join(ans))





if __name__ == "__main__":
    main()