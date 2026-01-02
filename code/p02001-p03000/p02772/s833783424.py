import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
from collections import Counter
def main():
    N = I()
    A = LI()
    for a in A:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 !=0:
                print('DENIED')
                exit()
    print('APPROVED')

if __name__ == "__main__":
    main()
