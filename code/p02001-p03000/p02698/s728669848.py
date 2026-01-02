def examA():
    K = I()
    A, B = LI()
    for i in range(A,B+1):
        if i%K==0:
            print("OK")
            return
    print("NG")
    return

def examB():
    X = I()
    now = 100
    ans = 0
    while(now<X):
        ans += 1
        now += now//100
    print(ans)
    return

def examC():
    N, M, Q = LI()

    ans = 0
    print(ans)
    return

def examD():
    A, B, N = LI()
    if N>=B-1:
        ans = (A*(B-1))//B
    else:
        ans = (A*N)//B
    print(ans)
    return

def examE():
    N, M = LI()
    ans = []
    if N%2==1:
        for i in range(N // 2):
            ans.append((i + 1, N - i))
    else:
        flag = False
        for i in range(N // 2):
            if N-i-(i+1)<=N//2:
                flag = True
            if flag:
                ans.append((i+1,N-i-1))
            else:
                ans.append((i + 1, N - i))
    #print(ans)
    for v in ans[:M]:
        print(" ".join(map(str,v)))
    return

def examF():
    N = I()
    A = LI()
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        u, v = LI()
        u -= 1; v -= 1
        V[u].append(v)
        V[v].append(u)
    dp = [-1]*N
    dp[0] = 1
    LIS = deque()
    LIS.append(A[0])
    def dfs(s):
        #print(LIS)
        for i in V[s]:
            if dp[i]!=-1:
                continue
            flag = []
            if A[i] > LIS[-1]:
                LIS.append(A[i])
                flag = False
            else:
                flag = [bisect.bisect_left(LIS, A[i]),LIS[bisect.bisect_left(LIS, A[i])]]
                LIS[flag[0]] = A[i]
            dp[i] = len(LIS)
            dfs(i)
            #print(flag)
            if not flag:
                LIS.pop()
            else:
                LIS[flag[0]] = flag[1]
        return
    dfs(0)
    ans = dp
    for v in ans:
        print(v)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examF()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""