class SegmentTree():
    def __init__(self, values, merge_func=min, default=float("inf")):
        n = len(values)
        self.size = 1
        self.default = default
        self.merge = merge_func
        while self.size < n:
            self.size *= 2
        # tree[0] = empty
        # child of tree[n] = tree[n*2], tree[n*2+1]
        self.tree = [self.default] * self.size * 2
        for i in range(n):
            self.tree[self.size + i] = values[i]
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.merge(self.tree[i*2], self.tree[i*2+1])

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.merge(
                self.tree[index*2], self.tree[index*2+1])

    def __query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.default
        if a <= l and r <= b:
            return self.tree[k]
        left = self.__query(a, b, k*2, l, (l+r)//2)
        right = self.__query(a, b, k*2+1, (l+r)//2, r)
        return self.merge(left, right)

    # query segmentation value of [a, b)
    def query(self, a, b):
        return self.__query(a, b, 1, 0, self.size)


def main():
    N = int(input())
    H = list(map(int, input().split()))
    A = list(map(int, input().split()))
    RMQ = SegmentTree([0] * N, merge_func=max, default=0)
    for i in range(N):
        maximum = RMQ.query(0, H[i]-1)
        RMQ.update(H[i]-1, maximum + A[i])
    print(RMQ.query(0, N))


if __name__ == "__main__":
    main()
