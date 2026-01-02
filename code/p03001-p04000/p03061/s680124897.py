def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


class SEGMENT_TREE:
    def __init__(self, N):
        self.N = N
        self.tree = [0] * (2 * N)  # 問題により修正

    def init(self, arr):
        N = self.N
        for i in range(N):
            self.tree[N + i] = arr[i]
        for i in range(N - 1, 0, -1):
            self.tree[i] = gcd(
                self.tree[i * 2], self.tree[i * 2 + 1])  # 問題により修正

    def update(self, p, value):
        i = p + self.N
        self.tree[i] = value
        while i > 1:
            self.tree[i // 2] = gcd(self.tree[i], self.tree[i ^ 1])  # 問題により修正
            i //= 2

    def query(self, l, r):
        N = self.N
        res = 0  # 問題により修正
        l += N
        r += N
        while l < r:
            if (l & 1):
                res = gcd(res, self.tree[l])  # 問題により修正
                l += 1
            if (r & 1):
                r -= 1
                res = gcd(res, self.tree[r])  # 問題により修正
            l //= 2
            r //= 2
        return res


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    seg = SEGMENT_TREE(N)
    seg.init(A)
    ans = 0
    for i in range(N):
        tmp = gcd(seg.query(0, i), seg.query(i + 1, N))
        ans = max(ans, tmp)
    print(ans)
