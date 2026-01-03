def examA():
    a, b = LI()
    if b<a:
        a,b = b,a
    if a<=0 and 0<=b:
        print("Zero")
    elif 0<a:
        print("Positive")
    else:
        judge = b-a+1
        if judge%2==0:
            print("Positive")
        else:
            print("Negative")
    return

def examB():
    N, M = LI()
    flag_R = [False]*N
    cnt = [1]*N
    flag_R[0] = True
    for _ in range(M):
        x, y = LI()
        x -= 1; y -= 1
        if flag_R[x]:
            flag_R[y] = True
        cnt[y] += 1
        cnt[x] -= 1
        if cnt[x]==0:
            flag_R[x] = False
    ans = sum(flag_R)
    print(ans)
    return

def examC():
    N, L = LI()
    A = LI()
    can = set()

    if N==2:
        if sum(A)<L:
            print("Impossible")
            return

    l = inf
    for i in range(N-1):
        cur_R = A[i]+A[i+1]
        if cur_R>=L:
            l = min(l,i)
            can.add(i)
    if not can:
        print("Impossible")
        return
    print("Possible")
    ans = []

    for i in range(l):
        ans.append(i+1)
    for i in range(l,N-1)[::-1]:
        if i in can:
            continue
        ans.append(i+1)
    for i in can:
        ans.append(i+1)
    for v in ans:
        print(v)
    return

def examD():
    ans = 0
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
    examC()

"""

"""