import sys
from collections import defaultdict, deque, Counter
import math

# import copy
from bisect import bisect_left, bisect_right
# import heapq

sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)


def nck(n, k, kaijyo):
    return (npk(n, k, kaijyo) * divide(kaijyo[k])) % MOD


def npk(n, k, kaijyo):
    if k == 0 or k == n:
        return n % MOD
    return (kaijyo[n] * divide(kaijyo[n-k])) % MOD


def kaijyo(n):
    ret = [1]
    for i in range(1, n + 1):
        ret.append((ret[-1] * i)% MOD)
    return ret


class Segtree_op():
    # 単位元及び操作を設定して使うこと
    # queryでは、区間の(l, r)を指定する ex: (0, 5) => [0, 1, 2, 3, 4]
    # 特定の1点は (i, i+1)
    def __init__(self, n):
        self.size = 1
        while (n >= 1):
            self.size = self.size << 1
            n = n // 2

        self.arr = [self.unit() for i in range(self.size * 2)]

    def op(self, lch, rch):
        return lch + rch
    def unit(self):
        return 0

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

class BIT():
    # A1 ... AnのBIT(1-indexed)
    def __init__(self, n):
        self.n = n
        self.BIT = [0] * (n + 2)

    # A1 ~ Aiまでの和 O(logN)
    def query(self, idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx & (-idx)
        return res_sum

    # Ai += x O(logN)
    def update(self, idx, x):
        # print(idx)
        while idx <= self.n:
            # print(idx)
            self.BIT[idx] += x
            idx += idx & (-idx)
        return

    def show(self):
        print(self.BIT)

def solve():
    n, q = getList()
    nums = getList()
    qs = []
    ans = [0 for i in range(q)]
    las = [0 for i in range(n+3)]
    qs_append = qs.append
    for i in range(q):
        ql, qr = getList()
        qs_append((ql, qr, i))

    qs.sort(key=lambda x: x[1])


    st = BIT(n)
    tmpr = 0
    for qq in qs:
        l, r, id = qq
        # print(qq)
        if r > tmpr:
            for i in range(tmpr + 1, r + 1):
                cur = nums[i - 1]
                st.update(i, 1)
                # print("s")
                if las[cur] != 0:
                    st.update(las[cur], -1)
                las[cur] = i
                # print(r)
            tmpr = r
        # st.show()
        # print(st.query(r) - st.query(l-1), l, r)
        ans[id] = st.query(r) - st.query(l-1)


    # ans.sort(key=lambda x: x[1])
    for an in ans:
        print(an)
def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()