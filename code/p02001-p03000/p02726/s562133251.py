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
#dequeを使うときはpython3を使う、pypyはダメ
from collections import Counter#文字列を個数カウント辞書に、
#S=Counter(l),S.most_common(x),S.keys(),S.values(),S.items()
from itertools import accumulate#累積和
#list(accumulate(l))
from heapq import heapify,heappop,heappush
#heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone

def input(): return sys.stdin.readline()[:-1]
def printl(li): print(*li, sep="\n")
def argsort(s, return_sorted=False): 
    inds=sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted: return inds, [s[i] for i in inds]
    return inds

#mod = 10**9+7
#w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

#N = int(input())
#N, K = map(int, input().split())
#L = [int(input()) for i in range(N)]
#A = list(map(int, input().split()))
#S = [list(map(int, input().split())) for i in range(N)]

mod=10**4
def dk(edge,vis):
    q=[vis]
    visited=[False]*N
    heapify(q)
    while len(q):
        e=heappop(q)
        cd,ce=e//mod, e%mod
        
        if visited[ce]:
            continue
        #print(cd,ce)
        visited[ce]=True
        if ce>vis:
            ans[cd]+=1
        for ne in edge[ce]:
            heappush(q,(cd+1)*mod+ne)



N, X, Y = map(int,input().split()) #n:頂点数　w:辺の数
ans=[0]*(N)
edge = [[] for i in range(N)]
    #edge[i] : iから出る道の[重み,行先]の配列
for i in range(N-1):
    x,y=i,i+1
    edge[x].append(y)
    edge[y].append(x)
edge[X-1].append(Y-1)
edge[Y-1].append(X-1)

for vis in range(N-1):
    dk(edge,vis)
    #print(ans)
for a in ans[1:]:
    print(a)

    