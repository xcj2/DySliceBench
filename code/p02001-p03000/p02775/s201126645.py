import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
from collections import defaultdict
def main():
    N = S()
    N =  N[::-1]
    N += '0'
    cnt = 0
    next = 0
    for i in range(len(N)):
        num = int(N[i])
        num += next
        if num <= 4:
            cnt += num
            next = 0
        elif num >= 6:
            cnt += 10 - num
            next = 1
        else:
            if int(N[i + 1]) <= 4:
                cnt += num
                next = 0
            else:
                cnt += 10 - num
                next = 1

    print(cnt)
if __name__ == "__main__":
    main()
