def examC():
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
                    W[ne] = nowW + 1
                    que.append(ne)
        return W
    N, M = LI()
    V = [[]for _ in range(N)]
    for i in range(M):
        a, b = LI()
        a -= 1
        b -= 1
        V[a].append(b)
        V[b].append(a)
    L = bfs(N,0,V)
    if L[N-1]==2:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
    return

def examD():
    K = I()
    N = 50
    A = [i for i in range(N)]
    for i in range(N):
        A[-1-i] +=((K-i+49)//N)
    print(N); print(" ".join(map(str,A)))
    return

def examE():
    N = I()
    A = LI()
    ans = 0
    while(True):
        cur = 0
        for i in range(N):
            cur += A[i]//N
        for i in range(N):
            A[i] = A[i]%N + cur-A[i]//N
        ans += cur
        if cur==0:
            break
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LFI(): return list(map(float,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examC()

"""

"""