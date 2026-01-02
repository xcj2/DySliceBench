def examA():
    N = I()
    ans = (10000 - N)%1000
    print(ans)
    return

def examB():
    T = ["AC","WA","TLE","RE"]
    N = I()
    S = [SI()for _ in range(N)]

    ans = [0]*4
    for s in S:
        for i in range(4):
            if s==T[i]:
                ans[i] += 1
                break
    for i in range(4):
        print(T[i]+" x "+str(ans[i]))
    return

def examC():
    H, W, K = LI()
    C = [[""]*W for _ in range(H)]
    for h in range(H):
        S = SI()
        for w in range(W):
            C[h][w] = S[w]
    ans = 0
    #print(C)
    for hi in range(1<<H):
        nowC = deepcopy(C)
        for h in range(H):
            if hi&(1<<h):
                for i in range(W):
                    nowC[h][i] = "R"
        for wi in range(1 << W):
            nowCC = deepcopy(nowC)
            for w in range(W):
                if wi & (1 << w):
                    for i in range(H):
                        nowCC[i][w] = "R"
            cnt = 0
            for h in range(H):
                for w in range(W):
                    if nowCC[h][w] == "#":
                        cnt += 1
            if cnt == K:
                #print(hi, wi, nowCC)
                ans += 1
    print(ans)
    return

def examD():
    N = I()
    A = LI()
    A.sort(reverse=True)
    ans = 0
    ans += A[0]
    cur = 0
    for i in range(2,N):
        if i%2==0:
            cur += 1
        ans += A[cur]
    print(ans)
    return

def examE():
    N, K = LI()
    A = LI()
    A_neg = []; neg = 0
    A_0 = []; num_0 = 0
    A_pos = []; pos = 0
    for a in A:
        if a<0:
            A_neg.append(-a)
            neg += 1
        elif a==0:
            A_0.append(a)
            num_0 += 1
        else:
            A_pos.append(a)
            pos += 1
    if N-num_0<K:
        print(0)
        return
    A_neg.sort()
    A_pos.sort()
    if pos==0:
        ans = 1
        if K%2==0:
            ans = 1
            for i in range(neg-K,neg):
                ans *= A_neg[i]
                ans %= mod
        else:
            for i in range(K):
                ans *= A_neg[i]
                ans %= mod
            ans = mod - ans
            if num_0>0:
                ans = 0
        print(ans)
        return

    if neg==0:
        ans = 1
        for i in range(pos - K, pos):
            ans *= A_pos[i]
            ans %= mod
        print(ans)
        return

    A_neg.sort(reverse=True)
    A_pos.sort(reverse=True)

    now_p = 0
    now_n = 0
    ans = 1

    if pos+neg==K:
        for i in range(pos):
            ans *= A_pos[i]
            ans %= mod
        for i in range(neg):
            ans *= A_neg[i]
            ans %= mod
        if neg%2==1:
            ans = mod-ans
        print(ans)
        return

    if K%2==1:
        ans *= A_pos[now_p]
        now_p += 1

    while (now_n + now_p < K):
        if now_n + 1 >= neg:
            ans *= A_pos[now_p] * A_pos[now_p + 1]
            ans %= mod
            now_p += 2
            continue
        if now_p + 1 >= pos:
            ans *= A_neg[now_n] * A_neg[now_n + 1]
            ans %= mod
            now_n += 2
            continue

        if A_pos[now_p] * A_pos[now_p + 1] >= A_neg[now_n] * A_neg[now_n + 1]:
            ans *= A_pos[now_p] * A_pos[now_p + 1]
            ans %= mod
            now_p += 2
        else:
            ans *= A_neg[now_n] * A_neg[now_n + 1]
            ans %= mod
            now_n += 2

    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examE()

"""
6
8 7 6 5 4 3


5 5
-1 -2 3 4 5
"""