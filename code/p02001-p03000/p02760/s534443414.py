def examA():
    N = I()
    ans = N//2 + N%2
    print(ans)
    return

def examB():
    A = [LI()for _ in range(3)]
    N = I()
    B = [I()for _ in range(N)]
    grid = [[False]*3 for _ in range(3)]
    ans = "No"
    for b in B:
        for i in range(3):
            for j in range(3):
                if A[i][j]==b:
                    grid[i][j] = True
    for i in range(3):
        flag = True
        for j in range(3):
            if not grid[i][j]:
                flag = False
        if flag:
            ans = "Yes"
    for i in range(3):
        flag = True
        for j in range(3):
            if not grid[j][i]:
                flag = False
        if flag:
            ans = "Yes"
    flag = True
    for i in range(3):
        if not grid[i][i]:
            flag = False
    if flag:
        ans = "Yes"
    flag = True
    for i in range(3):
        if not grid[i][2-i]:
            flag = False
    if flag:
        ans = "Yes"
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
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

import sys,copy,bisect,itertools,heapq,math,random
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

if __name__ == '__main__':
    examB()

"""

"""