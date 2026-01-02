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
    N = I()
    cnt = 0
    for i in range(N):
        d_1, d_2 = MI()
        if d_1 == d_2:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            print('Yes')
            exit()
    print('No')
if __name__ == "__main__":
    main()

