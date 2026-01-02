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
        self.range = [None] * self.size * 2
        for i in range(n):
            self.tree[self.size + i] = values[i]
        for i in range(self.size):
            self.range[self.size + i] = (i, i+1)
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.merge(self.tree[i*2], self.tree[i*2+1])
            self.range[i] = (self.range[i*2][0], self.range[i*2+1][1])

    def get(self, index):
        return self.tree[self.size + index]

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.merge(
                self.tree[index*2], self.tree[index*2+1])

    # query segmentation value of [a, b)
    def query(self, a, b):
        q = [1]
        ret = self.default
        while len(q):
            k = q.pop()
            l, r = self.range[k]
            if r <= a or b <= l:
                continue
            if a <= l and r <= b:
                ret = self.merge(ret, self.tree[k])
            else:
                q.append(k*2)
                q.append(k*2+1)
        return ret


def main():
    MAX = 300001
    N, K = map(int, input().split())
    rmq = SegmentTree([0]*MAX, merge_func=max, default=0)
    for _ in range(N):
        A = int(input())
        mx = rmq.query(A-K, A+K+1)
        rmq.update(A, mx+1)
    ans = rmq.query(0, MAX)
    print(ans)


if __name__ == "__main__":
    main()
