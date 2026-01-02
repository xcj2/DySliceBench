# coding: utf-8
import sys

# from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
printout = sys.stdout.write
sprint = sys.stdout.flush
# from heapq import heappop, heappush
# from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
# import math
# from itertools import product, accumulate, combinations, product
# import bisect
# import numpy as np
# from copy import deepcopy
#from collections import deque
# from decimal import Decimal
# from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7


def intread():
    return int(sysread())
def mapline(t=int):
    return map(t, sysread().split())
def mapread(t=int):
    return map(t, read().split())

def run():
    N = int(sysread())
    ans = 0
    for a in range(1, N):
        for b in range(1, N//a+1):
            c = N - a * b
            if c > 0:
                ans += 1
    print(ans)
if __name__ == "__main__":
    run()
