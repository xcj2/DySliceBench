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


def tree_init(N):
    edgelist = [[] for _ in range(N)]
    for a, b in [map(int, input().split()) for i in range(N-1)]:#木じゃない場合N-1をNに変える
        edgelist[a-1].append(b-1)#ノードの番号が0から始まる場合-1を消す
        edgelist[b-1].append(a-1)
    return edgelist

def root(x,par):
    px=par[x]
    while px!=x:
        x=px
        px=par[x]
    return px
def union(x,y,par):
    rx,ry=root(x,par),root(y,par)
    if rx!=ry:
        par[ry]=rx 


def main():
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    #N = int(input())
    N,M,K = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    par=[i for i in range(N)]
    fl=[[] for _ in range(N)]
    counts=[0]*N
    for _ in range(M):
        a, b= map(int,input().split())
        counts[a-1]-=1
        counts[b-1]-=1
        fl[a-1].append(b-1)
        fl[b-1].append(a-1)

    visited=[False]*N
    roots=[0]*N
    pcount=[0]*N
    for i in range(N):
        if visited[i]:
            continue
        q=deque([i])
        while len(q):
            
            e=q.pop()
            if visited[e]:
                continue
            #print(e)
            roots[e]=i
            pcount[i]+=1
            visited[e]=True
            for ne in fl[e]:
                if visited[ne]:
                    continue
                q.append(ne)
    #print(pcount)

    for i in range(N):
        counts[i]+=pcount[roots[i]]-1

    for _ in range(K):
        a, b= map(int,input().split())
        if roots[a-1]==roots[b-1]:
            counts[a-1]-=1
            counts[b-1]-=1

    print(*counts)
    



if __name__ == "__main__":
    main()