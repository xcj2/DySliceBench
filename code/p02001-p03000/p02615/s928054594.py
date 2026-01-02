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
    N = I()
    A = LI()
    A.sort(reverse=True)
    ans = A[0]
    cnt = 1
    i = 1
    while cnt < N - 1:
        ans += A[i] * 2
        cnt += 2
        i += 1
    if cnt > N - 1:
        ans -= A[i - 1]
    print(ans)
if __name__ == "__main__":
    main()

