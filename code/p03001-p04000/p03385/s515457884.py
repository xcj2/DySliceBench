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
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007
sys.setrecursionlimit(1000000)

#A
def A():
    s = S()
    a = s.count("a")
    b = s.count("b")
    c = 3-a-b
    if a&b&c:
        print("Yes")
    else:
        print("No")
#B
def B():
    a,b,k = LI()
    ans = []
    for i in range(a,min(a+k,b+1)):
        ans.append(i)
    for i in range(max(a,b-k+1),b+1):
        ans.append(i)
    ans = list(set(ans))
    ans.sort()
    for i in ans:
        print(i)

#C
def C():
    a,b,c = LI()
    ans = 0
    if a%2:
        if b%2:
            if not c%2:
                ans += 1
                a += 1
                b += 1
        else:
            ans += 1
            if not c%2:
                b += 1
                c += 1
            else:
                a += 1
                c += 1
    else:
        if b%2:
            ans += 1
            if not c%2:
                a += 1
                c += 1
            else:
                b += 1
                c += 1
        else:
            if c%2:
                ans += 1
                a += 1
                b += 1
    ans += (3*max(a,b,c)-a-b-c)//2
    print(ans)
#D
def D():
    q = I()
    for i in range(q):
        a,b = LI()
        x = int((a*b)**0.5)
        y = math.ceil((a*b)/x)-1
        ans = x+y-2
        if a==b:
            ans += 1
        print(ans)

#E
def E():
    s = S()
    f = {"N":0,"W":0,"S":0,"E":0}
    for i in s:
        f[i] = 1
    if f["N"]^f["S"]:
        print("No")
    elif f["W"]^f["E"]:
        print("No")
    else:
        print("Yes")
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
    A()
