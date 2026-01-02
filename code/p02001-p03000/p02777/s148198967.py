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
def main():
    X = LS()
    S_ = X[0]
    T = X[1]
    A, B = MI()
    U = S()
    if U == S_:
        print(A - 1, B)
    else:
        print(A, B - 1)


if __name__ == "__main__":
    main()

