import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N, M = MI()
    A = LI()
    a = sum(A) / (4 * M)
    A.sort()
    cnt = bisect.bisect_left(A, a)
    if N - cnt >= M:
        print('Yes')
    else:
        print('No')
if __name__ == "__main__":
    main()