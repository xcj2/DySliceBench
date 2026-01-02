import sys
input = sys.stdin.readline


class SegmentTree():
    def __init__(self, values, default=float("inf")):
        n = len(values)
        self.size = 1
        self.default = default
        while self.size < n:
            self.size *= 2
        # tree[0] = empty
        # child of tree[n] = tree[n*2], tree[n*2+1]
        self.tree = [self.default] * self.size * 2
        for i in range(n):
            self.tree[self.size + i] = values[i]
        for i in range(self.size-1, 0, -1):
            self.tree[i] = min(self.tree[i*2], self.tree[i*2+1])

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = min(
                self.tree[index*2], self.tree[index*2+1])

    def __query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.default
        if a <= l and r <= b:
            return self.tree[k]
        left = self.__query(a, b, k*2, l, (l+r)//2)
        right = self.__query(a, b, k*2+1, (l+r)//2, r)
        return min(left, right)

    # query segmentation value of [a, b)
    def query(self, a, b):
        return self.__query(a, b, 1, 0, self.size)


def main():
    N, M = map(int, input().split())
    op = [None] * M
    for i in range(M):
        L, R, C = map(int, input().split())
        op[i] = (L-1, R-1, C)
    op.sort()
    tree = SegmentTree([float("inf")] * N)
    tree.update(0, 0)
    for l, r, c in op:
        mn = tree.query(l, r)
        current = tree.tree[tree.size + r]
        if mn+c < current:
            tree.update(r, mn+c)
    ans = tree.query(N-1, N)
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
