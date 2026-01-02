#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007

#A
def A():
    """
    N個の足場があります。足場には1,2,…,Nと番号が振られています。 
    各i (1≤i≤N) について、足場 i の高さは hi です。
    最初、足場 1 にカエルがいます。 カエルは次の行動を何回か繰り返し、足場 N まで辿り着こうとしています。
    足場 i にいるとき、足場 i+1 または i+2 へジャンプする。
    このとき、ジャンプ先の足場を j とすると、コスト |hi−hj| を支払う。
    カエルが足場 N に辿り着くまでに支払うコストの総和の最小値を求めてください。

    制約
        入力はすべて整数である。
    2≤N≤10**5
    1≤hi≤10**4
    """
    n = II()
    h = LI()
    dp = [0 for i in range(n)]
    dp[1] = abs(h[0] - h[1])
    for i in range(2,n):
        dp[i] = min(dp[i - 1] + abs(h[i - 1] - h[i]), dp[i - 2] + abs(h[i - 2] - h[i]))
    print(dp[n-1])
    return

#B
def B():
    n, K = LI()
    h = LI()
    dp = [float("INF") for i in range(n + K + 1)]
    dp[0] = 0
    for i in range(n):
        for k in range(1, K + 1):
            if i + k >= n:
                break
            dp[i + k] = min(dp[i + k], dp[i] + abs(h[i] - h[i + k]))
    print(dp[n-1])
    return

#C
def C():
    n = II()
    abc = LIR(n)
    dp = [0 for i in range(3 * n + 1)]
    dp[0] = abc[0][0]
    dp[1] = abc[0][1]
    dp[2] = abc[0][2]
    for i in range(1,n):
        dp[3 * i] = max(dp[3 * i], dp[3 * (i - 1) + 1] + abc[i][0], dp[3 * (i - 1) + 2] + abc[i][0])
        dp[3 * i + 1] = max(dp[3 * i + 1], dp[3 * (i - 1) + 2] + abc[i][1], dp[3 * (i - 1)] + abc[i][1])
        dp[3 * i + 2] = max(dp[3 * i + 2], dp[3 * (i - 1) + 1] + abc[i][2], dp[3 * (i - 1)] + abc[i][2])
    dp[3 * n] = max(dp)
    print(dp[3*n])

    return

#D
def D():
    """N個の品物があります。 品物には 1,2,…,Nと番号が振られています。 
    各 i (1≤i≤N) について、品物i の重さはwi で、価値はvi です。
    太郎君は、N 個の品物のうちいくつかを選び、ナップサックに入れて持ち帰ることにしました。 
    ナップサックの容量は W であり、持ち帰る品物の重さの総和は W以下でなければなりません。
    太郎君が持ち帰る品物の価値の総和の最大値を求めてください
    
    入力はすべて整数である。
    1≤N≤100
    1≤W≤10**5
    1≤wi≤W
    1≤vi≤10**9"""
    n, w = LI()
    wv = LIR(n)
    dp = [[0 for k in range(w + 1)] for i in range(n + 2)]
    for i in range(1,n + 1):
        for j in range(w + 1):
            if j < wv[i-1][0]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - wv[i - 1][0]] + wv[i - 1][1])
    print(dp[n+1][w])

    
    return

#E
def E():
    """N個の品物があります。 品物には 1,2,…,Nと番号が振られています。 
    各 i (1≤i≤N) について、品物i の重さはwi で、価値はvi です。
    太郎君は、N 個の品物のうちいくつかを選び、ナップサックに入れて持ち帰ることにしました。 
    ナップサックの容量は W であり、持ち帰る品物の重さの総和は W以下でなければなりません。
    太郎君が持ち帰る品物の価値の総和の最大値を求めてください
    
    入力はすべて整数である。
    1≤N≤100
    1≤W≤10**9
    1≤wi≤W
    1≤vi≤10**3"""
    n, w = LI()
    wv = LIR(n)
    dp = [[float("INF") for i in range(10 ** 5 + 1)] for k in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for k in range(10 ** 5 + 1):
            if k < wv[i][1]:
                dp[i + 1][k] = dp[i][k]
            else:
                dp[i + 1][k] = min(dp[i][k], dp[i][k - wv[i][1]] + wv[i][0])
    ans = 0
    for i in range(10 ** 5 + 1):
        if dp[n][i] <= w:
            ans = i
    print(ans)

    return

#F
def F():
    s = S()
    t = S()
    dp = [[0 for i in range(len(t)+1)] for k in range(len(s)+1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                if dp[i][j + 1] < dp[i + 1][j]:
                    dp[i + 1][j + 1] = dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
    ss = len(s)
    tt = len(t)
    ans = ""
    si = ss
    ti = tt
    while si > 0 and ti > 0:
        if dp[si][ti] == dp[si - 1][ti]:
            si -= 1
        elif dp[si][ti] == dp[si][ti - 1]:
            ti -= 1
        else:
            si -= 1
            ti -= 1
            ans = s[si]+ans


    print(ans)
    return

#G
def G():
    n, m = LI()
    xy = LIR_(m)
    edge = [[] for i in range(n)]
    for x,y in xy:
        edge[x].append(y)
    dp = [0 for i in range(n)]
    def ans(dp, i):
        #print(dp, i)
        if dp[i] != 0:
            return dp[i]
        else:
            if len(edge[i]) == 0:
                return 0
            ansb = 0
            for k in edge[i]:
                #print(dp, k , i)
                ansb = max(ansb, ans(dp, k) + 1)
                dp[i] = max(ansb, dp[i])
                #print(dp)
            return ansb
            
    for i in range(n):
        dp[i] = ans(dp, i)
    print(max(dp))
    return

#H
def H():
    h, w = LI()
    a = SR(h)
    dp = [[0 for i in range(w)] for k in range(h)]
    for i in range(w):
        if a[0][i] == "#":
            break
        dp[0][i] = 1
    for i in range(h):
        if a[i][0] == "#":
            break
        dp[i][0] = 1
    for i in range(1,w):
        for k in range(1, h):
            #print(i,k, dp)
            if a[k - 1][i] == ".":
                if a[k][i - 1] == ".":
                    dp[k][i] = dp[k - 1][i] + dp[k][i - 1] % mod
                else:
                    dp[k][i] = dp[k - 1][i]
            else:
                if a[k][i - 1] == ".":
                    dp[k][i] = dp[k][i - 1]
    print(dp[h-1][w-1] % mod)

    return

#I
def I():
    n = II()
    p = LF()
    dp = [[0 for k in range(n+1)] for i in range(n+1)]
    dp[1][1] = p[0]
    dp[1][0] = 1-p[0]
    for i in range(2,n+1):
        for k in range(i + 1):
            if k == 0:
                
                dp[i][k] = dp[i-1][k] * (1 - p[i-1])
            else:
                dp[i][k] = dp[i - 1][k - 1] * p[i - 1] + dp[i - 1][k] * (1 - p[i - 1])
    #print(dp)
    print(sum(dp[n][n//2+1:]))
    return 
#J
def J():
    n = II()
    a = LI()


#K
def K():
    n, k = LI()
    an = LI()
    dp = [0 for i in range(k + 1)]
    dp[0] = 0
    ans = ["First","Second"]
    for i in range(k + 1):
        if i in an:
            dp[i] = 0
        else:
            for num, a in enumerate(an):
                if a < i:
                    if dp[i - a] == 1:
                        dp[i] = 0
                        break
            else:
                dp[i] = 1
        #print(dp,i)

    print(ans[dp[k]])

#L
def L():
    N, K = LI()
    an = LI()
    dp = [[1 for k in range(K + 2)] for n in range(N)]
    an.sort()
    for a in range(K + 2):
        if a == 0:
            continue
        elif a <= an[0]:
            dp[0][a] = (dp[0][a - 1] + 1) % mod
    for n in range(1,N):
        for k in range(1,K + 2):
            if k - an[n] <= 0:
                dp[n][k] = (dp[n - 1][k] + dp[n][k - 1]) % mod
            else:
                dp[n][k] =  dp[n][k-1] + (dp[n - 1][k] - dp[n - 1][k - an[n]]) % mod
    print(dp)

#M
#N
# O
# P
# Q
# R
# S
# T
# U
# V
# W
# X
# Y
# Z


#Solve
if __name__ == '__main__':
    F()

