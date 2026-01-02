#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    def f(s):
        return ord(s)-ord("A")
    n,a,b,c = LI()
    l = [a,b,c]
    ans = []
    s = [list(map(f, input())) for i in range(n)]
    for i in range(n):
        si = s[i]
        si.sort()
        if l[si[0]] == l[si[1]] == 0:
            print("No")
            return
        if l[si[0]] == l[si[1]] == 1 and min(l) == 0 and i+1 < n:
            nsi = s[i+1]
            nsi.sort()
            if nsi == si:
                if l[si[0]] < l[si[1]]:
                    l[si[0]] += 1
                    l[si[1]] -= 1
                    ans.append(chr(si[0]+ord("A")))
                else:
                    l[si[1]] += 1
                    l[si[0]] -= 1
                    ans.append(chr(si[1]+ord("A")))
            else:
                k = [0]*3
                for i in si+nsi:
                    k[i] += 1
                    if k[i] == 2:
                        break
                l[i] += 1
                for j in si:
                    if j != i:
                        break
                l[j] -= 1
                ans.append(chr(i+ord("A")))
        elif l[si[0]] < l[si[1]]:
            l[si[0]] += 1
            l[si[1]] -= 1
            ans.append(chr(si[0]+ord("A")))
        else:
            l[si[1]] += 1
            l[si[0]] -= 1
            ans.append(chr(si[1]+ord("A")))
    print("Yes")
    for i in ans:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
