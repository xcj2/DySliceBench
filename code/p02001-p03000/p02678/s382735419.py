def examA():
    S = {0:"pon",1:"pon",2:"hon",3:"bon",4:"hon",5:"hon",6:"pon",7:"hon",8:"pon",9:"hon"}
    N = SI()
    ans = S[int(N[-1])]
    print(ans)
    return

def examB():
    K = I()
    S = SI()
    N = len(S)
    if N<=K:
        ans = S
    else:
        ans = S[:K]+"..."
    print(ans)
    return

def examC():
    A, B, H, M = LI()
    a = abs(H*30 - M*5.5)
    deg = min(360-a,a)*math.pi/180
    #print(deg)
    ans = (A**2 + B**2 - 2*A*B*math.cos(deg))**(0.5)
    print(ans)
    return

def examD():

    N, M = LI()
    V = [[]for _ in range(N)]
    for _ in range(M):
        a, b = LI()
        a -= 1; b -= 1
        V[a].append(b)
        V[b].append(a)

    ans = [-1]*N

    def bfs(n, e, fordfs):
        # 点の数、スタートの点、有向グラフ
        W = [-1] * n
        # 各点の状態量、最短距離とか,見たかどうかとか
        W[e] = 0
        que = deque()
        que.append(e)
        while que:
            now = que.popleft()
            nowW = W[now]
            for ne in fordfs[now]:
                if W[ne] == -1:
                    W[ne] = now
                    que.append(ne)
        return W
    ans = bfs(N,0,V)
    for a in ans:
        if a==-1:
            print("No")
            return
    print("Yes")
    for v in ans[1:]:
        print(v+1)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
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

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examD()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""