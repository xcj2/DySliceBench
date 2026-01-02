import sys
input = lambda : sys.stdin.readline().strip()

from collections import deque
from operator import le, ge

class Convex_Hull_Trick():
    def __init__(self, op=ge):
        self.que = deque()
        self.op = op

    @staticmethod
    def f(f1, x):
        return f1[0]*x + f1[1]

    def check(self, f1, f2, f3):
        a = (f2[0] - f1[0]) * (f3[1] - f2[1])
        b = (f2[1] - f1[1]) * (f3[0] - f2[0])
        return self.op(a, b)

    def add_line(self, a, b):
        que = self.que
        fi = (a, b)
        while len(que) >= 2 and self.check(que[-2], que[-1], fi):
            que.pop()
        que.append(fi)

    def get(self, x):
        que = self.que
        f = self.f
        while len(que) >= 2 and self.op(f(que[0], x), f(que[1], x)):
            que.popleft()
        return f(que[0], x)

n,c = map(int, input().split())
h = list(map(int, input().split()))

CHT = Convex_Hull_Trick()
CHT.add_line(-2*h[0], h[0]**2)

DP = [0]*n

for i in range(1, n):
    min_cost = CHT.get(h[i])
    DP[i] = min_cost + h[i]*h[i] + c
    CHT.add_line(-2*h[i], h[i]**2+DP[i])

print(DP[-1])