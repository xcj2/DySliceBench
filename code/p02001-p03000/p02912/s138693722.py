import sys

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

import heapq
from math import floor, ceil

def main():
    n, m = LI()
    a_s = LI()
    minus_as = [-i for i in a_s]
    heapq.heapify(minus_as)
    ans = 0
    for i in range(m):
        v = heapq.heappop(minus_as)
        v = ceil(v / 2)
        heapq.heappush(minus_as, v)
    print(-1 * int(sum(minus_as)))





if __name__ == '__main__':
    main()