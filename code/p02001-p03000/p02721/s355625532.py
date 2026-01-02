class SegmentTree:
    """Segment Tree (Point Update & Range Query)
    Query
        1. update(i, val): update i-th value to val
        2. query(low, high): find f(value) in [low, high)
    Complexity
        time complexity: O(log n)
        space complexity: O(n)
    """

    def __init__(self, N, f, default):
        self.N = 1 << (N - 1).bit_length()
        self.default = default
        self.f = f
        self.segtree = [self.default] * ((self.N << 1) - 1)

    @classmethod
    def create_from_array(cls, arr, f, default):
        N = len(arr)
        self = cls(N, f, default)
        for i in range(N):
            self.segtree[self.N - 1 + i] = arr[i]

        for i in reversed(range(self.N - 1)):
            self.segtree[i] = self.f(
                self.segtree[(i << 1) + 1], self.segtree[(i << 1) + 2]
            )
        return self

    def update(self, i, val):
        i += self.N - 1
        self.segtree[i] = val
        while i > 0:
            i = (i - 1) >> 1
            self.segtree[i] = self.f(
                self.segtree[(i << 1) + 1], self.segtree[(i << 1) + 2]
            )

    def __getitem__(self, k):
        return self.segtree[self.N - 1 + k]

    def query(self, low, high):
        # query [l, r)
        low, high = low + self.N, high + self.N
        left_ret, right_ret = self.default, self.default
        while low < high:
            if low & 1:
                left_ret = self.f(left_ret, self.segtree[low - 1])
                low += 1
            if high & 1:
                high -= 1
                right_ret = self.f(self.segtree[high - 1], right_ret)
            low, high = low >> 1, high >> 1
        return self.f(left_ret, right_ret)


def main() -> None:
    N, K, C = map(int, input().split())
    S = [1 if s == "o" else 0 for s in input()]
    left, right = [-1] * N, [-1] * N
    max_v = -1
    for i in range(N):
        if i - C - 1 >= 0:
            max_v = max(max_v, left[i - C - 1])
        if S[i] == 1:
            left[i] = max_v + 1
    max_v = -1
    for i in reversed(range(N)):
        if i + C + 1 <= N - 1:
            max_v = max(max_v, right[i + C + 1])
        if S[i] == 1:
            right[i] = max_v + 1
    work_day = [max(0, left[i] + right[i] + 1) for i in range(N)]
    #print(work_day)
    if max(work_day) > K:
        return
    segt = SegmentTree.create_from_array(work_day, max, 0)
    ans = []
    for i in range(N):
        if work_day[i] < K:
            continue
        m = max(segt.query(max(0, i - C), i), segt.query(i+1, min(i + 1 + C, N)))
        if m >= K:
            continue
        # m = max(segt.query(0, max(0, i - C)), segt.query(min(N, i + 1 + C), N))
        # if m >= K + 1:
        #     continue
        ans.append(i + 1)
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
