import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
from collections import Counter
import bisect
def main():
    S_ = S()
    if S_[-1] == 's':
        S_ += 'es'
    else:
        S_ += 's'
    print(S_)
if __name__ == "__main__":
    main()

