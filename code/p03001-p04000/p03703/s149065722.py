from bisect import bisect_right
import sys
input = sys.stdin.buffer.readline

class BIT:
    def __init__(self, size, values):
        self.size = size
        self.tree = [0] * (size + 1)

        self.values = values
        self.values.sort()
        self.vToI = {v: i for i, v in enumerate(self.values, start=1)}

    def lowerValueIndex(self, v):
        return self.vToI[self.values[bisect_right(self.values, v) - 1]]

    def add(self, index):
        index = self.vToI[index]
        while index <= self.size:
            self.tree[index] += 1
            index += index & (-index)

    def sum(self, index):
        index = self.lowerValueIndex(index)
        ret = 0
        while index:
            ret += self.tree[index]
            index -= index & (-index)
        return ret

    def search(self, value):
        i = 0
        s = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            if i + step <= self.size and s + self.tree[i + step] < value:
                i += step
                s += self.tree[i]
            step //= 2
        return i + 1

N, K = map(int, input().split())
A = [int(input()) - K for _ in range(N)]

accA = [0] * (N + 1)
for i, a in enumerate(A, start=1):
    accA[i] = accA[i - 1] + a

values = accA + [10**18]
values += [-v for v in values]
values = list(set(values))
tree = BIT(len(values), values)

ans = 0
for i, a in enumerate(accA):
    ans += i - tree.sum(-a - 1)
    tree.add(-a)
print(ans)
