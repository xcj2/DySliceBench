import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

from collections import Counter
from itertools import product

def main():
    N = II()
    A = LI()
    n_neg = 0
    for a in A:
        if a < 0:
            n_neg += 1
        elif a == 0:
            n_neg = 0
            break
    if n_neg % 2 == 0:
        ans = sum(abs(a) for a in A)
    else:
        A = [abs(a) for a in A]
        A.sort()
        ans = sum(A[1:]) - A[0]

    return ans

print(main())