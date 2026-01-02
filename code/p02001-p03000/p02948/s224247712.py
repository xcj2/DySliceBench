import sys
# from collections import defaultdict, deque
# import math
# import copy
# from bisect import bisect_left, bisect_right
# import heapq

# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 1000000007


class Segtree_op():
    def __init__(self, n):
        self.size = 1
        while (n >= 1):
            self.size = self.size << 1
            n = n // 2

        self.arr = [self.unit() for i in range(self.size * 2)]

    def op(self, lch, rch):
        # update min with holding index
        return max(lch, rch)

    def unit(self):
        return -INF

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
    n, m = getList()
    baito = []
    for i in range(n):
        a, b = getList()
        baito.append((b, a))

    baito.sort(reverse=True)
    st = Segtree_op(m)
    for i in range(m):
        st.update(i, i)

    ans = 0
    for kin, hi in (baito):
        if hi > m:
            continue
        tgt = st.query(0, m - hi + 1)
        if tgt != -INF:
            ans += kin
            st.update(tgt,-INF)

    # st.show()
    # st.update(0, -10)
    # print(st.query(0, 1))
    print(ans)

def main():
    n = getN()
    for _ in range(n):
        solve()
if __name__ == "__main__":
    # main()
    solve()
