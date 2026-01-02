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

def ARC68_C():
    X = I()
    ans = 0
    ans += 2*(X//11)
    rest = X%11
    if rest>0:
        ans += 1
    if rest>=7:
        ans += 1
    print(ans)
    return

def ABC49_C():
    S = SI()
    T = {"maerd","remaerd","esare","resare"}
    stack = ""
    for s in S[::-1]:
        stack += s
        if stack in T:
            stack = ""
    if stack:
        print("NO")
    else:
        print("YES")
    return

def ABC142_E():
    N, M = LI()
    A = [0]*M
    C = [[]for _ in range(M)]
    for i in range(M):
        A[i], b = LI()
        C[i] = LI()
    mask = 2**N
    dp = [[inf]*mask for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(M):
        key = 0
        for j in C[i]:
            key += 2**(j-1)
        #print(key)
        for now in range(mask):
            dp[i + 1][now] = min(dp[i + 1][now], dp[i][now])
            if key|now==now:
                continue
            dp[i+1][now|key] = min(dp[i+1][now|key],dp[i][now]+A[i])
    if dp[M][mask-1]==inf:
        print(-1)
    else:
        ans = dp[M][mask-1]
        print(ans)
    #print(dp)
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
    ABC142_E()

"""

"""