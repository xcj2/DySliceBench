###参考 https://ei1333.hateblo.jp/entry/2017/04/10/224413
# 非負の重みをもつ無向の木 T の直径
def main():
    N = I()
    if N==1:
        print(0)
        return
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        s, t, w = LI()
        V[s].append((t,w))
        V[t].append((s,w))
    dist = [0]*N

    def dfs1(start,parent):
        for i,w in V[start]:
            if i==parent:
                continue
            dfs1(i,start)
            dist[start] = max(dist[start],dist[i]+w)
        return
    def dfs2(s,d_p,p):
        child = [(0,-1)]
        for i,w in V[s]:
            if i==p:
                child.append((d_p+w,i))
            else:
                child.append((w+dist[i],i))
        child.sort(reverse=True)
        rep = child[0][0] + child[1][0]
        for i,w in V[s]:
            if i==p:
                continue
            rep = max(rep,dfs2(i,child[child[0][1]==i][0],s))
        return rep
    dfs1(N//2,-1)
    #print(dist)
    ans = dfs2(N//2,0,-1)
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(2*10**6)

if __name__ == '__main__':
    main()

"""


"""
