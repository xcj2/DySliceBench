#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
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

def solve():
    n = I()
    b = IR(n)
    b.sort()
    a = deque(b)
    q = deque([a.pop()])
    n -= 1
    for i in range(n):
        if i&1:
            ai = a.pop()
        else:
            ai = a.popleft()
        x = q[0]
        y = q[-1]
        if abs(x-ai) < abs(y-ai):
            q.append(ai)
        else:
            q.appendleft(ai)
    ans = 0
    for i in range(n):
        ans += abs(q[i+1]-q[i])
    a = deque(b)
    q = deque([a.popleft()])
    for i in range(n):
        if i&1:
            ai = a.popleft()
        else:
            ai = a.pop()
        x = q[0]
        y = q[-1]
        if abs(x-ai) < abs(y-ai):
            q.append(ai)
        else:
            q.appendleft(ai)
    ans2 = 0
    for i in range(n):
        ans2 += abs(q[i+1]-q[i])
    a = deque(b)
    q = deque([a.pop()])
    for i in range(n):
        if i&2:
            ai = a.pop()
        else:
            ai = a.popleft()
        x = q[0]
        y = q[-1]
        if abs(x-ai) < abs(y-ai):
            q.append(ai)
        else:
            q.appendleft(ai)
    ans3 = 0
    for i in range(n):
        ans3 += abs(q[i+1]-q[i])
    a = deque(b)
    q = deque([a.popleft()])
    for i in range(n):
        if i&2:
            ai = a.popleft()
        else:
            ai = a.pop()
        x = q[0]
        y = q[-1]
        if abs(x-ai) < abs(y-ai):
            q.append(ai)
        else:
            q.appendleft(ai)
    ans4 = 0
    for i in range(n):
        ans4 += abs(q[i+1]-q[i])
    print(max(ans,ans2,ans3,ans4))
    return


#Solve
if __name__ == "__main__":
    solve()
