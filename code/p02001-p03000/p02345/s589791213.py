import sys

input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N, X, func, init_v):
        self.N = N
        self.func = func
        self.init_v = init_v
        self.__build(X)

    def __build(self, X):
        self.node = [self.init_v] * (2 * self.N)  # 1-based index
        for i, x in enumerate(X, self.N):
            self.node[i] = x
        for i in range(self.N - 1, 0, -1):
            self.node[i] = self.func(self.node[i << 1], self.node[i << 1 | 1])

    def update(self, i, x):
        i += self.N - 1
        self.node[i] = x
        while i > 1:
            i >>= 1
            self.node[i] = self.func(self.node[i << 1], self.node[i << 1 | 1])

    def query(self, l, r):
        dst_l = self.init_v
        dst_r = self.init_v
        l += self.N - 1
        r += self.N - 1
        while l < r:
            if l & 1:
                dst_l = self.func(dst_l, self.node[l])
                l += 1
            if r & 1:
                r -= 1
                dst_r = self.func(self.node[r], dst_r)
            l >>= 1
            r >>= 1
        return self.func(dst_l, dst_r)


def main():
    N, Q = map(int, input().split())
    a = [2 ** 31 - 1] * N

    st = SegmentTree(N, a, func=min, init_v=float("inf"))

    ans = []
    for _ in range(Q):
        com, x, y = map(int, input().split())
        if com == 0:
            # update
            x += 1  # For AOJ input type (0-based index)
            st.update(x, y)
        else:
            # find
            x += 1  # For AOJ input type (0-based index)
            y += 1  # For AOJ input type (0-based index)
            ans.append(st.query(x, y + 1))

    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()

