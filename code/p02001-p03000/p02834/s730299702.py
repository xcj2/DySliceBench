def examA():
    AB = [I() for _ in range(2)]
    for i in range(1,4):
        if not i in AB:
            ans = i
            break
    print(ans)
    return

def examB():
    N = I()
    S,T = LSI()
    ans = ""
    for i in range(N):
        ans += S[i]+T[i]
    print(ans)
    return

def gcd(x, y):
    if y == 0:
        return x
    while y != 0:
        x, y = y, x % y
    return x
def lcm(x, y):
    return x * y // gcd(x, y)
def examC():
    A, B = LI()
    ans = lcm(A,B)
    print(ans)
    return

def examD():
    N = I()
    A = LI()
    ans = N; cur = 1
    for a in A:
        if cur==a:
            ans -=1
            cur +=1
    if ans==N:
        ans = -1
    print(ans)
    return

def examE():
    N = I()
    ans = 0
    if N%2==0:
        N //=2
        while(N>0):
            ans +=N//5
            N //=5
    print(ans)
    return


def bfs(n,e,fordfs):
    #点の数、スタートの点、有向グラフ
    W = [-1]*n
    #各点の状態量、最短距離とか,見たかどうかとか
    W[e] = 0
    que = deque()
    que.append(e)
    len = [float("inf")]*n
    len[e] = 0
    while que:
        now = que.popleft()
        nowv = W[now]
        nowlen = len[now]
        for ne in fordfs[now]:
            if nowv == W[ne]:
                #ループが嫌な時
                return -1
            elif W[ne] == -1:
                W[ne] = (nowv+1) % 2
                len[ne] = nowlen+1
                que.append(ne)
    return len
def examF():
    N, u, v = LI()
    V = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = LI()
        V[a-1].append(b-1)
        V[b-1].append(a-1)
    La = bfs(N,u-1,V)
    Lb = bfs(N,v-1,V)
#    print(La)
#    print(Lb)
    ans = 0
    for i in range(N):
        if La[i]>Lb[i]:
            continue
        ans = max(Lb[i],ans)
    print(ans-1)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examF()
