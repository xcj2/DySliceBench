def examA():
    R = I()
    if R<1200:
        ans = "ABC"
    elif R<2800:
        ans = "ARC"
    else:
        ans = "AGC"
    print(ans)
    return

def examB():
    S = SI(); N = len(S)
    ans = "AC"
    if not S[0]=="A":
        ans = "WA"
    flag = False
    for i in range(2,N-1):
        if S[i]=="C":
            flag = True
    if not flag:
        ans = "WA"
    num = 0
    for i in S:
        if ord("A")<=ord(i)<=ord('Z'):
            num +=1
    if not num==2:
        ans = "WA"
    print(ans)
    return

def examC():
    return

def examD():
    S = SI(); N = len(S)
    dp = [[0]*4 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        C = S[i]
        if C=="?":
            dp[i+1][0] = dp[i][0]*3
            dp[i+1][1] = dp[i][1]*3 + dp[i][0]
            dp[i+1][2] = dp[i][2]*3 + dp[i][1]
            dp[i+1][3] = dp[i][3]*3 + dp[i][2]
        elif C=="A":
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1] + dp[i][0]
            dp[i+1][2] = dp[i][2]
            dp[i+1][3] = dp[i][3]
        elif C=="B":
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1]
            dp[i+1][2] = dp[i][2] + dp[i][1]
            dp[i+1][3] = dp[i][3]
        elif C=="C":
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1]
            dp[i+1][2] = dp[i][2]
            dp[i+1][3] = dp[i][3] + dp[i][2]
        for j in range(4):
            dp[i+1][j] %=mod
    ans = dp[-1][3]
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
    examD()
