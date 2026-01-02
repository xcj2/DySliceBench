#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
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
inf = 1e10

class SlidingWindowAggregation:
    """ https://scrapbox.io/data-structures/Sliding_Window_Aggregation """
    
    def __init__(self, f=sum):
        self.f = f
        self.front_stack = deque()
        self.back_stack = deque()
    
    def empty(self):
        return self.front_stack or self.back_stack

    def __len__(self):
        return len(self.front_stack) + len(self.back_stack)

    def fold_all(self):
        try:
            assert self.empty(), "Both stack is empty"
            if not self.front_stack:
                return self.back_stack[-1][1]
            elif not self.back_stack:
                return self.front_stack[-1][1]
            else:
                return self.f(self.front_stack[-1][1], self.back_stack[-1][1])
        except AssertionError as err:
            print("AssertionError :", err)

    def push(self, x):
        if not self.back_stack:
            self.back_stack.append((x, x))
        else:
            tmp = self.f(self.back_stack[-1][1], x)
            self.back_stack.append((x, tmp))

    def popleft(self):
        try:
            assert self.empty(), "Both stack is empty"
            if not self.front_stack:
                x,fx = self.back_stack.pop()
                self.front_stack.append((x, x))
                while self.back_stack:
                    x, fx = self.back_stack.pop()
                    fx = self.f(x, self.front_stack[-1][1])
                    self.front_stack.append((x, fx))
            self.front_stack.pop()

        except AssertionError as err:
            print("AssertionError :", err)

#solve
def solve():
    n = II()
    lr = LIR(n)
    maxl = max([l for l, r in lr])
    minr = min([r for l, r in lr])
    ans = max(minr - maxl + 1, 0) + max([r - l + 1 for l, r in lr])
    lisminr = SlidingWindowAggregation(min)
    lr.sort()
    for _, r in lr:
        lisminr.push(r)

    for l, r in lr[:-1]:
        lisminr.popleft()
        ans = max(ans, max(minr - l + 1, 0) + max(lisminr.fold_all() - maxl + 1, 0))
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
