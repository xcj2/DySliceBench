def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

from collections import defaultdict, deque
from sys import exit
import math
import copy
from bisect import bisect_left

import sys
# sys.setrecursionlimit(1000000)
INF = 10 ** 17

def check(books, x, i, m, n):
    ab = [0 for i in range(m)]
    ret = 0
    for k in range(n):
        if i % 2 == 1:
            book = books[k]
            for tab, b in enumerate(book[1:]):
                ab[tab] += b
            ret += book[0]
        i //= 2
    # print(bin(i), ab)
    for cab in ab:
        if cab < x:
            return INF

    return ret

def main():
    n, m, x = getList()
    books = [getList() for _ in range(n)]
    ans = INF
    for i in range(2**n):
        # print(i)
        tmp = check(books, x, i, m, n)
        if ans > tmp:
            ans = tmp

    if ans == INF:
        print(-1)
    else:
        print(ans)
if __name__ == "__main__":
    main()

