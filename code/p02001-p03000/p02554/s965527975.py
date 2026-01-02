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
def main():
    N = I()
    mod = 10 ** 9 + 7
    print((pow(10, N, mod) - (2 * pow(9, N, mod) % mod) + pow(8, N, mod)) % mod)
if __name__ == "__main__":
    main()

