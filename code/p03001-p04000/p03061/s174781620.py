# coding: utf-8
import sys

# from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
printout = sys.stdout.write
sprint = sys.stdout.flush
# from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
import math
# from itertools import product, accumulate, combinations, product
#import bisect
# import numpy as np
# from copy import deepcopy
#from collections import deque
# from decimal import Decimal
# from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 998244353


def intread():
    return int(sysread())
def mapline(t=int):
    return map(t, sysread().split())
def mapread(t=int):
    return map(t, read().split())



def run():
    N, *A = mapread()
    LEFT = [0] * (N+2)
    RIGHT = [0] * (N+2)
    for i, a in enumerate(A, 1):
        LEFT[i] = math.gcd(LEFT[i-1], a)
    for i in range(N-1, -1, -1):
        k = i+1# for RIGHT
        RIGHT[k] = math.gcd(RIGHT[k+1], A[i])
    #print(LEFT)
    #print(RIGHT)
    ans = 0
    for i in range(N):
        k = i + 1# for LEFT and RIGHT
        v = math.gcd(LEFT[k-1], RIGHT[k+1])
        #print(v)
        ans = max(ans, v)

    print(ans)



if __name__ == "__main__":
    #print(math.gcd(0, 10))
    run()
