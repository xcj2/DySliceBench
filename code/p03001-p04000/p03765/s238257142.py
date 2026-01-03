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
    x = S()
    s = 0
    ans = len(x)
    for i in x:
        if i == "S":
            s += 1
        else:
            if s > 0:
                s -= 1
                ans -= 2
    print(ans)
    return

#B
def B():
    n = I()
    a = LI()
    f = [0 for i in range(n+1)]
    for i in range(n):
        f[a[i]] = i
    l = [i for i in range(n+1)]
    r = [i for i in range(n+1)]
    ans = 0
    for i in range(1,n+1)[::-1]:
        j = f[i]
        ans += (j-l[j]+1)*(r[j]-j+1)*i
        l[r[j]+1] = l[j]
        r[l[j]-1] = r[j]
    print(ans)
    return

#C
def C():
    n,x = LI()
    if x == 1 or x == 2*n-1:
        print("No")
        quit()
    else:
        ans = [i+1 for i in range(2*n-1)]
        k = x-n
        if k < 0:
            ans = ans[2*n-1+k:]+ans[:2*n-1+k]
        if k > 0:
            ans = ans[k:]+ans[:k]
        print("Yes")
        for i in ans:
            print(i)
    return

#D
def D():
    s = S()
    t = S()
    n = len(s)
    m = len(t)
    fs = [1 if s[i] == "A" else 2 for i in range(n)]
    ft = [1 if t[i] == "A" else 2 for i in range(m)]
    for i in range(n-1):
        fs[i+1] += fs[i]
        fs[i+1] %= mod
    for i in range(m-1):
        ft[i+1] += ft[i]
        ft[i+1] %= mod
    fs.insert(0,0)
    ft.insert(0,0)
    q = I()
    for i in range(q):
        a,b,c,d = LI()
        a -= 1
        c -= 1
        if (fs[b]-fs[a])%3 == (ft[d]-ft[c])%3:
            print("YES")
        else:
            print("NO")
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == "__main__":
    D()
