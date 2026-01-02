class SegmentTree:

    __slots__ = ["func", "e", "n", "data"]

    def __init__(self, monoid_data, func, e):
        self.func = func
        self.e = e
        self.n = len(monoid_data)
        self.data = monoid_data * 2
        for i in range(self.n-1, 0, -1):
            self.data[i] = self.func(self.data[2*i], self.data[2*i+1])

    def replace(self, index, value):
        index += self.n
        self.data[index] = value
        index //= 2
        while index > 0:
            self.data[index] = self.func(self.data[2*index], self.data[2*index+1])
            index //= 2
        
    def folded(self, l, r):
        left_folded = self.e
        right_folded = self.e
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                left_folded = self.func(left_folded, self.data[l])
                l += 1
            if r % 2:
                r -= 1
                right_folded = self.func(self.data[r], right_folded)
            l //= 2
            r //= 2
        return self.func(left_folded, right_folded)

    def __getitem__(self, index):
        return self.data[self.n + index]

import sys
input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

N, K = map(int, input().split())
As = list(map(int, read().split()))

dp = SegmentTree([0] * 300001, max, 0)
for A in As:
    l = max(0, A - K)
    r = min(300001, A + K + 1)
    dp.replace(A, dp.folded(l, r) + 1)

print(dp.folded(0, 300001))