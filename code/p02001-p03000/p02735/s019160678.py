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

def dfs(H,W,L):
    d=0
    c=True
    if L[0][0]==False:
        d=1
        c=False
    q=deque([(d*10000,c)])
    dxs=((0,1),(1,0))
    visited=[False]*10000
    while len(q):
        
        #print(q)
        dxy,c=q.popleft()#ここをpopleftにすると幅優先探索BFSになる
        d,xy=divmod(dxy,10000)
        x,y=divmod(xy,100)
        if visited[xy]: continue
        visited[xy]=True
        if x==H-1 and y==W-1:
            return d
        for dx in dxs:
            nx=x+dx[0]
            ny=y+dx[1]
            if nx>=H or ny>=W:
                continue
            if visited[nx*100+ny]:continue

            if L[nx][ny] or c==False:
                q.appendleft((d*10000+nx*100+ny,L[nx][ny]))
            else:
                q.append(((d+1)*10000+nx*100+ny,False))

                


def main():
    mod = 10**9+7
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    #N = int(input())
    H,W = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    L = list(list(input()) for i in range(H)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    #Lt=[[True]*H for _ in range(W)]
    for i in range (H):
        for j in range(W):
            if L[i][j]=='#':
                L[i][j]=False
            else:
                L[i][j]=True
            
    ans=dfs(H,W,L)

    print(ans)


if __name__ == "__main__":
    main()