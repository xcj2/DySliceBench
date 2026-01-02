import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
from functools import partial, reduce
from operator import mul
prod = partial(reduce, mul)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

def main():
    N, M = LI()
    for i in range(N, int(M ** 0.5) + 1):
        if M % i == 0:
            return M // i
    for i in range(min(N - 1, int(M ** 0.5), M // N), 0, -1):
        if M % i == 0:
            return i
    return 1

print(main())