import sys
import re
import random
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)


class Segtree_op():
    # 単位元及び操作を設定して使うこと
    # queryでは、区間の(l, r)を指定する ex: (0, 5) => [0, 1, 2, 3, 4]
    # 特定の1点は (i, i+1)
    def __init__(self, n):
        self.n = n

        self.size = 1
        while (n >= 1):
            self.size = self.size << 1
            n = n // 2

        self.arr = [self.unit() for i in range(self.size * 2)]

    def op(self, lch, rch):
        # update min with holding index
        return min(lch, rch)

    def unit(self):
        return self.n

    def update(self, k, val):
        k += self.size - 1
        self.arr[k] = val
        while (k):
            k = (k - 1) // 2
            self.arr[k] = self.op(self.arr[k * 2 + 1], self.arr[k * 2 + 2])

    def query(self, l, r):
        L = l + self.size
        R = r + self.size
        s = self.unit()
        while L < R:
            if R & 1:
                R -= 1
                s = self.op(s, self.arr[R - 1])

            if L & 1:
                s = self.op(s, self.arr[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return s

    def show(self):
        idx = 1
        while (idx <= self.size):
            print(self.arr[idx - 1:idx * 2 - 1])
            idx *= 2


def solve():
    n, q = getList()

    st_tate = Segtree_op(n)
    st_yoko = Segtree_op(n)

    reversed = 0
    for _ in range(q):
        op, idx = getList()
        if op == 1:
            border = st_tate.query(idx, n+1)
            reversed += border - 2
            val = min(st_yoko.query(border, border+1), idx)
            st_yoko.update(border, val)
        else:
            border = st_yoko.query(idx, n+1)
            reversed += border - 2
            val = min(st_tate.query(border, border + 1), idx)
            st_tate.update(border, val)

        # st_tate.show()
        # st_yoko.show()
        # print(reversed)
        # print("=========")

    print((n-2) ** 2 - reversed)








def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()