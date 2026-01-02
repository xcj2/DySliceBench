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
    N, Q = MI()
    #i行の一番右をline_right[i],　j列目の一番下をcolumn_under[j]とする。
    line_right = deque([(N, N)])
    line_right_keys = deque([N])
    column_under = deque([(N, N)])
    column_under_keys = deque([N])
    bla = pow(N - 2, 2)
    x_min = N
    y_min = N
    for i in range(Q):
        query = LI()
        if query[0] == 1:
            w = query[1]
            x = bisect.bisect_left(column_under_keys, w)
            bla -= column_under[x][1] - 2
            if w < x_min:
                line_right.appendleft((column_under[x][1], w))
                line_right_keys.appendleft(column_under[x][1])
                x_min = w
        else:
            y = query[1]
            z = bisect.bisect_left(line_right_keys, y)
            bla -= line_right[z][1] - 2
            if y < y_min:
                column_under.appendleft((line_right[z][1], y))
                column_under_keys.appendleft(line_right[z][1])
                y_min = y
    print(bla)
if __name__ == "__main__":
    main()