# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n = II()
A = [0] + LI() + [0]
C = [0]
for a1, a2 in zip(A[:-1], A[1:]):
    C.append(C[-1] + abs(a2 - a1))

for i in range(1, n + 1):
    if A[i - 1] <= A[i] <= A[i + 1]:
        print(C[-1])
    elif A[i - 1] >= A[i] >= A[i + 1]:
        print(C[-1])
    else:
        print(C[-1] - 2 * min(abs(A[i] - A[i - 1]), abs(A[i] - A[i + 1])))