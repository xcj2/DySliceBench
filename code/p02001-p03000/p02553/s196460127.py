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
    a, b, c, d = MI()
    print(max(a * c, b * d, a * d, b * c))
if __name__ == "__main__":
    main()

