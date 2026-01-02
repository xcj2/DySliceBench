def ABC67_B():
    N, K = LI()
    L = LI()
    L.sort(reverse=True)
    ans = sum(L[:K])
    print(ans)
    return

def ABC100_C():
    def factorization_2(n):
        arr = defaultdict(int)
        temp = n
        i = 2
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr[i] = cnt
        if temp != 1:
            arr[temp] = 1
        if arr == []:
            arr[n] = 1
        return arr[2]
    N = I()
    A = LI()
    ans = 0
    for a in A:
        ans += factorization_2(a)
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
    ABC100_C()

"""

"""