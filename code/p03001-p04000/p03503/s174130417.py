import sys
import numpy as np
import itertools as it

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

n = I()
F, P = [], []
for _ in range(n):
    F.append(LI())

for _ in range(n):
    P.append(LI())

F = np.array(F)

b = (0, 1)
b10 = (b,)*10
iter_ = it.product(*b10)

Fdotx = [F.dot(x) for x in iter_][1:]

print(max([sum([P[i][val] for i, val in enumerate(row)]) for row in Fdotx]))