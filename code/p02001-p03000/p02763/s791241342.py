import sys

input = sys.stdin.readline


class SegmentTree:
    def __init__(self, N, X):
        self.N = N
        self.func = lambda x, y: x | y
        self.__build(X)

    def __build(self, X):
        # Initialize all nodes
        self.node = [set() for _ in range(2 * self.N)]

        # Elementary intervals are stored
        for i, s in enumerate(X, self.N):
            self.node[i].add(s)

        # The internal nodes correspond to intervals that are the union of elementary intervals
        for i in range(self.N - 1, 0, -1):
            self.node[i] = self.func(self.node[i << 1], self.node[i << 1 | 1])

    def update(self, i, s):
        i += self.N - 1
        if s in self.node[i]:
            return
        self.node[i] = set([s])
        while i > 1:
            i >>= 1
            self.node[i] = self.func(self.node[i << 1], self.node[i << 1 | 1])

    def query(self, l, r):
        """Query for right half-open interval [l, r).

        Args:
            l (int): index (1-based index)
            r (int): index (1-based index)
        """
        dst_l = set()
        dst_r = set()
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
    N = int(input())
    S = input().rstrip()

    S = list(S)
    st = SegmentTree(N, S)

    ans = []
    Q = int(input())
    for _ in range(Q):
        query = input().split()
        q = int(query[0])
        if q == 1:
            i = int(query[1])
            c = query[2]
            st.update(i, c)
        else:
            l = int(query[1])
            r = int(query[2])
            res = st.query(l, r + 1)
            ans.append(len(res))

    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
