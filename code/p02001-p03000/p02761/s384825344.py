#!usr/bin/env python3
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
import numpy as np


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def LS(): return [list(x) for x in sys.stdin.readline().split()]


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


def main():
    # write codes here
    [N, M] = LI()

    if N != 1 and M == 0:
        print(str(10 ** (N - 1)))

    elif N == 1 and M == 0:
        print("0")

    else:

        SCset = set([tuple(LI()) for i in range(M)])
        SClist = list(SCset)

        Mactual = len(SCset)

        Ss = Counter([SClist[i][0] for i in range(Mactual)])

        Ss_np = np.array(list(Ss.values()))

        SCdict = {SClist[i][0]: SClist[i][1] for i in range(Mactual)}

        if np.sum(Ss_np > 1) > 0:
            print("-1")

        elif N > 1 and 1 in Ss.keys() and SCdict[1] == 0:
            print("-1")

        else:
            if 1 not in SCdict.keys():
                SCdict[1] = 1
            print(str(sum([SCdict[key] * 10 ** (N - key) for key in SCdict.keys()])))


# Main
if __name__ == "__main__":
    main()
