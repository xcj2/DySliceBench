import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def solve(cumsum, prev_plus):
    cnt = 0
    total_sum = 0
    for i, c in enumerate(cumsum):
        c = c + total_sum
        if prev_plus:
            # if minus, ignore
            if c < 0:
                pass
            else:
                cnt += (c - (-1))
                total_sum -= (c - (-1))
        else:
            if c > 0:
                pass
            else:
                cnt += (1 - c)
                total_sum += (1 - c)
        prev_plus = not prev_plus
    return cnt


def main():
    N = I()
    A = LI()
    cumsum = [0]
    for i in range(N):
        cumsum.append(A[i] + cumsum[i])
    cumsum = cumsum[1:]
    prev_plus = cumsum[0] > 0
    a1 = solve(cumsum, True)
    a2 = solve(cumsum, False)
    print(min(a1, a2))

main()

