import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict
from collections import deque
import bisect
from decimal import *
from functools import reduce
def main():
    N = I()
    Dots = defaultdict()
    xpyp = []
    xpyn = []
    xnyp = []
    xnyn = []
    for i in range(N):
        x, y = MI()
        Dots[i] = (x, y)
        xpyp.append(x + y)
        xpyn.append(x - y)
        xnyp.append(- x + y)
        xnyn.append(- x - y)
    xpyp_max = max(xpyp) - min(xpyp)
    xpyn_max = max(xpyn) - min(xpyn)
    xnyp_max = max(xnyp) - min(xnyp)
    xnyn_max = max(xnyn) - min(xnyn)
    print(max(xpyp_max, xpyn_max, xnyp_max, xnyn_max))

if __name__ == "__main__":
    main()

