import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
from collections import Counter
import bisect
from functools import reduce

def main():
    H = I()
    cnt = 0
    while H > 1:
        H //= 2
        cnt += 1
    ans = pow(2, cnt + 1) - 1
    print(ans)


if __name__ == "__main__":
    main()

