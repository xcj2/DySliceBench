def examD():
    St = S(); X, Y = LI()
    N = len(St)
    ans = "No"
    Fx = deque(); Fy = deque()
    ve = int(1); cur = int(0)
    for i in range(N):
        if St[i] == "F":
            cur += 1
        else:
            if ve == 1:
                Fx.append(cur)
                cur = int(0)
                ve *= -1
            else:
                Fy.append(cur)
                cur = int(0)
                ve *= -1
    if ve == 1:
        Fx.append(cur)
    else:
        Fy.append(cur)
    xfirst = Fx.popleft()
    X = X - xfirst
#    print(Fx)
#    print(Fy)
    xlen = len(Fx); ylen = len(Fy)
    xneed = -1; yneed = -1
    if (sum(Fx) - X) % 2 == 0:
        xneed = (sum(Fx) - X) // 2
    if (sum(Fy) - Y) % 2 == 0:
        yneed = (sum(Fy) - Y) // 2
#    print(xneed)
    dp = [[0] * (xneed + 1) for _ in range(xlen + 1)]
    if xneed > 0:
        dp[0][0] = 1
        for i in range(xlen):
            for j in range(max(xneed + 1, 0)):
                if dp[i][j] != 0:
                    if xneed + 1 - Fx[i] > j:
                        dp[i + 1][j + Fx[i]] = dp[i][j]
                    dp[i + 1][j] = dp[i][j]
    #    print(dp)
    #    print(dp[xlen][xneed])
    if (xneed > 0 and dp[xlen][xneed] == 1) or xneed == 0:
        dp = [[0] * (yneed + 1) for _ in range(ylen + 1)]
        if yneed>0:
            dp[0][0] = 1
            for i in range(ylen):
                for j in range(max(yneed + 1, 0)):
                    if dp[i][j] != 0:
                        if yneed + 1 - Fy[i] > j:
                            dp[i + 1][j + Fy[i]] = dp[i][j]
                        dp[i + 1][j] = dp[i][j]
        if (yneed > 0 and dp[ylen][yneed] == 1) or yneed == 0:
            ans = "Yes"
    print(ans)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
