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



def tree_init(N,M):
    edgelist = [[] for _ in range(N)]
    for a, b in [map(int, input().split()) for i in range(M)]:#木じゃない場合N-1をNに変える
        edgelist[a-1].append(b-1)#ノードの番号が0から始まる場合-1を消す
        edgelist[b-1].append(a-1)
    return edgelist

def dfs(N, start, edge):
    q=deque([(start,0)])
    visited=[False]*N
    ans=[0]*N
    while len(q):
        e, pe=q.popleft()#ここをpopleftにすると幅優先探索BFSになる
        if visited[e]:continue
        ans[e]=pe
        visited[e]=True
        for ne in edge[e]:
            q.append((ne,e))
            
    return ans

def main():
    mod = 10**9+7
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    #N = int(input())
    N, M = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列

    edgelist=tree_init(N,M)

    ans=dfs(N,0,edgelist)
    print('Yes')
    for a in ans[1:]:
        print(a+1)





if __name__ == "__main__":
    main()