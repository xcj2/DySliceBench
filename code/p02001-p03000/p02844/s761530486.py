def examD():
    N = I();  S = SI()
    dp = [[0]*10 for _ in range(N+1)]
    for i in range(N):
        for j in range(10):
            dp[i+1][j] = dp[i][j]
        dp[i+1][int(S[i])] +=1
    left = [-1]*10; right = [-1]*10
    for i in range(N):
        if left[int(S[i])]==-1:
            left[int(S[i])] = i
    for i in range(N-1,-1,-1):
        if right[int(S[i])]==-1:
            right[int(S[i])] = i
    ans = 0
#    print(left)
#    print(right)
    for i in left:
        if i>=0:
            for j in right:
                if j>=0:
                    for k in range(10):
                        if dp[j][k]>0 and dp[j][k] - dp[i+1][k] > 0:
                            ans += 1
#                            print(S[i],k,S[j])
    print(ans)
    return
def examE(mod):
    N = I()
    A = LI()
    a =[0,0,0]
    cur = 1
    for i in A:
        if a[0]==i:
            if a[0]==a[1]:
                if a[1]==a[2]:
                    cur *= 3
                else:
                    cur *=2
            a[0]+=1
        elif a[1]==i:
            if a[1] == a[2]:
                cur *= 2
            a[1] +=1
        elif a[2]==i:
            a[2]+=1
        else:
            cur *=0
        a.sort(reverse=True)
        cur %=mod
    print(cur)
    return

def examF():
    T = LI()
    A = LI()
    B = LI()
    loop1 = T[0]*(A[0]-B[0])
    loop2 = T[1]*(A[1]-B[1])
    if loop1>0 and loop2>0:
        ans = 0
    elif loop1<0 and loop2<0:
        ans = 0
    else:
        now = loop1
        cur = loop1+loop2
#        print(now,cur)
        if cur!=0:
            ans = abs(now)//abs(cur)*2
            if abs(now)%abs(cur)!=0:
                judge = now + cur*ans//2
                if (now>0 and judge+loop1>0) or (now<0 and judge+loop1<0):
                    ans +=1
        else:
            ans = "infinity"
    print(ans)
    return

import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
