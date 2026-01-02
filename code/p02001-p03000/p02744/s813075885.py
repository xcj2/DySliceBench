def examA():
    L = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
    K = I()

    ans = L[K-1]
    print(ans)
    return

def examB():
    H, W = LI()
    if H==1 or W==1:
        print(1)
        return
    ans = H*W//2 + (H*W)%2
    print(ans)
    return

def examC():
    a,b,c = LI()
    if c-(a+b)<=0:
        print("No")
        return
    judge = (c-a-b)**2-4*a*b
    if judge>0:
        print("Yes")
    else:
        print("No")
    return

def examD():
    def bfs(N):
        W = [0]*(5*10**6)
        L = [""]*(5*10**6)
        que = deque()
        que.append(0)
        L[0] = "a"
        W[0] = 0
        flag = True
        ne = 0
        while(flag):
            now = que.popleft()
            nowW = W[now]
            if len(L[now])==N:
                flag = False
                break
            for i in range(W[now]+2):
                ne += 1
                W[ne] = max(nowW,i)
                que.append(ne)
                L[ne] = L[now] + alphabet[i]
        return L
    N = I()
    D = bfs(N)
    for ans in D:
        if not ans:
            break
        if len(ans)<N:
            continue
        print(ans)
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

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examD()

"""

"""