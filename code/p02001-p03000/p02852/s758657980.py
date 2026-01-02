
class SegmentTree:
    def __init__(self, size, fn=min, default=None, initial_values=None):
        """
        :param int size:
        :param callable fn: 区間に適用する関数。引数を 2 つ取る。min, max, operator.xor など
        :param default:
        :param list initial_values:
        """
        default = default or 0

        # size 以上である最小の 2 冪を size とする
        n = 1
        while n < size:
            n *= 2
        self._size = n
        self._fn = fn

        self._tree = [default] * (self._size * 2 - 1)
        if initial_values:
            i = self._size - 1
            for v in initial_values:
                self._tree[i] = v
                i += 1
            i = self._size - 2
            while i >= 0:
                self._tree[i] = self._fn(self._tree[i * 2 + 1], self._tree[i * 2 + 2])
                i -= 1

    def set(self, i, value):
        """
        i 番目に value を設定
        :param int i:
        :param value:
        :return:
        """
        x = self._size - 1 + i
        self._tree[x] = value

        while x > 0:
            x = (x - 1) // 2
            self._tree[x] = self._fn(self._tree[x * 2 + 1], self._tree[x * 2 + 2])

    def update(self, i, value):
        """
        もとの i 番目と value に fn を適用したものを i 番目に設定
        :param int i:
        :param value:
        :return:
        """
        x = self._size - 1 + i
        self.set(i, self._fn(self._tree[x], value))

    def get(self, from_i, to_i=None, k=0, L=None, r=None):
        """
        [from_i, to_i) に fn を適用した結果を返す
        :param int from_i:
        :param int to_i:
        :param int k: self._tree[k] が、[L, r) に fn を適用した結果を持つ
        :param int L:
        :param int r:
        :return:
        """
        if to_i is None:
            return self._tree[self._size - 1 + from_i]

        L = 0 if L is None else L
        r = self._size if r is None else r

        if from_i <= L and r <= to_i:
            return self._tree[k]

        if to_i <= L or r <= from_i:
            return None

        ret_L = self.get(from_i, to_i, k * 2 + 1, L, (L + r) // 2)
        ret_r = self.get(from_i, to_i, k * 2 + 2, (L + r) // 2, r)
        if ret_L is None:
            return ret_r
        if ret_r is None:
            return ret_L
        return self._fn(ret_L, ret_r)

    def __len__(self):
        return self._size


def resolve():
    INF = float('inf')
    N, M = map(int, input().split())
    S = input()

    dp = [INF] * (N + 1)
    dp[0] = 0

    seg = SegmentTree(N + 1, min, INF)
    seg.update(N, 0)
    for i in range(N - 1, -1, -1):
        if S[i] == '1':
            continue
        # seg.query(l, r) := [l, r)の最小値
        dp[i] = seg.get(i, i + M + 1) + 1
        seg.update(i, dp[i])

    ans = []
    position = 0
    while position < N:
        for move in range(1, M + 1):
            if position + move > N:
                continue
            if S[position + move] == '1':
                continue

            # 最短手数にならない
            if dp[position + move] == dp[position]:
                continue

            ans.append(move)
            position += move
            break

        else:
            print(-1)
            return

    print(*ans)


if __name__ == "__main__":
    resolve()
