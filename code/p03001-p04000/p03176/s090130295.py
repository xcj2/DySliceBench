import operator


class SegmentTree:
    __slots__ = ('n', 'op', 'tree')

    def __init__(self, seq, op=operator.add):
        self.n = len(seq)
        self.op = op
        self.tree = [-1] * self.n + seq
        for i in reversed(range(1, self.n)):
            self.tree[i] = op(self.tree[2*i], self.tree[2*i+1])

    def modify(self, pos, val):
        assert pos < self.n
        pos += self.n
        self.tree[pos] = val
        while pos > 1:
            self.tree[pos//2] = self.op(self.tree[pos], self.tree[pos ^ 1])
            pos //= 2

    def query(self, L, R):
        assert L <= R and L >= 0 and R <= self.n
        res = 0
        L += self.n
        R += self.n
        while L < R:
            if L % 2 == 1:
                res = self.op(res, self.tree[L])
                L += 1
            if R % 2 == 1:
                R -= 1
                res = self.op(res, self.tree[R])

            L //= 2
            R //= 2

        return res


def solve(n, heights, beauty):
    dp = [0] * (n+1)
    st = SegmentTree(dp, op=max)

    for flower in range(n):
        pos = heights[flower]
        val = st.query(0, heights[flower]) + beauty[flower]
        st.modify(pos, val)

    return st.tree[1]


def main():
    n = int(input())
    heights = [int(c) for c in input().split()]
    beauty = [int(c) for c in input().split()]
    ans = solve(n, heights, beauty)
    print(ans)


if __name__ == "__main__":
    main()
