#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
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

class SlidingWindowAggretgation:
    def __init__(self, default = float("inf"), f = min):
        self.default = default
        self.f = f
        self.front_stack = deque()
        self.back_stack = deque()

    def get(self):
        res = self.default
        if self.front_stack:
            res = self.f(res, self.front_stack[-1][1])
        if self.back_stack:
            res = self.f(res, self.back_stack[-1][1])
        return res

    def append(self, x):
        fx = x
        if self.back_stack:
            fx = self.f(self.back_stack[-1][1], x)
        self.back_stack.append((x, fx))

    def popleft(self):
        if not self.front_stack:
            x, fx = self.back_stack.pop()
            self.front_stack.append((x, x))
            while self.back_stack:
                x, fx = self.back_stack.pop()
                fx = self.f(x, self.front_stack[-1][1])
                self.front_stack.append((x, fx))
        self.front_stack.pop()

def solve():
    n,l = LI()
    a = LI()
    swag = SlidingWindowAggretgation()
    ans = []
    for i in range(n):
        swag.append(a[i])
        if i+1 >= l:
            ans.append(swag.get())
            swag.popleft()
    print(*ans)
    return

#Solve
if __name__ == "__main__":
    solve()

