#!usr/bin/env python3
from collections import defaultdict
from collections import deque
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
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    return

#B
def B():
    return

#C
def C():
    n,m = LI()
    t = [0 for i in range(n+1)]
    for i in range(m):
        l,r = LI()
        t[l-1] += 1
        t[r] -= 1
    for i in range(n):
        t[i+1] += t[i]
        if t[i] == m:
            t[i] = 1
        else:
            t[i] = 0
    print(sum(t[:n]))
    return

#D
def D():
    n,m = LI()
    a = LI()
    q = []
    for i in range(n):
        heappush(q,a[i])
    l = LIR(m)
    l.sort(key = lambda x:-x[1])
    for b,c in l:
        for i in range(b):
            x = heappop(q)
            if x < c:
                x = c
                heappush(q,x)
            else:
                heappush(q,x)
                break
    print(sum(q))
    return

#E
def E():
    n,m,k = LI()
    M = n*m
    fact = [1]*(M+1)
    for i in range(M):
        fact[i+1] = fact[i]*(i+1)%mod
    inv = [1]*(M+1)
    inv[M] = pow(fact[M],mod-2,mod)
    for i in range(M)[::-1]:
        inv[i] = inv[i+1]*(i+1)%mod
    ans = fact[M-2]*inv[k-2]*inv[M-k]%mod
    s = 0
    for i in range(1,M):
        s += i*(max(0,n-i)*m**2+max(0,m-i)*n**2)%mod
        s %= mod
    ans = ans*s%mod
    print(ans)
    return

#F
def F():
    q = I()
    m = 0
    l = [-float("inf"),float("inf")]
    x = 0
    num = 0
    for _ in range(q):
        Q = LI()
        if len(Q) == 1:
            print(x,m)
        else:
            z,a,b = Q
            m += b
            if num == 0:
                num += 1
                l = [a,float("inf")]
                x = a
            elif num == 1:
                if a != l[0]:
                    num += 1
                    l = [min(a,l[0]),max(a,l[0])]
                    x = l[0]
                    m += l[1]-l[0]
            else:
                num += 1
                if num % 2:
                    if l[0] <= a < l[1]:
                        m += min(a-l[0],l[1]-a)
                        x = a
                    elif a < l[0]:
                        m += l[0]-a
                        x = l[0]
                        l = [a,l[1]]
                    else:
                        m += a-l[1]
                        x = l[1]
                        l = [l[0],a]
                else:
                    if l[0] <= a < l[1]:
                        if a < x:
                            m += x-a
                            l = [a,x]
                            x = a
                        else:
                            m += a-x
                            l = [x,a]
                    elif a < l[0]:
                        m += x-a
                        x = l[0]
                        l = [l[0],x]
                    else:
                        m += a-x
                        l = [x,l[1]]
    return

#G
def G():
    return

#H
def H():
    return

#I
def I_():
    return

#J
def J():
    return

#Solve
if __name__ == "__main__":
    E()
