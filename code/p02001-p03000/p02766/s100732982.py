import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
import bisect
def main():
    N, K = MI()
    ans = 0
    p = 1
    while p <= N:
        p *= K
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()
