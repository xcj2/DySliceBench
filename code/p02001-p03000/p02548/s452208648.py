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
from collections import defaultdict

def main():
    N = I()
    ans = 0
    for i in range(1, N):
        x, y = divmod(N, i)
        ans += x
        if y == 0:
            ans -= 1


    print(ans)

if __name__ == "__main__":
    main()
