#!usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007
#A
def A():
    t,x = LI()
    print(t/x)

#B
def B():
    n = I()
    a = LI()
    m = max(a)
    if m >= sum(a)-m:
        print("No")
    else:
        print("Yes")


#C
def C():
    n,m = LI()
    x = LI()
    x.sort()
    l = [x[i+1]-x[i] for i in range(m-1)]
    l.sort()
    l = l[::-1]
    ans = sum(l[max(n-1,0):])
    print(ans)

#D
def D():
    n,k = LI()
    a = LI()
    k = list(map(int,list(bin(k)[2:])))
    l = len(k)
    for i in range(n):
        a[i] = list(map(int,list(bin(a[i])[2:])))
        l = max(l,len(a[i]))
    for i in range(n):
        for j in range(l-len(a[i])):
            a[i].insert(0,0)
    for j in range(l-len(k)):
        k.insert(0,0)
    s = [[0,0] for i in range(l)]
    pow2 = [1 for i in range(l)]
    for i in range(l-1)[::-1]:
        pow2[i] = pow2[i+1]*2
    for i in a:
        for j in range(l):
            s[j][0] += pow2[j]*i[j]
            s[j][1] += pow2[j]*(not i[j])
    dp = [0 for i in range(l+1)]
    small = False
    for i in range(l):
        if not small:
            if not k[i]:
                dp[i+1] += dp[i]+s[i][0]
            else:
                if s[i][0] >= s[i][1]:
                    dp[i+1] += dp[i]+s[i][0]
                    small = True
                else:
                    dp[i+1] += dp[i]+s[i][1]
        else:
            dp[i+1] += dp[i]+max(s[i])
    print(dp[l])

#E
if __name__ == "__main__":
    C()

#F

#G

#H

#I

#J

#K

#L

#M

#N

#O

#P

#Q

#R

#S

#T
