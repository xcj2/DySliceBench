#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys, math, bisect, random, itertools
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
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
    a, b, c = LI()
    print(c - min(b + c, a) + b)
    return

#B
def B():
    n = II()
    ans = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2:
            ans += 1
    print(ans)
    return

#C
def C():
    n = II()
    h = LI()
    h = h[::-1]
    for i in range(1, n):
        if h[i] <= h[i-1]:
            continue
        if h[i] == h[i - 1] + 1:
            h[i] -= 1
            continue
        print("No")
        return
    print("Yes")
    return

#D
def D():
    s = S()
    lens = len(s)
    ans = [0] * len(s)
    i = 0
    while i != len(s):
        for j in range(i, lens):
            if s[j] == "R":
                continue
            break
        R = j - i
        for i in range(j, lens):
            if s[i] == "L":
                continue
            break
        else:
            i += 1
        L = i - j
        ans[j] = R // 2 + (L+1) // 2
        ans[j - 1] = L // 2 + (R+1) // 2

    print(*ans)
    return

#E
def E():
    def make_divisor(n):
        res = []
        for i in range(1, int(math.sqrt(n))+1):
            if n % i == 0:
                res.append(i)
                res.append(n // i)
        if n == math.sqrt(n)** 2:
            res.append(int(math.sqrt(n)))
        return res
    n, k = LI()
    a = LI()
    x = sum(a)
    maxa = max(a)
    lis = make_divisor(x)
    lis.sort(reverse=True)
    for li in lis:
        l1 = list(map(lambda x: x % li, a))
        l2 = list(map(lambda x: - x % li, a))
        l1.sort()
        l2.sort()
        c = 0
        while 0 in l1:
            l1.remove(0)
            c += 1
        while 0 in l2:
            l2.remove(0)
        l = 0
        r = 0
        b = 0
        rx = 0
        lx = 0
        while l + r < n - c:
            if b < 0:
                b += l2[r]
                rx += l2[r]
                r += 1
            else:
                b -= l1[l]
                lx += l1[l]
                l += 1
        if b == 0 and rx <= k:
            print(li)
            return
    return

#F
def F():
    return

#Solve
if __name__ == '__main__':
    E()
