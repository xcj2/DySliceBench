def examA():
    N = LI()
    N.sort()
    if N[0]==N[1] and N[0]!=N[2]:
        print("Yes")
    elif N[1]==N[2] and N[0]!=N[2]:
        print("Yes")
    else:
        print("No")
    return

def examB():
    N = I()
    A = LI()
    for a in A:
        if a%2==0:
            if a%3!=0 and a%5!=0:
                print("DENIED")
                return
    print("APPROVED")
    return

def examC():
    N = I()
    S = [SI()for _ in range(N)]
    d = defaultdict(int)
    for s in S:
        d[s] += 1
    t = max(d.values())
    ans = []
    for s in S:
        if d[s]==t:
            ans.append(s)
            d[s] = 0
    ans.sort()
    for v in ans:
        print(v)
    return

def examD():
    N, K = LI()
    A = LI()


    ans = 0
    print(ans)
    return

def examE():
    S = SI()
    N = len(S)
    flag = False
    ans = 0
    for i in range(N-1,-1,-1):
        #print(ans)
        cur = int(S[i])
        if flag:
            cur += 1
        if cur>=6:
            ans += 10-cur
            flag = True
        else:
            ans += cur
            flag = False
    if flag:
        ans += 1
    print(ans)
    return

def examE2():
    S = SI()
    N = len(S)
    dp = [[0]*2 for _ in range(N+2)]
    dp[0][1] = inf
    S = S[::-1]
    S += "0"
    for i in range(N+1):
        s = int(S[i])
        dp[i+1][0] = dp[i][0] + s
        dp[i+1][1] = dp[i][0] + (10-s)
        if s<9:
            dp[i+1][0] = min(dp[i+1][0],dp[i][1] + (s+1))
        dp[i+1][1] = min(dp[i+1][1],dp[i][1] + (10-s-1))
    #print(dp)
    ans = min(dp[-1][0],dp[-1][1])
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
    examE2()

"""
4396817
"""