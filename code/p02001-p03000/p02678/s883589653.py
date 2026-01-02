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
from heapq import *
import sys
# sys.setrecursionlimit(1000000)
INF = 10 ** 17
MOD = 998244353

def check(mid, points, origin, rotate):
    height = origin * math.cos(math.radians(rotate))
    # print(height)
    cs = math.cos(math.radians(rotate))
    sn = math.sin(math.radians(rotate))
    for px, py in points:
        py = py - origin
        rx, ry = px*cs - py * sn, px * sn + py * cs
        if abs(rx) > height + 0.0000001 or abs(ry) > height + 0.0000001:
            # print("FALSE", rotate)
            return False

    return True


class Segtree_op():
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


def solve():
    n, m = getList()
    graph = [[] for i in range(n)]
    michi = [-1  for i in range(n)]
    det = [INF for i in range(n)]
    det[0] = 0

    for _ in range(m):
        a, b = getList()
        a, b = a-1, b-1
        graph[a].append(b)
        graph[b].append(a)

    h = []
    for nx in graph[0]:
        heappush(h, (1, nx))
        det[nx] = 1
        michi[nx] = 1

    while(h):
        # print(h)
        _, tgt = heappop(h)
        for nx in graph[tgt]:
            if det[nx] == INF:
                michi[nx] = tgt+1
                det[nx] = det[tgt] + 1
                heappush(h, (det[nx], nx))

    # print(det)
    for d in det:
        if d == INF:
            print("No")
            return
    print("Yes")
    for m in michi[1:]:
        print(m)
def main():
    n = getN()
    for _ in range(n):
        solve()
if __name__ == "__main__":
    solve()

