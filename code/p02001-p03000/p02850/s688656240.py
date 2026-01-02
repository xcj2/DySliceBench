def bfs(n,e,fordfs,D):
    #点の数、スタートの点、有向グラフ
    W = [-1]*(n-1)
    #各点の状態量、最短距離とか,見たかどうかとか
    used = defaultdict(bool)
    que = deque()
    que.append(e)
    while que:
        now = que.popleft()
        i = 1
        for ne in fordfs[now]:
            l = min(now,ne); r = max(now,ne)
            if W[D[(l,r)]] == -1:
                while(True):
                    if not used[(now,i)]:
                        used[(now, i)] = True
                        used[(ne, i)] = True
                        break
                    i +=1
                que.append(ne)
                W[D[(l,r)]] = i
    return W
def examD():
    N = I()
    V = [[]for _ in range(N)]
    d = defaultdict(int)
    for i in range(N-1):
        a, b = LI()
        V[a-1].append(b-1)
        V[b-1].append(a-1)
        d[(a-1,b-1)] = i
    ans = bfs(N,0,V,d)
    print(max(ans))
    for v in ans:
        print(v)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examD()
