def examC():
    N, M = LI()
    if N-M//2>=0:
        ans = M//2
    else:
        ans = N + (M-N*2)//4
    print(ans)
    return

def examD():
    N = I()
    S = SI()
    for i1,i2 in [[0,0],[0,1],[1,0],[1,1]]:
        flag = True
        sheep = [1]*N
        sheep[0] = i1
        sheep[1] = i2
        for j in range(1,N-1):
            if S[j]=="o":
                cur = 1
            else:
                cur = 0
            sheep[j+1] = (sheep[j]^cur)^sheep[j-1]
        if S[-1] == "o":
            cur = 1
        else:
            cur = 0
        if sheep[0]!=(sheep[-1] ^ cur) ^ sheep[-2]:
            flag = False
        if S[0] == "o":
            cur = 1
        else:
            cur = 0
        if sheep[1]!=(sheep[0] ^ cur) ^ sheep[-1]:
            flag = False
        if flag:
            ans = ""
            for i in sheep:
                if i==1:
                    ans += "S"
                else:
                    ans += "W"
            print(ans)
            return
    print(-1)
    return

def examE():
    N = I()
    A = LI()
    Ai = [[0,0]]
    for i in range(N):
        Ai.append([A[i],i])
    Ai = sorted(Ai, key=lambda x:x[1], reverse = True)
    Ai = sorted(Ai, key=lambda x:x[0], reverse = True)
#    print(Ai)
    ans = [0]*N
    now = N
    for i in range(N):
        now = min(now,Ai[i][1])
        ans[now] += (i+1)*(Ai[i][0]-Ai[i+1][0])
    for v in ans:
        print(v)
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
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examE()

"""

"""