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
import itertools
def main():
    N, X, M = MI()
    circle = [X]
    ans = 0
    i = 1
    num_list = [0] * (M + 1)
    a = X
    while num_list[a] == 0:
        num_list[a] = i
        a = pow(a, 2, M)
        circle.append(a)
        i += 1
    b = num_list[a]
    del circle[-1]
    sta = circle[:b - 1]
    v = len(sta)
    w = sum(sta)
    circle = circle[b - 1:]
    x = len(circle)
    y = sum(circle)
    if N <= v:
        ans = sum(sta[:N + 1])
        print(ans)
        exit()
    else:
        ans = w
        p, q = divmod(N - v, x)
        ans += y * p
        if q != 0:
            for i in range(q):
                ans += circle[i]

        print(ans)
if __name__ == "__main__":
    main()
