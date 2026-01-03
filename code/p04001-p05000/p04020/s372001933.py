def examA():
    S = SI()
    if "W" in S and not "E" in S:
        print("No")
    elif "E" in S and not "W" in S:
        print("No")
    elif "N" in S and not "S" in S:
        print("No")
    elif "S" in S and not "N" in S:
        print("No")
    else:
        print("Yes")
    return

def examB():
    N = I()
    A = [I()for _ in range(N)]
    ans = 0
    for i in range(N-1):
        ans += A[i]//2
        if A[i]%2 and A[i+1]>=1:
            ans += 1
            A[i+1] -= 1
    ans += A[N-1]//2
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    N = I()
    S = [I()for _ in range(N)]

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
    examB()

"""

"""