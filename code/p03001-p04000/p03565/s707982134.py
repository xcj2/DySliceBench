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
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
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
inf = float('INF')

#A
def A():
    return

#B
def B():
    return

#C
def C():
    s = S()
    t = S()
    ansa = []
    anslis = []
    lisans = []
    for i in range(len(s)):
        for j in range(len(t)):
            if 0 <= i + j < len(s) and (s[i + j] == t[j] or s[i + j] == "?"):
                continue
            break
        else:
            ansa.append((i, i + j))
    if len(ansa) == 0:
        print("UNRESTORABLE")
        return
    for ans in ansa:
        a = ""
        for num in range(len(s)):
            i = s[num]
            if ans[0] <= num <= ans[1]:
                i = t[num-ans[0]]
            a += i
        anslis.append(a)
    for ans in anslis:
        k = ""
        for i in ans:
            if i == "?":
                k += "a"
            else:
                k += i
        lisans.append(k)
    lisans.sort()
    print(lisans[0])
        
    return

#D
def D():
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
if __name__ == '__main__':
    A()


#A
"""
r = I()
g = I()
print(2*g-r)
"""

#B
"""
n = I()
k = I()
ans = 1
for i in range(n):
    ans = min(ans * 2, ans + k)
print(ans)
"""



    


#D
"""
n = I()
t = LI()
v = LI()
"""
if __name__ == "__main__":
    C()
